/* Service Worker for Local Book Reader — offline support + PWA.
   Bump CACHE_VERSION on every deploy that changes cached assets so old
   caches are cleaned up on activate. */
const CACHE_VERSION = 'v2';
const SHELL_CACHE = 'reader-shell-' + CACHE_VERSION;
const RUNTIME_CACHE = 'reader-runtime-' + CACHE_VERSION;

/* App shell — same-origin files needed to boot offline. */
const SHELL_ASSETS = [
  './',
  'index.html',
  'manifest.json',
  'icon.svg'
];

/* Cross-origin CDN hosts whose responses we cache at runtime so the app
   (PDF/EPUB parsing, icons and fonts) keeps working fully offline. */
const RUNTIME_HOSTS = [
  'cdnjs.cloudflare.com',
  'cdn.jsdelivr.net',
  'fonts.googleapis.com',
  'fonts.gstatic.com'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      // addAll is atomic; reload avoids serving an HTTP-cached stale shell.
      .then(cache => cache.addAll(
        SHELL_ASSETS.map(url => new Request(url, { cache: 'reload' }))
      ))
      .then(() => self.skipWaiting())
      .catch(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(key => key !== SHELL_CACHE && key !== RUNTIME_CACHE)
          .map(key => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

/* Cache-first with background refresh: serve the cached copy instantly,
   but still hit the network to keep the cache fresh for next time. */
function staleWhileRevalidate(request, cacheName){
  return caches.open(cacheName).then(cache =>
    cache.match(request).then(cached => {
      const network = fetch(request).then(response => {
        // Cache successful or opaque (cross-origin, no-cors) responses.
        if(response && (response.ok || response.type === 'opaque')){
          cache.put(request, response.clone()).catch(() => {});
        }
        return response;
      }).catch(() => cached);
      return cached || network;
    })
  );
}

self.addEventListener('fetch', event => {
  const request = event.request;
  if(request.method !== 'GET') return;

  let url;
  try { url = new URL(request.url); }
  catch(e){ return; }

  // Cross-origin CDN dependencies — runtime cache, cache-first.
  if(RUNTIME_HOSTS.indexOf(url.hostname) !== -1){
    event.respondWith(staleWhileRevalidate(request, RUNTIME_CACHE));
    return;
  }

  // Same-origin requests — cache-first, falling back to network.
  if(url.origin === self.location.origin){
    event.respondWith(
      caches.match(request).then(cached => {
        if(cached) return cached;
        return fetch(request).then(response => {
          if(response && response.ok){
            const copy = response.clone();
            caches.open(RUNTIME_CACHE)
              .then(cache => cache.put(request, copy))
              .catch(() => {});
          }
          return response;
        }).catch(() => {
          // Navigation fallback: serve the app shell when offline.
          if(request.mode === 'navigate'){
            return caches.match('index.html');
          }
        });
      })
    );
  }
});

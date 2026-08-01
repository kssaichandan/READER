Render deployment steps

1. Create a Git repository and push this project (see `git-deploy.ps1` or `git-deploy.sh`).

2. Sign in to https://dashboard.render.com and create a new Static Site:
   - Connect your GitHub/GitLab account
   - Select the repository you pushed
   - Build command: leave empty (static site)
   - Publish directory: `.`

3. After Render finishes building, open the provided URL to verify the site.

Quick health check (replace with your Render URL):

```bash
curl -I https://your-site.onrender.com
```

If you want me to create the Render service via the API or `render` CLI, provide a Render API key and repo details and I can prepare an automated script.

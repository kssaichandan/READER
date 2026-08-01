#!/usr/bin/env bash
# Simple helper to initialize git repo and push to remote.
set -euo pipefail
if [ ! -d .git ]; then
  git init
  echo "Initialized git repository"
fi
if [ -z "$(git status --porcelain)" ]; then
  echo "No changes to commit"
else
  git add .
  git commit -m "Minimal reader: responsive UI + PDF/EPUB support"
fi
if ! git remote get-url origin >/dev/null 2>&1; then
  read -p "Enter remote URL (e.g. https://github.com/you/repo.git): " REMOTE
  if [ -n "$REMOTE" ]; then
    git remote add origin "$REMOTE"
  fi
fi
git branch -M main
echo "Pushing to origin main..."
git push -u origin main
echo "Done. If push failed, check your remote and credentials."

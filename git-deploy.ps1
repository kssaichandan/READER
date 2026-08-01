<#
PowerShell helper to initialize a git repo, set remote and push.
Run from project root. You will be prompted for a remote URL if none is set.
#>
param(
  [string]$RemoteUrl
)
if(-not (Test-Path .git)){
  git init
  Write-Host "Initialized git repository"
}
if(-not (git status --porcelain)){
  Write-Host "No changes to commit"
} else {
  git add .
  git commit -m "Minimal reader: responsive UI + PDF/EPUB support"
}
try{
  $remotes = git remote
}catch{
  $remotes = @()
}
if(-not $remotes -or -not (git remote get-url origin 2>$null)){
  if(-not $RemoteUrl){ $RemoteUrl = Read-Host 'Enter remote repository URL (e.g. https://github.com/you/repo.git)'; }
  if($RemoteUrl){ git remote add origin $RemoteUrl; Write-Host "Added remote origin -> $RemoteUrl" }
}
git branch -M main
Write-Host "Pushing to origin main... you may be prompted for credentials"
git push -u origin main
Write-Host "Done. If push failed, verify your remote URL and credentials and try again."

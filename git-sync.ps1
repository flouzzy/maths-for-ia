$vaultDir = $PSScriptRoot
Set-Location -Path $vaultDir

# Vérifier s'il y a des changements
$status = wsl git status --porcelain
if ($status) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    wsl git add .
    wsl git commit -m "Auto-sync: $date"
    wsl git push origin main
    Write-Output "Synchronisé avec succès le $date"
} else {
    Write-Output "Rien à synchroniser."
}

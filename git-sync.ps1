$vaultDir = "c:\Users\Charles\Documents\MathsIA\MathsIA"
Set-Location -Path $vaultDir

# Vérifier s'il y a des changements
$status = & "C:\Program Files\Git\cmd\git.exe" status --porcelain
if ($status) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    & "C:\Program Files\Git\cmd\git.exe" add .
    & "C:\Program Files\Git\cmd\git.exe" commit -m "Auto-sync: $date"
    & "C:\Program Files\Git\cmd\git.exe" push origin main
    Write-Output "Synchronisé avec succès le $date"
} else {
    Write-Output "Rien à synchroniser."
}

# Script para configurar variables de entorno para Radio2 Updates
# Ejecutar este script antes de usar upload_update.py

Write-Host "Configurando variables de entorno para Radio2 Updates..." -ForegroundColor Green

# Configurar variables de entorno
$env:GITHUB_TOKEN = "TU_TOKEN_GITHUB_AQUI"
$env:GITHUB_USER = "userserverbackup"
$env:UPDATE_REPO = "radio2-updates"

Write-Host "Variables configuradas:" -ForegroundColor Yellow
Write-Host "GITHUB_TOKEN=*** (oculto por seguridad)" -ForegroundColor Red
Write-Host "GITHUB_USER=$env:GITHUB_USER" -ForegroundColor Cyan
Write-Host "UPDATE_REPO=$env:UPDATE_REPO" -ForegroundColor Cyan

Write-Host ""
Write-Host "Para usar el script de actualización:" -ForegroundColor Green
Write-Host "1. Ejecuta este script: .\setup_env.ps1" -ForegroundColor White
Write-Host "2. Luego ejecuta: python scripts/upload_update.py" -ForegroundColor White
Write-Host ""
Write-Host "Presiona cualquier tecla para continuar..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 
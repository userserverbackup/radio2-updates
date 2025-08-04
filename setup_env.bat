@echo off
REM Script para configurar variables de entorno para Radio2 Updates
REM Ejecutar este script antes de usar upload_update.py

echo Configurando variables de entorno para Radio2 Updates...

REM Configurar variables de entorno
set GITHUB_TOKEN=TU_TOKEN_GITHUB_AQUI
set GITHUB_USER=userserverbackup
set UPDATE_REPO=radio2-updates

echo Variables configuradas:
echo GITHUB_TOKEN=*** (oculto por seguridad)
echo GITHUB_USER=%GITHUB_USER%
echo UPDATE_REPO=%UPDATE_REPO%

echo.
echo Para usar el script de actualización:
echo 1. Ejecuta este script: setup_env.bat
echo 2. Luego ejecuta: python scripts/upload_update.py
echo.
pause 
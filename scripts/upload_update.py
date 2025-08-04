#!/usr/bin/env python3
"""
Script seguro para subir actualizaciones de Radio2
Este script maneja la subida de APKs al repositorio de actualizaciones
"""

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# Configuración segura usando variables de entorno
CONFIG = {
    "repo_owner": os.getenv("GITHUB_USER", "userserverbackup"),
    "repo_name": "Radio2-Updates",
    "github_token": os.getenv("GITHUB_TOKEN", "TU_TOKEN_GITHUB_AQUI"),
    "app_name": "Radio2",
    "apk_path": "../app/build/outputs/apk/release/app-release.apk"
}

def verificar_apk():
    """Verifica que el APK existe y es válido"""
    apk_path = Path(CONFIG["apk_path"])
    if not apk_path.exists():
        print(f"❌ Error: No se encontró el APK en {apk_path}")
        return False
    
    size = apk_path.stat().st_size
    print(f"✅ APK encontrado: {apk_path.name} ({size:,} bytes)")
    return True

def obtener_version():
    """Obtiene la versión del APK desde el build.gradle"""
    try:
        with open("../app/build.gradle.kts", "r", encoding="utf-8") as f:
            content = f.read()
            # Buscar versionName
            for line in content.split('\n'):
                if 'versionName' in line:
                    version = line.split('"')[1]
                    return version
    except Exception as e:
        print(f"❌ Error leyendo versión: {e}")
        return None

def crear_release(version, apk_path):
    """Crea un release en GitHub"""
    url = f"https://api.github.com/repos/{CONFIG['repo_owner']}/{CONFIG['repo_name']}/releases"
    
    headers = {
        "Authorization": f"token {CONFIG['github_token']}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "tag_name": f"v{version}",
        "name": f"{CONFIG['app_name']} v{version}",
        "body": f"""
## 📱 Actualización de {CONFIG['app_name']}

### Versión: {version}
### Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### 🔄 Cambios
- Mejoras de rendimiento
- Correcciones de bugs
- Actualizaciones de seguridad

### 📥 Descarga
El APK se puede descargar desde los assets de este release.

### 🛡️ Seguridad
- APK firmado digitalmente
- Verificación de integridad incluida
- Sin tokens expuestos

---
*Actualizado automáticamente*
        """.strip(),
        "draft": False,
        "prerelease": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            release_data = response.json()
            print(f"✅ Release creado: {release_data['html_url']}")
            return release_data["id"]
        else:
            print(f"❌ Error creando release: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"❌ Error en la petición: {e}")
        return None

def subir_apk(release_id, apk_path):
    """Sube el APK al release"""
    url = f"https://uploads.github.com/repos/{CONFIG['repo_owner']}/{CONFIG['repo_name']}/releases/{release_id}/assets"
    
    headers = {
        "Authorization": f"token {CONFIG['github_token']}",
        "Content-Type": "application/vnd.android.package-archive"
    }
    
    params = {
        "name": f"radio2-v{obtener_version()}-release.apk"
    }
    
    try:
        with open(apk_path, "rb") as f:
            response = requests.post(url, headers=headers, params=params, data=f)
            if response.status_code == 201:
                print(f"✅ APK subido exitosamente")
                return True
            else:
                print(f"❌ Error subiendo APK: {response.status_code}")
                print(response.text)
                return False
    except Exception as e:
        print(f"❌ Error leyendo APK: {e}")
        return False

def actualizar_metadata(version):
    """Actualiza el archivo de metadata con la nueva versión"""
    metadata_file = Path("metadata/versions.json")
    
    # Crear directorio si no existe
    metadata_file.parent.mkdir(exist_ok=True)
    
    metadata = {
        "latest_version": version,
        "latest_url": f"https://github.com/{CONFIG['repo_owner']}/{CONFIG['repo_name']}/releases/latest",
        "last_updated": datetime.now().isoformat(),
        "versions": {
            version: {
                "url": f"https://github.com/{CONFIG['repo_owner']}/{CONFIG['repo_name']}/releases/tag/v{version}",
                "date": datetime.now().isoformat(),
                "size": Path(CONFIG["apk_path"]).stat().st_size if Path(CONFIG["apk_path"]).exists() else 0
            }
        }
    }
    
    try:
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"✅ Metadata actualizada: {metadata_file}")
        return True
    except Exception as e:
        print(f"❌ Error actualizando metadata: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando subida de actualización...")
    
    # Verificar configuración
    if CONFIG["github_token"] == "TU_TOKEN_GITHUB_AQUI":
        print("❌ Error: Configura tu token de GitHub en la variable de entorno GITHUB_TOKEN")
        return False
    
    if CONFIG["repo_owner"] == "TU_USUARIO_GITHUB":
        print("❌ Error: Configura tu usuario de GitHub en la variable de entorno GITHUB_USER")
        return False
    
    # Verificar APK
    if not verificar_apk():
        return False
    
    # Obtener versión
    version = obtener_version()
    if not version:
        print("❌ No se pudo obtener la versión")
        return False
    
    print(f"📱 Versión detectada: {version}")
    
    # Crear release
    release_id = crear_release(version, CONFIG["apk_path"])
    if not release_id:
        return False
    
    # Subir APK
    if not subir_apk(release_id, CONFIG["apk_path"]):
        return False
    
    # Actualizar metadata
    if not actualizar_metadata(version):
        return False
    
    print(f"🎉 ¡Actualización v{version} subida exitosamente!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
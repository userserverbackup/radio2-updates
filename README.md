# Radio2 Updates Repository

Este repositorio está dedicado exclusivamente a las actualizaciones de la aplicación Radio2.

## 📱 Propósito

- Almacenar APKs de releases
- Gestionar actualizaciones automáticas
- Mantener historial de versiones
- Proporcionar endpoint seguro para descargas

## 🚀 Estructura

```
Radio2-Updates/
├── releases/          # APKs de releases
├── metadata/          # Información de versiones
├── scripts/           # Scripts de automatización
└── README.md         # Este archivo
```

## 📋 Versiones Disponibles

Las versiones se organizan por carpetas con el formato: `vX.Y.Z`

### Última Versión
- **v1.5.42** - Versión estable actual

## 🔧 Configuración

### Para Desarrolladores
1. Configurar variables de entorno:
   ```bash
   export GITHUB_TOKEN="tu_token_aqui"
   export GITHUB_USER="userserverbackup"
   ```
2. Compilar APK: `./gradlew assembleRelease`
3. Subir a releases: `python scripts/upload_update.py`
4. Crear tag: `git tag v1.5.43`

### Para Usuarios
La aplicación se actualiza automáticamente desde este repositorio.

## 🛡️ Seguridad

- Solo APKs firmados
- Verificación de integridad
- Tokens seguros en variables de entorno
- Sin código fuente expuesto

## 📞 Contacto

Para reportar problemas con actualizaciones, contactar al desarrollador principal.

---

**Última actualización:** Diciembre 2024  
**Estado:** ✅ Activo y funcionando 
# Despliegue en Render - E-Learning JCB Reflex

Guía completa para desplegar la aplicación E-Learning JCB Reflex en Render.com.

## Problema de WebSockets en Render

### Diagnóstico

El error que aparece en la consola del navegador:

```
WebSocket connection to 'wss://jcb-daw-project-reflex.onrender.com/_event/?token=...' failed
```

Indica que los WebSockets no están conectándose correctamente. Esto puede deberse a:

1. **Plan gratuito de Render**: El plan gratuito puede tener limitaciones con WebSockets
2. **Cold starts**: El servidor se duerme después de 15 minutos de inactividad
3. **Configuración incorrecta**: Falta configuración de producción en `rxconfig.py`
4. **Comando de inicio incorrecto**: El servicio debe correr en modo producción

### Solución Implementada

Se han realizado los siguientes cambios:

#### 1. Actualización de `rxconfig.py`

```python
# Configuración mejorada para producción
config = rx.Config(
    app_name="E_Learning_JCB_Reflex",
    backend_port=int(os.getenv("BACKEND_PORT", "8000")),
    frontend_port=int(os.getenv("FRONTEND_PORT", "3000")),
    api_url=os.getenv("API_URL"),
    backend_host="0.0.0.0",  # Escuchar en todas las interfaces
    cors_allowed_origins=[...],  # Configurado para producción
)
```

#### 2. Creación de `render.yaml`

Archivo de configuración para Render con:
- Build command optimizado
- Start command correcto para producción
- Variables de entorno necesarias
- Healthcheck configurado

## Pasos para Desplegar en Render

### Opción A: Usando render.yaml (Recomendado)

1. **Commit y push de los cambios**:
   ```bash
   git add rxconfig.py render.yaml
   git commit -m "[CDP] Configurar despliegue en Render con soporte WebSockets"
   git push origin main
   ```

2. **En Render Dashboard**:
   - Ve a https://dashboard.render.com/
   - Click en "New +" → "Blueprint"
   - Conecta tu repositorio de GitHub
   - Render detectará automáticamente el `render.yaml`
   - Click en "Apply"

3. **Configurar variables de entorno**:
   En el dashboard de tu servicio, añade:
   ```
   MONGODB_URI=mongodb+srv://tu-conexion-mongodb-atlas
   ENVIRONMENT=production
   API_URL=https://tu-app.onrender.com
   FRONTEND_URL=https://tu-app.onrender.com
   ```

### Opción B: Configuración Manual

1. **Crear nuevo Web Service**:
   - Dashboard → "New +" → "Web Service"
   - Conecta tu repositorio

2. **Configuración del servicio**:
   ```
   Name: jcb-daw-project-reflex
   Region: Frankfurt (o tu región preferida)
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt && reflex init && reflex export --frontend-only --no-zip
   Start Command: reflex run --env prod --backend-only
   ```

3. **Variables de entorno** (mismas que Opción A)

## Solución al Problema de WebSockets

### El problema principal

Reflex necesita que tanto el backend como el frontend estén correctamente configurados para WebSockets en producción. El error ocurre porque:

1. **El backend no está escuchando correctamente** en la URL de producción
2. **CORS no está configurado** para permitir conexiones WebSocket
3. **El comando de inicio** no está usando el modo de producción

### La solución

La configuración actualizada:

```python
# rxconfig.py
backend_host="0.0.0.0"  # CRÍTICO: Permite conexiones externas
api_url=os.getenv("API_URL")  # Usa la URL de producción
cors_allowed_origins=[...]  # Permite conexiones del frontend
```

Y el comando de inicio correcto:

```bash
reflex run --env prod --backend-only
```

Esto asegura que:
- ✅ El backend escucha en todas las interfaces (0.0.0.0)
- ✅ Usa la URL correcta de producción con HTTPS
- ✅ Los WebSockets usan WSS (WebSocket Secure) en lugar de WS
- ✅ CORS está configurado correctamente

## Limitaciones del Plan Gratuito de Render

⚠️ **Importante**: El plan gratuito de Render tiene limitaciones:

1. **Cold starts**: El servicio se duerme después de 15 minutos sin actividad
2. **Primer acceso lento**: Puede tardar 30-60 segundos en "despertar"
3. **WebSockets pueden desconectarse**: Durante cold starts
4. **750 horas/mes gratis**: Suficiente para desarrollo/demostración

### Recomendaciones

Para producción real, considera:

1. **Plan Starter de Render** ($7/mes):
   - Sin cold starts
   - WebSockets más estables
   - Mejor rendimiento

2. **Railway.app** (Alternativa):
   - Similar a Render
   - Mejor soporte para WebSockets en plan gratuito
   - $5 de crédito gratis al mes

3. **Docker + VPS** (Mayor control):
   - DigitalOcean, Linode, etc.
   - Desde $5/mes
   - Control total del servidor

## Verificación del Despliegue

1. **Verificar que el servicio está corriendo**:
   - Ve al dashboard de Render
   - Comprueba que el estado es "Live"
   - Revisa los logs para errores

2. **Probar la aplicación**:
   - Abre la URL de tu aplicación
   - Verifica que carga correctamente
   - Abre la consola del navegador (F12)
   - Busca errores de WebSocket

3. **Si los WebSockets siguen fallando**:
   - Verifica las variables de entorno
   - Comprueba que `API_URL` es la URL completa con HTTPS
   - Verifica que el servicio está usando Python 3.14
   - Revisa los logs del backend en Render

## Debugging

### Ver logs en tiempo real

```bash
# En el dashboard de Render, ve a "Logs"
# O usa Render CLI:
render logs -f
```

### Verificar variables de entorno

En el dashboard de Render:
1. Ve a tu servicio
2. Click en "Environment"
3. Verifica que todas las variables estén configuradas

### Probar localmente en modo producción

```bash
# Activar entorno
source reflex-env/bin/activate

# Configurar variables de entorno
export ENVIRONMENT=production
export API_URL=http://localhost:8000
export FRONTEND_URL=http://localhost:3000

# Ejecutar en modo producción
reflex run --env prod
```

## Solución Rápida si WebSockets Fallan

Si después de aplicar todos los cambios, los WebSockets siguen fallando:

### Opción 1: Cambiar a Railway.app

Railway tiene mejor soporte para WebSockets en su plan gratuito:

1. Ve a https://railway.app
2. Conecta tu repositorio de GitHub
3. Railway detecta automáticamente que es una app Python
4. Añade las mismas variables de entorno
5. Deploy automático

### Opción 2: Usar Reflex Hosting (Oficial)

Reflex ofrece hosting oficial optimizado para aplicaciones Reflex:

```bash
reflex deploy
```

Sigue las instrucciones en: https://reflex.dev/docs/hosting/deploy/

## Notas Importantes

1. **MongoDB Atlas**: Asegúrate de que tu cluster de MongoDB permite conexiones desde cualquier IP (0.0.0.0/0) o añade la IP de Render a la whitelist

2. **Primer despliegue**: Puede tardar 5-10 minutos en completarse

3. **Actualizaciones**: Render redespliega automáticamente cuando haces push a la rama main

4. **Logs**: Revisa siempre los logs para diagnosticar problemas

5. **HTTPS**: Render proporciona HTTPS automáticamente, asegúrate de que `API_URL` usa `https://`

## Recursos Adicionales

- [Documentación de Render](https://render.com/docs)
- [Documentación de Reflex Hosting](https://reflex.dev/docs/hosting/deploy/)
- [Guía de WebSockets en Reflex](https://reflex.dev/docs/advanced/websocket/)
- [Railway como alternativa](https://railway.app)

---

**Última actualización**: 2025-12-22
**Versión**: 1.0

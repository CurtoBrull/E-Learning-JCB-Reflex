# Despliegue en Reflex Cloud - E-Learning JCB

Guía completa para desplegar la aplicación E-Learning JCB en Reflex Cloud (hosting oficial de Reflex).

## ¿Por qué Reflex Cloud?

Reflex Cloud es el servicio de hosting oficial de Reflex, diseñado específicamente para aplicaciones Reflex. Ventajas:

- ✅ **WebSockets funcionan perfectamente** (sin configuración adicional)
- ✅ **Optimizado para Reflex** (mejor rendimiento)
- ✅ **SSL/HTTPS automático**
- ✅ **Despliegue con un solo comando** (`reflex deploy`)
- ✅ **Escalado automático**
- ✅ **Monitoreo incluido**
- ✅ **Sin cold starts** (en planes de pago)

## Requisitos Previos

1. **Cuenta en Reflex Cloud**:
   - Visita: https://reflex.dev/
   - Crea una cuenta gratuita
   - Verifica tu email

2. **MongoDB Atlas configurado**:
   - Tu connection string de MongoDB
   - Whitelist configurada para permitir todas las IPs (0.0.0.0/0)

3. **Repositorio Git**:
   - Todo tu código debe estar commiteado
   - Push a GitHub/GitLab (recomendado para CI/CD)

## Pasos para Desplegar

### 1. Autenticarse en Reflex Cloud

Primero, inicia sesión desde la terminal:

```bash
# Activar entorno virtual
source reflex-env/bin/activate

# Autenticarse (abrirá el navegador)
reflex login
```

Esto abrirá tu navegador para autenticarte. Una vez autenticado, vuelve a la terminal.

### 2. Preparar Variables de Entorno

Crea un archivo `.env.production` con tus variables de producción:

```bash
# Copiar el ejemplo
cp .env.production.example .env.production

# Editar con tu editor favorito
nano .env.production
```

Contenido del archivo `.env.production`:

```env
ENVIRONMENT=production
MONGODB_URI=mongodb+srv://tu-usuario:tu-password@cluster.mongodb.net/elearning-jcb-db?retryWrites=true&w=majority
```

⚠️ **IMPORTANTE**: NO commitees el archivo `.env.production` al repositorio. Ya está en `.gitignore`.

### 3. Desplegar la Aplicación

Existen dos formas de desplegar:

#### Opción A: Despliegue Interactivo (Recomendado para primera vez)

```bash
reflex deploy --interactive
```

Este comando te guiará paso a paso:

1. **Nombre de la app**: Ej. `elearning-jcb`
2. **Región**: Elige la más cercana a tus usuarios
   - `sjc` - San José, California (USA West)
   - `iad` - Washington DC (USA East)
   - `fra` - Frankfurt (Europe)
   - `sin` - Singapore (Asia)
3. **Variables de entorno**: Se cargarán desde `.env.production`
4. **Tipo de VM**: Elige según tu presupuesto
   - `free` - Gratis (1 CPU, 512MB RAM)
   - `basic` - $20/mes (1 CPU, 1GB RAM)
   - `standard` - $40/mes (2 CPU, 2GB RAM)

#### Opción B: Despliegue No Interactivo (Para CI/CD)

```bash
reflex deploy \
  --no-interactive \
  --app-name elearning-jcb \
  --region fra \
  --vmtype free \
  --envfile .env.production
```

### 4. Verificar el Despliegue

Una vez completado el despliegue, Reflex te mostrará:

```
✅ Deployment successful!
🌐 Frontend URL: https://elearning-jcb.reflex.run
🔧 Backend URL: https://elearning-jcb-backend.reflex.run
📊 Dashboard: https://cloud.reflex.dev/projects/your-project-id
```

Abre la URL del frontend en tu navegador y verifica que:

1. La aplicación carga correctamente
2. No hay errores de WebSocket en la consola (F12)
3. Puedes navegar entre páginas
4. La conexión a MongoDB funciona

## Gestión del Despliegue

### Ver Logs en Tiempo Real

```bash
# Ver logs del backend
reflex logs --app-name elearning-jcb

# Ver logs con auto-refresh
reflex logs --app-name elearning-jcb --follow
```

### Actualizar la Aplicación

Para redesplegar después de hacer cambios:

```bash
# 1. Asegúrate de tener todos los cambios commiteados
git add .
git commit -m "[CDP] Descripción de cambios"
git push

# 2. Redesplegar
reflex deploy --app-name elearning-jcb
```

### Ver Estado de la Aplicación

```bash
# Listar todas tus aplicaciones
reflex cloud apps

# Ver detalles de una app específica
reflex cloud app --app-name elearning-jcb
```

### Actualizar Variables de Entorno

Si necesitas cambiar variables de entorno sin redesplegar:

```bash
# Actualizar una variable
reflex deploy --app-name elearning-jcb --env MONGODB_URI=nueva-uri

# Actualizar desde archivo
reflex deploy --app-name elearning-jcb --envfile .env.production
```

### Eliminar el Despliegue

```bash
reflex cloud delete --app-name elearning-jcb
```

## Dominios Personalizados

Para usar tu propio dominio (ej: `elearning.midominio.com`):

### 1. Configurar Dominio en Reflex Cloud

```bash
reflex deploy --app-name elearning-jcb --hostname elearning.midominio.com
```

### 2. Configurar DNS

En tu proveedor de DNS (GoDaddy, Cloudflare, etc.), añade un registro CNAME:

```
Tipo: CNAME
Nombre: elearning
Valor: elearning-jcb.reflex.run
TTL: 3600 (o automático)
```

### 3. Verificar

Espera a que se propague el DNS (puede tardar hasta 24 horas, usualmente 5-10 minutos) y visita tu dominio personalizado.

## Configuración de Regiones Múltiples

Para mejor rendimiento global, despliega en múltiples regiones:

```bash
reflex deploy \
  --app-name elearning-jcb \
  --region fra \
  --region sjc \
  --region sin \
  --vmtype standard
```

Reflex Cloud automáticamente enrutará a los usuarios a la región más cercana.

## Monitoreo y Métricas

### Dashboard Web

Accede a https://cloud.reflex.dev/ para ver:

- 📊 Métricas de uso (CPU, RAM, requests)
- 📈 Gráficos de tráfico
- 🔍 Logs en tiempo real
- ⚠️ Alertas y errores

### Alertas por Email

Configura alertas en el dashboard para recibir notificaciones sobre:

- Errores del servidor
- Uso excesivo de recursos
- Tiempo de inactividad

## Troubleshooting

### Error: "Authentication failed"

```bash
# Cerrar sesión y volver a autenticar
reflex logout
reflex login
```

### Error: "App name already exists"

```bash
# Listar tus apps para ver nombres disponibles
reflex cloud apps

# Usar un nombre diferente o eliminar la app existente
reflex cloud delete --app-name nombre-existente
```

### Error: "MongoDB connection failed"

Verifica:

1. El `MONGODB_URI` es correcto
2. MongoDB Atlas permite conexiones desde cualquier IP (0.0.0.0/0)
3. Las credenciales son correctas
4. La base de datos existe

```bash
# Ver las variables de entorno configuradas
reflex cloud app --app-name elearning-jcb
```

### Error: "Build failed"

Revisa los logs del build:

```bash
reflex logs --app-name elearning-jcb --build
```

Posibles causas:

- Error en `requirements.txt`
- Error de sintaxis en el código Python
- Dependencias faltantes

### WebSockets no funcionan

Esto NO debería ocurrir en Reflex Cloud, pero si ocurre:

1. Verifica que estés usando la URL correcta (`https://...reflex.run`)
2. Comprueba que no haya bloqueadores de WebSocket en tu red
3. Revisa los logs del backend

```bash
reflex logs --app-name elearning-jcb --follow
```

## Comparación de Planes

| Plan | Precio | CPU | RAM | Storage | WebSockets | SSL | Custom Domain |
|------|--------|-----|-----|---------|------------|-----|---------------|
| **Free** | $0 | 0.5 | 512MB | 1GB | ✅ | ✅ | ❌ |
| **Basic** | $20/mes | 1 | 1GB | 10GB | ✅ | ✅ | ✅ |
| **Standard** | $40/mes | 2 | 2GB | 20GB | ✅ | ✅ | ✅ |
| **Pro** | $80/mes | 4 | 4GB | 50GB | ✅ | ✅ | ✅ |

Ver planes actualizados: https://reflex.dev/pricing/

## Mejores Prácticas

### 1. Usar CI/CD con GitHub Actions

Crea `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Reflex Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.14'
      - name: Install Reflex
        run: pip install reflex
      - name: Deploy
        env:
          REFLEX_TOKEN: ${{ secrets.REFLEX_TOKEN }}
        run: |
          reflex deploy \
            --no-interactive \
            --app-name elearning-jcb \
            --token $REFLEX_TOKEN \
            --envfile .env.production
```

### 2. Separar Entornos (Staging y Production)

```bash
# Staging
reflex deploy --app-name elearning-jcb-staging --vmtype free

# Production
reflex deploy --app-name elearning-jcb --vmtype standard --region fra --region sjc
```

### 3. Backup de MongoDB

Configura backups automáticos en MongoDB Atlas:

1. Ve a tu cluster en MongoDB Atlas
2. Click en "Backup"
3. Habilita "Continuous Backup" (recomendado para producción)

### 4. Monitoreo de Errores

Integra Sentry o similar para trackear errores en producción:

```bash
pip install sentry-sdk

# En tu código
import sentry_sdk
sentry_sdk.init(dsn="tu-sentry-dsn")
```

## Migración desde Render

Si ya tienes la app en Render:

1. **Exporta los datos** (si es necesario)
2. **Despliega en Reflex Cloud** siguiendo esta guía
3. **Verifica que funciona** correctamente
4. **Actualiza DNS** para apuntar al nuevo dominio
5. **Elimina el servicio de Render**

## Recursos Adicionales

- [Documentación oficial de Reflex Deploy](https://reflex.dev/docs/hosting/deploy/)
- [Reflex Cloud Dashboard](https://cloud.reflex.dev/)
- [Reflex Discord (Soporte)](https://discord.gg/reflex-dev)
- [Pricing de Reflex Cloud](https://reflex.dev/pricing/)

## Comandos Útiles (Cheatsheet)

```bash
# Autenticación
reflex login                    # Iniciar sesión
reflex logout                   # Cerrar sesión

# Despliegue
reflex deploy                   # Desplegar (interactivo)
reflex deploy --no-interactive  # Desplegar (no interactivo)

# Gestión
reflex cloud apps               # Listar apps
reflex cloud app --app-name X   # Ver detalles de app
reflex cloud delete --app-name X # Eliminar app

# Logs
reflex logs --app-name X        # Ver logs
reflex logs --app-name X -f     # Ver logs en tiempo real

# Regiones y VMs
reflex cloud regions            # Ver regiones disponibles
reflex cloud vmtypes            # Ver tipos de VM disponibles
```

---

**Última actualización**: 2025-12-22
**Versión**: 1.0

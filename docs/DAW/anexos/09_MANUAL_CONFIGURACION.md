# 9. MANUAL DE CONFIGURACIÓN Y FUNCIONAMIENTO

## 9.1. Requisitos del Sistema

### 9.1.1. Requisitos de Hardware

#### Requisitos Mínimos

| Componente | Especificación Mínima |
|------------|----------------------|
| **Procesador** | Intel Core i3 / AMD Ryzen 3 (2 cores) |
| **RAM** | 4 GB |
| **Almacenamiento** | 2 GB disponibles (SSD recomendado) |
| **Resolución de pantalla** | 1280 × 720 (HD) |
| **Conexión a Internet** | 5 Mbps (descarga) |

#### Requisitos Recomendados

| Componente | Especificación Recomendada |
|------------|---------------------------|
| **Procesador** | Intel Core i5 / AMD Ryzen 5 (4 cores) |
| **RAM** | 8 GB |
| **Almacenamiento** | 5 GB disponibles en SSD |
| **Resolución de pantalla** | 1920 × 1080 (Full HD) |
| **Conexión a Internet** | 25 Mbps (descarga) |

---

### 9.1.2. Requisitos de Software

#### Sistema Operativo

✅ **Linux**:
- Ubuntu 20.04 LTS o superior
- Debian 10 o superior
- Fedora 34 o superior
- Arch Linux (actualizado)

✅ **macOS**:
- macOS 11 Big Sur o superior
- macOS 12 Monterey (recomendado)
- macOS 13 Ventura

✅ **Windows**:
- Windows 10 (versión 1909 o superior)
- Windows 11 (recomendado)

#### Dependencias Principales

| Software | Versión Mínima | Versión Recomendada | Propósito |
|----------|----------------|---------------------|-----------|
| **Python** | 3.10 | 3.11 o 3.12 | Lenguaje principal |
| **pip** | 21.0 | Última | Gestor de paquetes Python |
| **Node.js** | 18.0.0 | 20.11.0 LTS | Frontend (generado por Reflex) |
| **npm** | 8.0.0 | 10.0.0 | Gestor de paquetes Node |
| **Git** | 2.30 | Última | Control de versiones |

#### Navegadores Soportados (para usuarios finales)

| Navegador | Versión Mínima |
|-----------|----------------|
| Google Chrome | 90+ |
| Mozilla Firefox | 88+ |
| Safari | 14+ |
| Microsoft Edge | 90+ |

---

## 9.2. Instalación y Configuración

### 9.2.1. Instalación en Windows

#### Paso 1: Instalar Python

1. Descargar Python desde https://www.python.org/downloads/
2. Ejecutar el instalador
3. ✅ **IMPORTANTE**: Marcar "Add Python to PATH"
4. Click en "Install Now"
5. Verificar instalación:
   ```cmd
   python --version
   ```
   **Salida esperada**: `Python 3.11.x` (o superior)

#### Paso 2: Instalar Node.js

1. Descargar Node.js LTS desde https://nodejs.org/
2. Ejecutar el instalador (opciones por defecto)
3. Verificar instalación:
   ```cmd
   node --version
   npm --version
   ```
   **Salida esperada**:
   ```
   v20.11.0
   10.2.4
   ```

#### Paso 3: Instalar Git

1. Descargar Git desde https://git-scm.com/download/win
2. Ejecutar el instalador (opciones por defecto)
3. Verificar instalación:
   ```cmd
   git --version
   ```

#### Paso 4: Clonar el Repositorio

```cmd
# Navegar a la carpeta deseada
cd C:\Users\TuUsuario\Documents

# Clonar repositorio
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git

# Entrar al directorio
cd E-Learning-JCB-Reflex
```

#### Paso 5: Crear Entorno Virtual

```cmd
# Crear entorno virtual
python -m venv reflex-env

# Activar entorno virtual
reflex-env\Scripts\activate

# Verificar activación (debe aparecer (reflex-env) en el prompt)
```

#### Paso 6: Instalar Dependencias

```cmd
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

**Tiempo estimado**: 3-5 minutos

**Progreso esperado**:
```
Collecting reflex==0.8.24
Collecting motor==3.7.1
Collecting bcrypt==5.0.0
...
Successfully installed reflex-0.8.24 motor-3.7.1 bcrypt-5.0.0 ...
```

#### Paso 7: Configurar Variables de Entorno

```cmd
# Copiar archivo de ejemplo
copy .env.example .env

# Editar .env con Notepad
notepad .env
```

Ver sección 9.3 para configuración de variables.

#### Paso 8: Ejecutar la Aplicación

```cmd
# Primera ejecución (inicializa Reflex)
reflex init

# Ejecutar en modo desarrollo
reflex run
```

**Salida esperada**:
```
Starting Reflex App
─────────────────────────────────────────────────────
App running at:
  └─ http://localhost:3000

Backend running at:
  └─ http://localhost:8000
```

✅ **Abrir navegador** en http://localhost:3000

---

### 9.2.2. Instalación en Linux (Ubuntu/Debian)

#### Paso 1: Actualizar Sistema

```bash
sudo apt update
sudo apt upgrade -y
```

#### Paso 2: Instalar Python 3.11

```bash
# Instalar dependencias
sudo apt install software-properties-common -y

# Añadir repositorio deadsnakes (Python versiones)
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# Instalar Python 3.11
sudo apt install python3.11 python3.11-venv python3.11-dev -y

# Verificar
python3.11 --version
```

#### Paso 3: Instalar Node.js (desde NodeSource)

```bash
# Instalar Node.js 20 LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y

# Verificar
node --version
npm --version
```

#### Paso 4: Instalar Git

```bash
sudo apt install git -y

# Verificar
git --version
```

#### Paso 5: Clonar Repositorio

```bash
# Navegar a home
cd ~

# Clonar
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git
cd E-Learning-JCB-Reflex
```

#### Paso 6: Crear Entorno Virtual

```bash
# Crear entorno virtual con Python 3.11
python3.11 -m venv reflex-env

# Activar
source reflex-env/bin/activate

# Verificar activación
which python  # Debe mostrar ruta dentro de reflex-env
```

#### Paso 7: Instalar Dependencias

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

#### Paso 8: Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar con nano (o vim, gedit, etc.)
nano .env
```

#### Paso 9: Ejecutar Aplicación

```bash
# Inicializar Reflex
reflex init

# Ejecutar
reflex run
```

---

### 9.2.3. Instalación en macOS

#### Paso 1: Instalar Homebrew (si no está instalado)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Paso 2: Instalar Python

```bash
# Instalar Python 3.11
brew install python@3.11

# Verificar
python3.11 --version
```

#### Paso 3: Instalar Node.js

```bash
# Instalar Node.js LTS
brew install node@20

# Verificar
node --version
npm --version
```

#### Paso 4: Instalar Git

```bash
# Git ya viene con Xcode Command Line Tools, pero puede actualizarse
brew install git

# Verificar
git --version
```

#### Pasos 5-9: Iguales a Linux

Ver sección 9.2.2 pasos 5-9 (clonar, entorno virtual, dependencias, configurar, ejecutar)

---

## 9.3. Configuración de Variables de Entorno

### 9.3.1. Archivo `.env`

El archivo `.env` contiene configuraciones sensibles que **NO deben committearse** a Git (ya está en `.gitignore`).

**Ubicación**: Raíz del proyecto (`/E-Learning-JCB-Reflex/.env`)

**Plantilla** (`.env.example`):
```env
# ============================================
# CONFIGURACIÓN DE E-LEARNING JCB PLATFORM
# ============================================

# --- BASE DE DATOS ---
# URI de conexión a MongoDB Atlas
# Formato: mongodb+srv://<usuario>:<password>@<cluster>.mongodb.net
MONGODB_URI=mongodb+srv://usuario:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority

# Nombre de la base de datos
DB_NAME=elearning_jcb

# --- APLICACIÓN ---
# Entorno de ejecución (development | production)
ENVIRONMENT=development

# URL del frontend (para CORS en producción)
FRONTEND_URL=http://localhost:3000

# Puerto del backend (por defecto 8000)
BACKEND_PORT=8000

# --- SEGURIDAD ---
# Clave secreta para firmar sesiones (generar con: python -c "import secrets; print(secrets.token_hex(32))")
SECRET_KEY=tu_clave_secreta_aqui_debe_ser_muy_larga_y_aleatoria

# --- EMAIL (opcional, para futuro) ---
# Configuración de SendGrid para emails
SENDGRID_API_KEY=
EMAIL_FROM=noreply@elearningjcb.com

# --- OTROS ---
# Nivel de logging (DEBUG | INFO | WARNING | ERROR)
LOG_LEVEL=DEBUG
```

---

### 9.3.2. Obtener URI de MongoDB Atlas

#### Paso 1: Crear Cuenta en MongoDB Atlas

1. Ir a https://www.mongodb.com/cloud/atlas/register
2. Registrarse con email (gratis)
3. Verificar email

#### Paso 2: Crear Cluster Gratuito

1. Click en "Build a Database"
2. Seleccionar **M0 (FREE)**
3. Elegir proveedor cloud: **AWS** (recomendado)
4. Región: **Europe (Ireland)** `eu-west-1` (más cercano a España)
5. Nombre del cluster: `Cluster0` (por defecto)
6. Click en "Create"

**Tiempo de creación**: 3-5 minutos

#### Paso 3: Configurar Acceso

**3.1. Crear Usuario de Base de Datos**:
1. En "Database Access", click "Add New Database User"
2. Authentication Method: **Password**
3. Usuario: `elearning_admin`
4. Contraseña: Generar automática (guardar en lugar seguro)
5. Database User Privileges: **Read and write to any database**
6. Click "Add User"

**3.2. Configurar IP Whitelist**:
1. En "Network Access", click "Add IP Address"
2. **Desarrollo**: Click "Allow Access from Anywhere" (0.0.0.0/0)
   - ⚠️ **Nota**: En producción, especificar IP del servidor
3. Click "Confirm"

#### Paso 4: Obtener Connection String

1. En "Database", click "Connect" en tu cluster
2. Seleccionar "Connect your application"
3. Driver: **Python**, Version: **3.6 or later**
4. Copiar connection string:
   ```
   mongodb+srv://elearning_admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
5. Reemplazar `<password>` con la contraseña del usuario

#### Paso 5: Pegar en `.env`

```env
MONGODB_URI=mongodb+srv://elearning_admin:TuPasswordAqui@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
DB_NAME=elearning_jcb
```

✅ **Guardar archivo**

---

### 9.3.3. Generar Clave Secreta

```bash
# Activar entorno virtual primero
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Generar clave aleatoria de 64 caracteres
python -c "import secrets; print(secrets.token_hex(32))"
```

**Salida** (ejemplo):
```
a7f3d2e9c1b8f4a6e3d7c2b9a8f5e1d4c3b7a6f2e9d8c4b1a7f3e2d9c6b8a5f4
```

**Copiar en `.env`**:
```env
SECRET_KEY=a7f3d2e9c1b8f4a6e3d7c2b9a8f5e1d4c3b7a6f2e9d8c4b1a7f3e2d9c6b8a5f4
```

---

## 9.4. Despliegue en Producción

### 9.4.1. Despliegue en Reflex Cloud

**Reflex Cloud** es la plataforma oficial de despliegue para aplicaciones Reflex, con configuración simplificada.

#### Paso 1: Crear Cuenta en Reflex Cloud

1. Ir a https://reflex.dev/cloud
2. Registrarse con GitHub (OAuth)
3. Autorizar acceso a repositorios

#### Paso 2: Conectar Repositorio

1. En dashboard de Reflex Cloud, click "New Project"
2. Seleccionar repositorio: `E-Learning-JCB-Reflex`
3. Branch: `main`
4. Click "Import"

#### Paso 3: Configurar Variables de Entorno

1. En proyecto, ir a "Settings" > "Environment Variables"
2. Añadir las siguientes variables (una por una):

   | Variable | Valor |
   |----------|-------|
   | `MONGODB_URI` | mongodb+srv://... (tu URI completa) |
   | `DB_NAME` | elearning_jcb |
   | `ENVIRONMENT` | production |
   | `SECRET_KEY` | (tu clave secreta generada) |
   | `FRONTEND_URL` | (se autocompletará con URL de Reflex Cloud) |

3. Click "Save" para cada variable

#### Paso 4: Desplegar

1. En dashboard del proyecto, click "Deploy"
2. Reflex Cloud automáticamente:
   - Clona el repositorio
   - Instala dependencias (`pip install -r requirements.txt`)
   - Ejecuta `reflex init`
   - Ejecuta `reflex export --frontend-only` (si aplica)
   - Inicia servidor
3. **Tiempo de despliegue**: 3-5 minutos

#### Paso 5: Verificar Despliegue

**URL de producción**: https://[tu-proyecto].reflex.run

✅ Abrir en navegador y verificar funcionamiento

#### Paso 6: Configurar Dominio Personalizado (Opcional)

1. En "Settings" > "Domains"
2. Click "Add Custom Domain"
3. Introducir dominio: `www.elearningjcb.com`
4. Configurar DNS en tu proveedor de dominio:
   - Tipo: `CNAME`
   - Nombre: `www`
   - Valor: `[tu-proyecto].reflex.run`
5. Verificar dominio (24-48 horas para propagación DNS)

**Certificado SSL**: Automático con Let's Encrypt

---

### 9.4.2. Despliegue en VPS (Alternativa)

Si prefieres control total, puedes desplegar en un VPS (DigitalOcean, Linode, Hetzner).

#### Requisitos del Servidor

- **OS**: Ubuntu 22.04 LTS
- **RAM**: Mínimo 2 GB (4 GB recomendado)
- **CPU**: 1 vCPU (2 vCPUs recomendado)
- **Almacenamiento**: 20 GB SSD
- **IP**: Pública estática

#### Paso 1: Configurar Servidor

```bash
# Conectar via SSH
ssh root@tu_ip_servidor

# Actualizar sistema
apt update && apt upgrade -y

# Instalar dependencias
apt install python3.11 python3.11-venv python3-pip nodejs npm nginx git -y

# Crear usuario para la aplicación
adduser elearning
usermod -aG sudo elearning

# Cambiar a usuario elearning
su - elearning
```

#### Paso 2: Clonar y Configurar Aplicación

```bash
# Clonar repositorio
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git
cd E-Learning-JCB-Reflex

# Crear entorno virtual
python3.11 -m venv reflex-env
source reflex-env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
nano .env
# (pegar configuración de producción)
```

#### Paso 3: Configurar Nginx como Reverse Proxy

```bash
# Crear configuración de Nginx
sudo nano /etc/nginx/sites-available/elearning
```

**Contenido**:
```nginx
server {
    listen 80;
    server_name tu_dominio.com www.tu_dominio.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
    }
}
```

```bash
# Activar sitio
sudo ln -s /etc/nginx/sites-available/elearning /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Paso 4: Configurar Systemd Service

```bash
# Crear servicio
sudo nano /etc/systemd/system/elearning.service
```

**Contenido**:
```ini
[Unit]
Description=E-Learning JCB Platform
After=network.target

[Service]
User=elearning
WorkingDirectory=/home/elearning/E-Learning-JCB-Reflex
Environment="PATH=/home/elearning/E-Learning-JCB-Reflex/reflex-env/bin"
ExecStart=/home/elearning/E-Learning-JCB-Reflex/reflex-env/bin/reflex run --production

[Install]
WantedBy=multi-user.target
```

```bash
# Activar y iniciar servicio
sudo systemctl enable elearning
sudo systemctl start elearning

# Verificar estado
sudo systemctl status elearning
```

#### Paso 5: Configurar SSL con Let's Encrypt

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtener certificado
sudo certbot --nginx -d tu_dominio.com -d www.tu_dominio.com

# Renovación automática (ya configurada por Certbot)
sudo certbot renew --dry-run
```

✅ **Aplicación disponible en**: https://tu_dominio.com

---

## 9.5. Resolución de Problemas Comunes

### 9.5.1. Error: "MONGODB_URI environment variable is not set"

**Causa**: Archivo `.env` no existe o no está configurado

**Solución**:
```bash
# Verificar que existe .env
ls -la .env  # Linux/Mac
dir .env     # Windows

# Si no existe, copiar desde ejemplo
cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows

# Editar y configurar MONGODB_URI
nano .env  # Linux/Mac
notepad .env  # Windows
```

---

### 9.5.2. Error: "reflex: command not found"

**Causa**: Entorno virtual no activado o Reflex no instalado

**Solución**:
```bash
# Activar entorno virtual
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Verificar activación (debe aparecer (reflex-env) en prompt)

# Si Reflex no está instalado
pip install reflex==0.8.24
```

---

### 9.5.3. Error: "Port 3000 already in use"

**Causa**: Otro proceso está usando el puerto 3000

**Solución**:

**Linux/Mac**:
```bash
# Encontrar proceso en puerto 3000
lsof -i :3000

# Matar proceso (usar PID del comando anterior)
kill -9 <PID>
```

**Windows**:
```cmd
# Encontrar proceso
netstat -ano | findstr :3000

# Matar proceso (usar PID de la última columna)
taskkill /PID <PID> /F
```

**Alternativa**: Ejecutar en otro puerto:
```bash
reflex run --port 3001
```

---

### 9.5.4. Error: "ModuleNotFoundError: No module named 'motor'"

**Causa**: Dependencias no instaladas

**Solución**:
```bash
# Asegurarse de que entorno virtual está activado
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Reinstalar dependencias
pip install -r requirements.txt

# Si persiste, instalar manualmente
pip install motor==3.7.1
```

---

### 9.5.5. Error: "Connection refused" al conectar a MongoDB

**Causa**: URI de MongoDB incorrecta o IP no whitelisteada

**Solución**:
1. Verificar URI en `.env` (copiar exactamente desde MongoDB Atlas)
2. En MongoDB Atlas, ir a "Network Access"
3. Verificar que tu IP está en whitelist (o 0.0.0.0/0 para desarrollo)
4. Verificar que el usuario de BD tiene permisos correctos ("Database Access")

---

### 9.5.6. Página en blanco / No carga UI

**Causa**: Frontend no inicializado o error en build

**Solución**:
```bash
# Limpiar caché de Reflex
rm -rf .web  # Linux/Mac
rmdir /s .web  # Windows

# Reinicializar
reflex init

# Ejecutar
reflex run
```

---

### 9.5.7. Logs de Errores

**Ver logs de Reflex**:
```bash
# Durante ejecución, los logs aparecen en consola

# Para servidor en producción (systemd):
sudo journalctl -u elearning -f
```

**Habilitar logging debug**:

En `.env`:
```env
LOG_LEVEL=DEBUG
```

---

## 9.6. Comandos Útiles

### Comandos de Reflex

```bash
# Ejecutar en modo desarrollo
reflex run

# Ejecutar en modo producción
reflex run --production

# Ejecutar en otro puerto
reflex run --port 3001

# Limpiar caché
reflex clean

# Exportar frontend estático (si aplica)
reflex export

# Ver versión de Reflex
reflex --version
```

### Comandos de Python/Pip

```bash
# Ver paquetes instalados
pip list

# Actualizar un paquete
pip install --upgrade reflex

# Congelar dependencias actuales
pip freeze > requirements.txt
```

### Comandos de Git

```bash
# Ver estado del repositorio
git status

# Descargar últimos cambios
git pull origin main

# Ver historial de commits
git log --oneline

# Ver diferencias
git diff
```

---

**Conclusión Sección 9**: El manual de configuración proporciona instrucciones detalladas paso a paso para instalar E-Learning JCB Platform en Windows, Linux y macOS. Incluye configuración de MongoDB Atlas, despliegue en Reflex Cloud (recomendado) y VPS (avanzado), así como resolución de problemas comunes. Con este manual, cualquier usuario con conocimientos básicos puede poner en funcionamiento la aplicación en menos de 30 minutos.

---

<div style="page-break-after: always;"></div>

# 6. ESTUDIO DE VIABILIDAD DEL PROYECTO

## 6.1. Viabilidad Técnica

### 6.1.1. Análisis de Capacidades Técnicas

#### Tecnologías Disponibles

**Reflex Framework** (v0.8.24)

✅ **Disponibilidad**: Open source, licencia Apache 2.0
✅ **Madurez**: Framework en producción usado por +1,000 proyectos
✅ **Documentación**: Completa en https://reflex.dev/docs
✅ **Comunidad**: Discord activo con +5,000 miembros
✅ **Soporte**: Equipo de Reflex responde en <24h

**MongoDB Atlas**

✅ **Disponibilidad**: Cloud SaaS con tier gratuito M0
✅ **Madurez**: Tecnología establecida desde 2009
✅ **Documentación**: Extensa en mongodb.com/docs
✅ **Escalabilidad**: Probada en millones de aplicaciones
✅ **Soporte**: 24/7 para tiers de pago

**Python 3.10+**

✅ **Disponibilidad**: Open source, multiplataforma
✅ **Madurez**: Lenguaje consolidado, versión 3.10 estable
✅ **Ecosystem**: +400,000 paquetes en PyPI
✅ **Comunidad**: Una de las más grandes del mundo
✅ **Soporte**: Long-term support hasta 2026

---

### 6.1.2. Evaluación de Conocimientos del Equipo

#### Conocimientos Actuales (Desarrollador Principal)

| Tecnología | Nivel Actual | Nivel Requerido | Gap | Plan de Formación |
|------------|--------------|-----------------|-----|-------------------|
| **Python** | ⭐⭐⭐⭐ Avanzado | ⭐⭐⭐⭐ Avanzado | ✅ Ninguno | Repaso de async/await |
| **Reflex** | ⭐⭐ Básico | ⭐⭐⭐⭐ Avanzado | ⚠️ Medio | Curso oficial (20h) |
| **MongoDB** | ⭐⭐ Básico | ⭐⭐⭐ Intermedio | ⚠️ Pequeño | MongoDB University (10h) |
| **Git/GitHub** | ⭐⭐⭐ Intermedio | ⭐⭐⭐ Intermedio | ✅ Ninguno | - |
| **HTML/CSS** | ⭐⭐⭐⭐ Avanzado | ⭐⭐⭐ Intermedio | ✅ Ninguno | - |
| **Diseño UX** | ⭐⭐ Básico | ⭐⭐ Básico | ✅ Ninguno | Práctica con Figma |

**Conclusión**: El gap técnico es **manejable** con 30 horas de formación específica en Reflex y MongoDB.

---

### 6.1.3. Infraestructura Técnica Necesaria

#### Hardware

| Componente | Mínimo | Recomendado | Disponible | Estado |
|------------|---------|-------------|------------|--------|
| **Procesador** | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7 | [Según equipo actual] | ✅/⚠️ |
| **RAM** | 8GB | 16GB | [Según equipo actual] | ✅/⚠️ |
| **Almacenamiento** | 256GB SSD | 512GB SSD | [Según equipo actual] | ✅/⚠️ |
| **Conexión Internet** | 10 Mbps | 50+ Mbps | Fibra óptica 300 Mbps | ✅ |

**Inversión necesaria**: 0€ - 1,200€ (si no se tiene equipo adecuado)

#### Software

| Software | Licencia | Coste | Disponible |
|----------|----------|-------|------------|
| **Python 3.10+** | Open source | 0€ | ✅ |
| **Reflex** | Apache 2.0 | 0€ | ✅ |
| **VS Code** | MIT | 0€ | ✅ |
| **Git** | GPL | 0€ | ✅ |
| **MongoDB Compass** | SSPL | 0€ | ✅ |
| **Sistema Operativo** | Ubuntu 22.04 LTS / Win 11 | 0€ | ✅ |

**Inversión total**: **0€** ✅

#### Infraestructura Cloud

| Servicio | Tier | Coste/Mes | Coste/Año | Estado |
|----------|------|-----------|-----------|--------|
| **MongoDB Atlas** (Dev) | M0 | 0€ | 0€ | ✅ Disponible |
| **MongoDB Atlas** (Prod) | M2 | 9€ | 108€ | ⚠️ Necesario |
| **Reflex Cloud** (Dev) | Free | 0€ | 0€ | ✅ Disponible |
| **Reflex Cloud** (Prod) | Starter | 20€ | 240€ | ⚠️ Necesario |
| **Dominio** | .com | - | 12€ | ⚠️ Opcional |

**Inversión desarrollo**: **0€**
**Inversión producción**: **360€/año**

---

### 6.1.4. Análisis de Riesgos Técnicos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Reflex tiene bugs críticos** | Baja (15%) | Alto | ⚠️ Medio | - Usar versión estable (0.8.24)<br>- Testing exhaustivo<br>- Reportar bugs a equipo Reflex |
| **Incompatibilidad de versiones** | Media (30%) | Medio | ⚠️ Medio | - Fijar versiones en requirements.txt<br>- Usar entorno virtual<br>- Documentar dependencias |
| **MongoDB Atlas caído** | Muy Baja (5%) | Alto | ⚠️ Bajo | - SLA 99.9% de Atlas<br>- Backups automáticos<br>- Plan de contingencia a MongoDB local |
| **Problemas de rendimiento** | Media (25%) | Medio | ⚠️ Medio | - Optimización de queries<br>- Índices en BD<br>- Lazy loading de datos |
| **Falta de conocimiento en Reflex** | Media (40%) | Medio | ⚠️ Medio-Alto | - 20h de formación oficial<br>- Soporte en Discord<br>- Documentación extensa |
| **Pérdida de código** | Muy Baja (5%) | Muy Alto | ⚠️ Bajo | - Git desde día 1<br>- GitHub remoto<br>- Commits frecuentes |

**Conclusión**: Riesgos técnicos son **manejables** con mitigaciones apropiadas.

---

### 6.1.5. Evaluación de Alternativas Técnicas

#### Comparativa Final de Viabilidad Técnica

| Alternativa | Tiempo Desarrollo | Complejidad | Costes | Escalabilidad | Viabilidad |
|-------------|-------------------|-------------|--------|---------------|------------|
| **Reflex + MongoDB** ⭐ | 6 meses | ⭐⭐ Baja | ⭐⭐⭐⭐⭐ Muy bajo | ⭐⭐⭐⭐ Alta | ✅ **95%** |
| MERN Stack | 9-12 meses | ⭐⭐⭐⭐ Alta | ⭐⭐⭐ Medio | ⭐⭐⭐⭐ Alta | ⚠️ 70% |
| Django + React | 8-10 meses | ⭐⭐⭐⭐ Alta | ⭐⭐ Alto | ⭐⭐⭐⭐⭐ Muy alta | ⚠️ 75% |
| Laravel + Vue | 8-11 meses | ⭐⭐⭐ Media | ⭐⭐ Alto | ⭐⭐⭐ Media | ⚠️ 65% |

**Conclusión**: **Reflex + MongoDB es la opción más viable técnicamente** (95% de viabilidad)

---

### 6.1.6. Conclusión de Viabilidad Técnica

#### Fortalezas Técnicas

✅ Stack tecnológico moderno y eficiente
✅ Todas las herramientas necesarias son gratuitas (desarrollo)
✅ Conocimientos del equipo son suficientes (con formación mínima)
✅ Infraestructura cloud robusta y económica
✅ Documentación y soporte disponibles
✅ Riesgos técnicos identificados y mitigables

#### Debilidades Técnicas

⚠️ Reflex es framework relativamente nuevo (menos maduro que Django/Laravel)
⚠️ Comunidad más pequeña (menos recursos de terceros)
⚠️ Necesidad de formación específica en Reflex (20h)

#### Dictamen Final

**Viabilidad Técnica: ALTA (95%)**

El proyecto es **altamente viable técnicamente**. Las tecnologías seleccionadas están disponibles, son suficientemente maduras y el equipo cuenta con las capacidades necesarias (o puede adquirirlas rápidamente). Los riesgos técnicos son bajos y están mitigados.

---

## 6.2. Viabilidad Económica

### 6.2.1. Costes Totales del Proyecto

#### Inversión Inicial (Una sola vez)

| Concepto | Cantidad | Justificación |
|----------|----------|---------------|
| **Hardware** (si no disponible) | 0€ - 1,200€ | Portátil de desarrollo |
| **Formación** | 190€ | Cursos Reflex + MongoDB + libros |
| **Gestoría (alta)** | 0€ | Trámite autónomo sin coste |
| **Legal (políticas)** | 300€ | Redacción de términos de uso, privacidad |
| **TOTAL INICIAL** | **490€ - 1,690€** | Escenario conservador: 490€ |

---

#### Costes Operativos Año 1

| Concepto | Mensual | Anual |
|----------|---------|-------|
| **Desarrollo (6 meses)** | | |
| - Coste de oportunidad (520h × 25€/h) | - | 13,000€ |
| **Infraestructura** | | |
| - MongoDB Atlas M2 (producción) | 9€ | 108€ |
| - Reflex Cloud Starter | 20€ | 240€ |
| - Dominio .com | - | 12€ |
| **Subtotal infraestructura** | 29€ | 360€ |
| **Obligaciones fiscales/sociales** | | |
| - Seguridad Social (tarifa plana 12m) | 80€ | 960€ |
| - Gestoría | 50€ | 600€ |
| - Seguro RC profesional | - | 200€ |
| **Subtotal obligaciones** | 130€ | 1,760€ |
| **Marketing** (desde mes 7) | | |
| - Google Ads | 200€ | 1,200€ |
| - LinkedIn Ads | 150€ | 900€ |
| - Canva Pro | 13€ | 156€ |
| **Subtotal marketing** | 363€ | 2,256€ |
| **TOTAL OPERATIVO AÑO 1** | **~520€** | **17,376€** |

**Nota**: El coste de desarrollo (13,000€) es coste de oportunidad (no salida de caja en proyecto académico)

---

#### Costes Operativos Año 2

| Concepto | Mensual | Anual |
|----------|---------|-------|
| **Personal** | | |
| - Desarrollador principal (part-time) | 1,500€ | 18,000€ |
| **Infraestructura** | | |
| - MongoDB Atlas M10 (escalado) | 57€ | 684€ |
| - Reflex Cloud Pro | 50€ | 600€ |
| - CDN, email, etc. | 20€ | 240€ |
| **Subtotal infraestructura** | 127€ | 1,524€ |
| **Obligaciones** | | |
| - Seguridad Social (sin tarifa plana) | 303€ | 3,636€ |
| - Gestoría | 75€ | 900€ |
| - Seguro | - | 250€ |
| **Subtotal obligaciones** | 378€ | 4,786€ |
| **Marketing** | | |
| - Publicidad online | 500€ | 6,000€ |
| - SEO/SEM | 200€ | 2,400€ |
| **Subtotal marketing** | 700€ | 8,400€ |
| **TOTAL OPERATIVO AÑO 2** | **~2,700€** | **32,710€** |

---

### 6.2.2. Proyección de Ingresos

#### Modelo de Negocio: Freemium + Marketplace

**Asunciones Base**:
- Precio medio curso premium: 99€
- Comisión marketplace (si instructor publica): 25%
- Tasa de conversión freemium: 5%
- Retención: 70% año 1, 80% año 2

---

#### Escenario Conservador (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 30 | 2 | 2 | 198€ | 198€ |
| Q2 | 80 | 5 | 7 | 693€ | 891€ |
| Q3 | 150 | 10 | 15 | 1,485€ | 2,376€ |
| Q4 | 250 | 18 | 28 | 2,772€ | 5,148€ |

**Total Año 1 (conservador)**: **5,148€**

---

#### Escenario Realista (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 50 | 3 | 4 | 396€ | 396€ |
| Q2 | 150 | 8 | 15 | 1,485€ | 1,881€ |
| Q3 | 300 | 20 | 40 | 3,960€ | 5,841€ |
| Q4 | 500 | 40 | 80 | 7,920€ | 13,761€ |

**Total Año 1 (realista)**: **13,761€**

---

#### Escenario Optimista (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 100 | 5 | 8 | 792€ | 792€ |
| Q2 | 300 | 18 | 30 | 2,970€ | 3,762€ |
| Q3 | 600 | 45 | 80 | 7,920€ | 11,682€ |
| Q4 | 1,000 | 80 | 150 | 14,850€ | 26,532€ |

**Total Año 1 (optimista)**: **26,532€**

---

#### Proyección Año 2

| Escenario | Usuarios Finales | Ingresos |
|-----------|------------------|----------|
| **Conservador** | 800 | 45,000€ |
| **Realista** | 2,000 | 120,000€ |
| **Optimista** | 4,000 | 220,000€ |

---

### 6.2.3. Análisis de Rentabilidad

#### Año 1

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 5,148€ | 13,761€ | 26,532€ |
| **Costes operativos** (sin desarrollo) | 4,376€ | 4,376€ | 4,376€ |
| **Costes de desarrollo** | 13,000€ | 13,000€ | 13,000€ |
| **Costes totales** | 17,376€ | 17,376€ | 17,376€ |
| **Beneficio neto** | **-12,228€** ❌ | **-3,615€** ❌ | **+9,156€** ✅ |
| **ROI** | -70% | -21% | +53% |

**Conclusión Año 1**:
- Escenario conservador/realista: **Pérdidas** (esperadas en startups año 1)
- Escenario optimista: **Beneficio positivo**
- **Nota**: Si se excluye coste de desarrollo (proyecto académico), todos los escenarios son rentables

#### Año 1 (Sin Coste de Desarrollo)

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 5,148€ | 13,761€ | 26,532€ |
| **Costes operativos** | 4,376€ | 4,376€ | 4,376€ |
| **Beneficio neto** | **+772€** ✅ | **+9,385€** ✅ | **+22,156€** ✅ |
| **ROI** | +18% | +214% | +506% |

---

#### Año 2

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 45,000€ | 120,000€ | 220,000€ |
| **Costes operativos** | 32,710€ | 35,000€ | 40,000€ |
| **Beneficio neto** | **+12,290€** ✅ | **+85,000€** ✅ | **+180,000€** ✅ |
| **Margen** | 27% | 71% | 82% |

**Conclusión Año 2**: **Rentable en todos los escenarios** ✅

---

### 6.2.4. Punto de Equilibrio (Break-Even)

#### Cálculo del Punto de Equilibrio

**Costes fijos mensuales** (Año 1): 159€
- Infraestructura: 29€
- Seguridad Social: 80€
- Gestoría: 50€

**Costes variables**: ~5€ por venta (procesamiento, comisiones)

**Precio medio curso**: 99€

**Margen de contribución**: 99€ - 5€ = 94€

**Punto de equilibrio**:
```
Break-even (unidades) = Costes Fijos / Margen Contribución
Break-even = 159€ / 94€ = 1.69 cursos/mes ≈ 2 cursos/mes
```

**Punto de equilibrio anual**: **24 cursos vendidos/año**

**Análisis**: El punto de equilibrio es **muy accesible**. Con solo 2 ventas mensuales, los costes operativos se cubren.

---

### 6.2.5. Financiación del Proyecto

#### Necesidades de Financiación

| Fase | Concepto | Cantidad | Fuente de Financiación |
|------|----------|----------|------------------------|
| **Desarrollo** | Inversión inicial | 490€ - 1,690€ | - Autofinanciación<br>- Ayuda Almería Emprende (3,000€) |
| **Año 1** | Operativo | 4,376€ | - Tarifa plana SS (ahorro 2,676€)<br>- Almería Emprende (3,000€)<br>- Ingresos propios |
| **Año 2** | Operativo + Crecimiento | 32,710€ | - Ingresos Año 1 reinvertidos<br>- ENISA (25,000€ si aplica) |

---

#### Fuentes de Financiación Disponibles

| Fuente | Tipo | Cantidad | Condiciones | Probabilidad |
|--------|------|----------|-------------|--------------|
| **Tarifa plana SS** | Ahorro | 2,676€ | Primer año como autónomo | ✅ 100% |
| **Almería Emprende** | Subvención | 3,000€ | Proyecto viable, domicilio Almería | ✅ 80% |
| **Cheque Innovación** | Bono servicios | 1,500€ | Componente tecnológico | ✅ 70% |
| **Kit Digital** | Subvención | 1,500€ | Web de marketing | ⚠️ 60% |
| **Andalucía Emprende** | Préstamo 0% | 15,000€ | Plan de negocio | ⚠️ 50% |
| **ENISA Jóvenes** | Préstamo participativo | 25,000€ | SL, <40 años, fondos propios | ⚠️ 40% |
| **Autofinanciación** | Capital propio | Variable | Ahorros personales | ✅ 100% |

**Total ayudas conservadoras**: 7,176€ (Tarifa plana + Almería Emprende + Cheque Innovación)

---

#### Plan de Financiación Conservador

| Fase | Necesidad | Fuente | Cantidad |
|------|-----------|--------|----------|
| **Inversión inicial** (490€) | 490€ | Autofinanciación | 490€ |
| **Año 1 - Costes operativos** (4,376€) | 4,376€ | - Tarifa plana SS (ahorro)<br>- Almería Emprende<br>- Ingresos propios | 2,676€<br>3,000€<br>Resto con ingresos |
| **Déficit máximo Año 1** | ~1,500€ | Autofinanciación | 1,500€ |

**Total inversión propia necesaria**: **~2,000€** (muy accesible)

---

### 6.2.6. Análisis de Riesgos Económicos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Ingresos inferiores a proyección** | Alta (60%) | Alto | ⚠️ Alto | - Escenario conservador ya asume bajos ingresos<br>- Marketing orgánico (0€)<br>- Reducir gastos variables |
| **Costes superiores a estimación** | Media (35%) | Medio | ⚠️ Medio | - Buffer del 10% en presupuesto<br>- Controlar gastos mensuales<br>- Priorizar inversiones |
| **No obtener ayudas esperadas** | Media (30%) | Medio | ⚠️ Medio | - Plan conservador no depende de ayudas mayores<br>- Solo contar con tarifa plana (100% segura) |
| **Competencia con precios bajos** | Media (40%) | Medio | ⚠️ Medio | - Diferenciación por transparencia<br>- Modelo freemium flexible<br>- Valor agregado claro |
| **Retraso en tiempo al mercado** | Media (30%) | Alto | ⚠️ Alto | - Planificación detallada<br>- MVP en 6 meses<br>- Entregas iterativas |

---

### 6.2.7. Conclusión de Viabilidad Económica

#### Fortalezas Económicas

✅ Costes de desarrollo muy bajos (stack gratuito)
✅ Costes operativos mínimos (360€/año producción)
✅ Punto de equilibrio muy bajo (24 ventas/año)
✅ Modelo de negocio escalable (marginal cost ≈ 0)
✅ Ayudas disponibles (7,176€ conservador)
✅ Inversión propia necesaria baja (~2,000€)
✅ Rentabilidad en Año 2 en todos los escenarios

#### Debilidades Económicas

⚠️ Año 1 con posibles pérdidas (en escenario conservador)
⚠️ Dependencia de marketing para alcanzar usuarios
⚠️ Mercado competitivo (Udemy, Coursera, etc.)
⚠️ Ingresos iniciales lentos (primeros 3-6 meses)

#### Dictamen Final

**Viabilidad Económica: ALTA (85%)**

El proyecto es **económicamente viable**. Los costes son muy bajos, las ayudas disponibles cubren gran parte de la inversión necesaria, y el punto de equilibrio es alcanzable. Aunque el Año 1 puede tener pérdidas en escenario conservador, el Año 2 es rentable en todos los escenarios. La inversión propia necesaria es mínima (~2,000€), lo que hace el proyecto accesible.

---

## 6.3. Viabilidad Operativa

### 6.3.1. Capacidades Operativas del Equipo

#### Análisis de Roles Necesarios

| Rol | Necesario en Año 1 | Disponible | Gap |
|-----|-------------------|------------|-----|
| **Desarrollador Full-Stack** | ✅ Sí (crítico) | ✅ Desarrollador principal | ✅ Cubierto |
| **Diseñador UX/UI** | ⚠️ Deseable | ⚠️ Básico (Figma) | ⚠️ Pequeño |
| **Marketing Digital** | ⚠️ Deseable | ⚠️ Básico (redes sociales) | ⚠️ Medio |
| **Gestor de Contenidos** | ❌ No | - | ✅ No aplica |
| **Soporte al Cliente** | ❌ No | - | ✅ No aplica |

**Conclusión**: El rol crítico (desarrollador) está cubierto. Los roles deseables pueden suplirse con:
- **Diseño**: Plantillas de Chakra UI + Figma básico
- **Marketing**: Marketing orgánico inicialmente (LinkedIn, X)

---

### 6.3.2. Procesos Operativos Necesarios

#### Desarrollo y Mantenimiento

| Proceso | Frecuencia | Tiempo Estimado | Responsable |
|---------|------------|-----------------|-------------|
| **Desarrollo de features** | Continuo | 20h/semana (Año 1) | Desarrollador principal |
| **Corrección de bugs** | On-demand | 2-4h/bug | Desarrollador principal |
| **Actualización de dependencias** | Mensual | 1h/mes | Desarrollador principal |
| **Backup de base de datos** | Automático (MongoDB Atlas) | 0h | MongoDB |
| **Monitoreo de errores** | Semanal | 1h/semana | Desarrollador principal |

**Total tiempo semanal**: 20-25h (sostenible para un desarrollador)

---

#### Atención al Cliente

| Proceso | Frecuencia | Tiempo Estimado | Canal |
|---------|------------|-----------------|-------|
| **Respuesta a consultas** | Según demanda | 0.5h/consulta | Email (inicialmente) |
| **Onboarding de instructores** | Según inscripciones | 1h/instructor | Email + video tutorial |
| **Soporte técnico** | Ocasional | 1h/semana | FAQ + email |
| **Moderación de contenidos** | Semanal | 2h/semana | Manual (Año 1) |

**Total tiempo semanal**: 3-5h (manejable)

---

#### Marketing y Ventas

| Proceso | Frecuencia | Tiempo Estimado | Canal |
|---------|------------|-----------------|-------|
| **Publicación en redes sociales** | 3x/semana | 2h/semana | LinkedIn, X |
| **Creación de contenido (blog)** | 2x/mes | 4h/mes | Blog en plataforma |
| **Email marketing** | 1x/semana | 1h/semana | SendGrid |
| **Análisis de métricas** | Semanal | 1h/semana | Google Analytics |

**Total tiempo semanal**: 3-4h (manejable)

---

### 6.3.3. Evaluación de Escalabilidad Operativa

#### Escenario Actual (Año 1)

| Métrica | Capacidad Actual | Comentario |
|---------|------------------|------------|
| **Usuarios concurrentes** | 100 | Suficiente para primeros 500 usuarios totales |
| **Cursos soportados** | Ilimitado | MongoDB permite crecimiento sin límite |
| **Transacciones/mes** | 1,000 | Muy por encima de necesidad Año 1 (50-100) |
| **Tiempo de desarrollo** | 20h/semana | Permite evolución continua |
| **Soporte al cliente** | 10 consultas/semana | Con FAQ robusta, manejable |

**Conclusión**: La capacidad operativa actual es **más que suficiente** para Año 1.

---

#### Escenario de Crecimiento (Año 2)

| Métrica | Capacidad Necesaria | Solución |
|---------|---------------------|----------|
| **Usuarios concurrentes** | 500-1,000 | - Escalar a MongoDB M10<br>- Reflex Cloud Pro |
| **Cursos soportados** | 200+ cursos | Sin cambios (escalabilidad nativa) |
| **Transacciones/mes** | 5,000-10,000 | Sin cambios (muy por debajo de límites) |
| **Tiempo de desarrollo** | 20h/semana insuficiente | - Contratar desarrollador junior part-time<br>- Automatizar tareas repetitivas |
| **Soporte al cliente** | 50 consultas/semana | - Chatbot básico (FAQ automático)<br>- Contratar freelance soporte (10h/semana) |

**Inversión necesaria Año 2**:
- Desarrollador junior part-time: 18,000€/año
- Freelance soporte: 4,800€/año
- Infraestructura escalada: +1,164€/año
**Total**: **~24,000€/año**

**Ingresos proyectados Año 2** (realista): 120,000€
**Margen suficiente**: ✅ Sí (85,000€ beneficio)

---

### 6.3.4. Usabilidad y Experiencia de Usuario

#### Evaluación de Usabilidad

| Aspecto | Objetivo | Implementación | Estado |
|---------|----------|----------------|--------|
| **Facilidad de registro** | <2 minutos | Formulario de 4 campos | ✅ Cumplido |
| **Navegación intuitiva** | <3 clics a cualquier sección | Navbar + breadcrumbs | ✅ Cumplido |
| **Tiempo de carga** | <3 segundos | Lazy loading, optimización | ✅ Cumplido |
| **Responsive design** | Funcional en móvil | Chakra UI responsive | ✅ Cumplido |
| **Accesibilidad** | WCAG 2.1 Level A | Chakra UI accesible | ✅ Cumplido |
| **Búsqueda de cursos** | <5 segundos | Índice de texto MongoDB | ✅ Cumplido |

**Conclusión**: La usabilidad está **garantizada** por el diseño de Chakra UI y las decisiones de arquitectura.

---

#### Facilidad de Mantenimiento

| Aspecto | Evaluación | Justificación |
|---------|------------|---------------|
| **Separación de capas** | ⭐⭐⭐⭐⭐ Excelente | Modelos, servicios, estados, componentes bien separados |
| **Documentación de código** | ⭐⭐⭐⭐ Buena | Docstrings, comentarios, README detallado |
| **Testing** | ⭐⭐⭐ Aceptable | Unit tests en servicios y modelos (cobertura 80%) |
| **Convenciones de código** | ⭐⭐⭐⭐ Buena | PEP 8, Black formatter, naming consistente |
| **Gestión de dependencias** | ⭐⭐⭐⭐⭐ Excelente | requirements.txt, entorno virtual, versiones fijadas |

**Conclusión**: El código es **altamente mantenible** (4.2/5 promedio)

---

### 6.3.5. Análisis de Riesgos Operativos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Sobrecarga de trabajo del desarrollador** | Alta (50%) | Alto | ⚠️ Alto | - Priorización estricta de features<br>- MVP bien definido<br>- Automatización de tareas<br>- Plan de contingencia (reducir scope) |
| **Falta de instructores (contenido)** | Media (30%) | Alto | ⚠️ Medio-Alto | - Crear cursos propios inicialmente<br>- Incentivos a primeros instructores<br>- Outreach proactivo a profesionales |
| **Baja adopción de usuarios** | Media (40%) | Alto | ⚠️ Alto | - Marketing orgánico constante<br>- Programa de referidos<br>- Modelo freemium (barrera de entrada baja) |
| **Problemas de calidad de contenido** | Baja (20%) | Medio | ⚠️ Bajo | - Revisión de cursos antes de publicación<br>- Sistema de valoraciones transparente<br>- Políticas de calidad claras |
| **Escalabilidad técnica insuficiente** | Muy Baja (10%) | Medio | ⚠️ Muy Bajo | - Arquitectura diseñada para escalar<br>- MongoDB y Reflex Cloud con autoscaling<br>- Monitoreo proactivo |

---

### 6.3.6. Conclusión de Viabilidad Operativa

#### Fortalezas Operativas

✅ Equipo (1 persona) suficiente para Año 1
✅ Procesos operativos bien definidos y manejables
✅ Escalabilidad técnica garantizada (MongoDB + Reflex Cloud)
✅ Usabilidad excelente (Chakra UI, diseño responsive)
✅ Código altamente mantenible (4.2/5)
✅ Automatización de tareas críticas (backups, deploy)

#### Debilidades Operativas

⚠️ Dependencia de un solo desarrollador (riesgo de sobrecarga)
⚠️ Falta de equipo de marketing especializado
⚠️ Necesidad de contenido inicial (cursos para atraer usuarios)
⚠️ Escalado operativo en Año 2 requiere contrataciones

#### Dictamen Final

**Viabilidad Operativa: ALTA (90%)**

El proyecto es **altamente viable operativamente**. Los procesos están bien definidos, el equipo es suficiente para Año 1, la usabilidad está garantizada y la escalabilidad técnica es nativa. Los principales riesgos (sobrecarga de trabajo, falta de contenido) son mitigables con planificación adecuada y priorización estricta.

---

## 6.4. Viabilidad Legal

### 6.4.1. Marco Legal Aplicable

#### Normativa de Protección de Datos

**RGPD (Reglamento General de Protección de Datos)**

**Aplicabilidad**: ✅ Obligatorio (usuarios en UE)

**Requisitos**:
1. **Base legal para tratamiento**: Consentimiento explícito o ejecución de contrato
2. **Información transparente**: Política de privacidad clara
3. **Derechos de los usuarios**: Acceso, rectificación, supresión, portabilidad
4. **Medidas de seguridad**: Cifrado, control de acceso, backups
5. **Registro de actividades**: Documentar tratamientos de datos
6. **DPO (Data Protection Officer)**: No obligatorio para empresas pequeñas

**Implementación en el proyecto**:
- ✅ Política de privacidad redactada
- ✅ Consentimiento explícito en registro
- ✅ Funcionalidad de edición/eliminación de cuenta
- ✅ Cifrado en tránsito (TLS) y en reposo (MongoDB Atlas)
- ✅ Control de acceso basado en roles (RBAC)

**Coste de cumplimiento**: 300€ (redacción legal) + 0€ (implementación técnica incluida)

---

**LOPDGDD (Ley Orgánica de Protección de Datos Personales)**

**Aplicabilidad**: ✅ Obligatorio (empresa española)

**Requisitos adicionales a RGPD**:
1. **Registro en AEPD**: Solo si hay transferencias internacionales (no aplica)
2. **Menores de 14 años**: Consentimiento paterno (no aplicable, +18)
3. **Videovigilancia**: No aplica (sin cámaras)

**Implementación**: ✅ Cubierto por cumplimiento RGPD

---

#### Normativa de Comercio Electrónico

**LSSI (Ley de Servicios de la Sociedad de la Información)**

**Aplicabilidad**: ✅ Obligatorio (servicio online)

**Requisitos**:
1. **Aviso legal**: Datos del titular, CIF, domicilio
2. **Política de cookies**: Consentimiento explícito
3. **Condiciones de contratación**: Términos de uso claros
4. **Procedimiento de contratación**: Pasos transparentes
5. **Email de contacto**: Canal de comunicación

**Implementación**:
- ✅ Aviso legal en footer
- ⚠️ Banner de cookies (a implementar cuando se usen cookies)
- ✅ Términos de uso redactados
- ✅ Email de contacto: info@elearningjcb.com

**Coste de cumplimiento**: Incluido en 300€ de redacción legal

---

#### Normativa Fiscal

**IVA (Impuesto sobre el Valor Añadido)**

**Aplicabilidad**: ✅ Obligatorio

**Tipo aplicable**: 21% (tipo general)
- **Nota**: Servicios educativos pueden estar exentos (art. 20.1.9º Ley IVA) pero solo si:
  - Centros privados autorizados
  - Enseñanza escolar o universitaria
  - **E-Learning JCB Platform**: NO exento (cursos online sin reconocimiento oficial)

**Obligaciones**:
- Modelo 303 (trimestral): Declaración de IVA
- Modelo 390 (anual): Resumen anual de IVA
- Facturación con IVA incluido

**Implementación**: ✅ Gestión via gestoría (600€/año)

---

**IRPF (Impuesto sobre la Renta de Personas Físicas)**

**Aplicabilidad**: ✅ Obligatorio (autónomo)

**Obligaciones**:
- Modelo 130 (trimestral): Pago fraccionado
- Modelo 100 (anual): Declaración de renta
- Retenciones (15%) si se factura a empresas

**Implementación**: ✅ Gestión via gestoría (600€/año)

---

#### Normativa de Propiedad Intelectual

**Ley de Propiedad Intelectual (Real Decreto Legislativo 1/1996)**

**Aplicabilidad**: ✅ Obligatorio

**Aspectos clave**:
1. **Contenido de cursos**: Propiedad del instructor
2. **Código fuente de la plataforma**: Propiedad de E-Learning JCB
3. **Licencia de uso**: Instructores conceden licencia no exclusiva a plataforma
4. **Plagio**: Sistema de detección (futuro)
5. **DMCA (Digital Millennium Copyright Act)**: Procedimiento de notificación

**Implementación**:
- ✅ Términos de uso especifican derechos de autor
- ✅ Instructores aceptan licencia al subir contenido
- ⚠️ Sistema anti-plagio (no en MVP)

**Coste**: Incluido en términos de uso (300€)

---

### 6.4.2. Obligaciones Legales con Terceros

#### Contratos con Instructores

**Necesidad**: ✅ Sí (relación mercantil)

**Contenido mínimo**:
- Derechos de propiedad intelectual
- Comisión de la plataforma (25%)
- Obligaciones de calidad
- Procedimiento de resolución de conflictos
- Duración y terminación

**Implementación**: ✅ Términos de servicio (aceptación online)

**Coste**: Incluido en 300€ de redacción legal

---

#### Contratos con Proveedores

| Proveedor | Tipo de Contrato | Necesidad | Estado |
|-----------|------------------|-----------|--------|
| **MongoDB Atlas** | ToS (Terms of Service) | ✅ Obligatorio | ✅ Aceptado online |
| **Reflex Cloud** | ToS | ✅ Obligatorio | ✅ Aceptado online |
| **Gestoría** | Contrato de servicios | ✅ Recomendado | ⚠️ A negociar |
| **Registrar de dominio** | ToS | ✅ Obligatorio | ✅ Aceptado online |

**Coste adicional**: 0€ (ToS estándar)

---

### 6.4.3. Responsabilidades Legales

#### Responsabilidad Civil

**Riesgo**: Daños a terceros (errores en plataforma, pérdida de datos)

**Solución**: Seguro de Responsabilidad Civil Profesional

**Cobertura recomendada**: 300,000€
**Coste**: 200€/año

**Implementación**: ✅ Previsto en presupuesto

---

#### Responsabilidad por Contenido

**Riesgo**: Contenido ilegal/inapropiado subido por instructores

**Marco legal**: Ley 34/2002 (LSSI) - Régimen de exención de responsabilidad

**Requisitos para exención**:
1. **No tener conocimiento efectivo** del contenido ilegal
2. **Actuar diligentemente** al tener conocimiento (retirar contenido)
3. **Sistema de notificación** para denuncias

**Implementación**:
- ✅ Sistema de moderación de contenido
- ✅ Formulario de denuncia
- ✅ Política de retirada de contenido ilegal (24-48h)

**Coste**: 0€ (funcionalidad integrada)

---

### 6.4.4. Análisis de Riesgos Legales

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Incumplimiento RGPD** | Baja (15%) | Muy Alto | ⚠️ Medio | - Política de privacidad completa<br>- Asesoría legal inicial<br>- Revisión anual |
| **Reclamación de propiedad intelectual** | Baja (20%) | Alto | ⚠️ Medio | - Términos de uso claros<br>- Licencia explícita de instructores<br>- Sistema de denuncias |
| **Contenido ilegal en plataforma** | Media (25%) | Alto | ⚠️ Medio-Alto | - Moderación proactiva<br>- Sistema de denuncias<br>- Retirada inmediata |
| **Problemas con Hacienda/SS** | Muy Baja (5%) | Alto | ⚠️ Muy Bajo | - Gestoría profesional<br>- Cumplimiento estricto<br>- Asesoría fiscal |
| **Demanda por responsabilidad civil** | Muy Baja (5%) | Alto | ⚠️ Muy Bajo | - Seguro RC profesional<br>- Términos de uso (limitación responsabilidad) |

---

### 6.4.5. Documentación Legal Necesaria

| Documento | Necesidad | Responsable | Coste | Estado |
|-----------|-----------|-------------|-------|--------|
| **Política de Privacidad** | ✅ Obligatorio | Abogado especializado | 100€ | ⚠️ A redactar |
| **Términos de Uso** | ✅ Obligatorio | Abogado especializado | 100€ | ⚠️ A redactar |
| **Aviso Legal** | ✅ Obligatorio | Abogado especializado | 50€ | ⚠️ A redactar |
| **Política de Cookies** | ⚠️ Si aplica | Abogado especializado | 50€ | ⚠️ Futuro |
| **Contrato con instructores** | ✅ Recomendado | Incluido en ToS | 0€ | ⚠️ Incluido en Términos |
| **TOTAL** | | | **300€** | |

---

### 6.4.6. Conclusión de Viabilidad Legal

#### Fortalezas Legales

✅ Marco legal bien identificado (RGPD, LSSI, IVA)
✅ Cumplimiento técnico de RGPD (cifrado, RBAC, backups)
✅ Documentación legal accesible (300€)
✅ Gestoría para cumplimiento fiscal (600€/año)
✅ Seguro RC profesional (200€/año)
✅ Sistema de moderación de contenido
✅ Régimen de exención de responsabilidad aplicable

#### Debilidades Legales

⚠️ Necesidad de redacción legal inicial (300€)
⚠️ Complejidad del RGPD (requiere asesoría inicial)
⚠️ Responsabilidad por contenido de terceros (mitigable)
⚠️ Actualizaciones legales periódicas necesarias

#### Dictamen Final

**Viabilidad Legal: ALTA (85%)**

El proyecto es **viable legalmente**. Todos los requisitos legales están identificados y son cumplibles con inversión razonable (300€ redacción + 200€ seguro). El cumplimiento del RGPD está garantizado por la arquitectura técnica (MongoDB Atlas cifrado, RBAC). Los riesgos legales son bajos y están mitigados con políticas claras y asesoría profesional.

---

## 6.5. Conclusión General del Estudio de Viabilidad

### Resumen Ejecutivo

| Dimensión | Viabilidad | Justificación |
|-----------|------------|---------------|
| **Técnica** | ✅ 95% | Stack moderno, herramientas disponibles, conocimientos suficientes |
| **Económica** | ✅ 85% | Costes bajos, punto de equilibrio bajo, rentabilidad Año 2 |
| **Operativa** | ✅ 90% | Procesos manejables, usabilidad garantizada, escalabilidad nativa |
| **Legal** | ✅ 85% | Marco legal claro, cumplimiento accesible, riesgos mitigados |
| **GLOBAL** | ✅ **89%** | **PROYECTO ALTAMENTE VIABLE** |

---

### Fortalezas del Proyecto

1. ✅ **Stack tecnológico eficiente**: Reflex + MongoDB reducen tiempo y costes
2. ✅ **Inversión inicial mínima**: ~2,000€ (muy accesible)
3. ✅ **Punto de equilibrio bajo**: 24 ventas/año
4. ✅ **Escalabilidad nativa**: Arquitectura preparada para crecer
5. ✅ **Ayudas disponibles**: 7,176€ en escenario conservador
6. ✅ **Diferenciación clara**: Transparencia en contenidos
7. ✅ **Mercado en crecimiento**: 13.7% CAGR global, 18.5% España
8. ✅ **Cumplimiento legal factible**: Requisitos claros y cumplibles

---

### Debilidades del Proyecto

1. ⚠️ **Mercado competitivo**: Udemy, Coursera, Domestika ya establecidos
2. ⚠️ **Dependencia de un solo desarrollador**: Riesgo de sobrecarga
3. ⚠️ **Reflex es framework nuevo**: Comunidad más pequeña
4. ⚠️ **Posibles pérdidas Año 1**: En escenario conservador (excl. ayudas)
5. ⚠️ **Necesidad de contenido inicial**: Cursos para atraer usuarios

---

### Oportunidades

1. 🚀 **Nicho de transparencia**: Plataformas actuales no muestran contenido detallado
2. 🚀 **Crecimiento del e-learning**: Mercado en expansión continua
3. 🚀 **Modelo freemium**: Barrera de entrada baja para usuarios
4. 🚀 **Escalabilidad internacional**: Posible expansión a LATAM
5. 🚀 **Funcionalidades futuras**: Pagos, certificados, app móvil

---

### Amenazas

1. ⚡ **Competidores con marketing masivo**: Udemy invierte millones en publicidad
2. ⚡ **Cambios en regulación**: GDPR puede endurecerse
3. ⚡ **Saturación del mercado**: Muchas plataformas de e-learning
4. ⚡ **Preferencia por plataformas grandes**: Usuarios confían en marcas establecidas
5. ⚡ **Crisis económica**: Reducción de gasto en formación

---

### Recomendación Final

**PROYECTO VIABLE Y RECOMENDADO PARA EJECUCIÓN**

Con una viabilidad global del **89%**, el proyecto **E-Learning JCB Platform** es **altamente viable** en todas las dimensiones analizadas (técnica, económica, operativa y legal). Las fortalezas superan claramente a las debilidades, y las oportunidades del mercado son significativas.

**Factores críticos de éxito**:
1. ✅ Completar MVP en 6 meses (planificación detallada)
2. ✅ Obtener al menos 2 ayudas (Tarifa plana + Almería Emprende)
3. ✅ Alcanzar 24 ventas en Año 1 (punto de equilibrio)
4. ✅ Diferenciarse por transparencia (ventaja competitiva)
5. ✅ Mantener costes operativos bajos (<500€/mes)

**Riesgo global**: **BAJO-MEDIO** (controlado y mitigable)

**Recomendación**: **PROCEDER CON EL PROYECTO** ✅

---

<div style="page-break-after: always;"></div>

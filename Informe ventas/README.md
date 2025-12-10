# 📊 Análisis de Ventas - Sistema Completo

Este proyecto contiene un sistema completo para analizar datos de ventas, generar visualizaciones y crear informes en diferentes formatos.

## 📁 Estructura del Proyecto

```
Informe ventas/
├── generar_datos.py          # Genera datos sintéticos de ventas
├── analisis.py               # Script de análisis completo
├── generar_informe.py        # Genera informe HTML con gráficos embebidos
├── analisis_ventas.ipynb     # Jupyter Notebook interactivo
├── ventas.csv                # Datos de ventas (generado)
├── ventas_por_mes.png        # Gráfico de ventas mensuales
├── top5_productos.png        # Gráfico de top 5 productos
└── informe_ventas.html       # Informe HTML completo (generado)
```

## 🚀 Uso Rápido

### Opción 1: Análisis con Scripts Python

1. **Generar datos sintéticos** (si no tienes `ventas.csv`):
```bash
python generar_datos.py
```

2. **Ejecutar análisis completo**:
```bash
python analisis.py
```
Esto generará:
- Análisis en consola
- Gráficos: `ventas_por_mes.png` y `top5_productos.png`

3. **Generar informe HTML**:
```bash
python generar_informe.py
```
Esto creará `informe_ventas.html` con todas las conclusiones y gráficos embebidos.

### Opción 2: Jupyter Notebook (Recomendado)

1. **Abrir el notebook**:
   - En VS Code: Abre `analisis_ventas.ipynb`
   - En JupyterLab: `jupyter lab analisis_ventas.ipynb`
   - En Jupyter Notebook: `jupyter notebook analisis_ventas.ipynb`

2. **Ejecutar las celdas**:
   - Ejecuta todas las celdas en orden (Run All)
   - O ejecuta celda por celda para ver los resultados paso a paso

3. **Ventajas del Notebook**:
   - ✅ Código, texto y gráficos en un solo documento
   - ✅ Ejecución interactiva
   - ✅ Fácil de compartir y presentar
   - ✅ Permite modificar y experimentar fácilmente

## 📋 Requisitos

Instala las dependencias necesarias:

```bash
pip install pandas matplotlib seaborn jupyter
```

O crea un archivo `requirements.txt`:

```txt
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
```

Luego instala con:
```bash
pip install -r requirements.txt
```

## 📊 Funcionalidades

### Análisis Realizado

1. **Ventas totales por mes**
   - Ingresos totales por mes
   - Cantidad de unidades vendidas por mes
   - Gráficos de líneas y barras

2. **Análisis por producto**
   - Producto más vendido (en cantidad)
   - Producto con mayores ingresos
   - Top 5 productos por ingresos
   - Top 5 productos por cantidad
   - Gráficos de barras horizontales

3. **Métricas generales**
   - Total de ingresos
   - Total de unidades vendidas
   - Promedio por venta
   - Número de productos diferentes

### Formatos de Salida

#### 1. Informe HTML (`informe_ventas.html`)
- ✅ Diseño profesional y moderno
- ✅ Gráficos embebidos (no requiere archivos externos)
- ✅ Tablas interactivas
- ✅ Conclusiones y recomendaciones
- ✅ Listo para imprimir o compartir

#### 2. Jupyter Notebook (`analisis_ventas.ipynb`)
- ✅ Código ejecutable paso a paso
- ✅ Visualizaciones interactivas
- ✅ Documentación en Markdown
- ✅ Fácil de modificar y experimentar

#### 3. Gráficos PNG
- `ventas_por_mes.png`: Ventas mensuales
- `top5_productos.png`: Top productos

## 🔧 Personalización

### Modificar el análisis

Edita `analisis.py` o las celdas del notebook para:
- Cambiar los periodos de análisis
- Agregar nuevas métricas
- Modificar los gráficos
- Incluir análisis adicionales

### Personalizar el informe HTML

Edita `generar_informe.py` para:
- Cambiar el diseño y colores
- Agregar secciones adicionales
- Modificar las conclusiones
- Incluir más gráficos

## 📝 Formato del CSV

El archivo `ventas.csv` debe tener el siguiente formato:

```csv
fecha,producto,cantidad,precio
2025-01-05,A,3,10.0
2025-01-20,B,1,20.0
2025-02-13,A,2,10.0
...
```

**Columnas requeridas:**
- `fecha`: Fecha en formato YYYY-MM-DD
- `producto`: Nombre o código del producto
- `cantidad`: Cantidad vendida (entero)
- `precio`: Precio unitario (decimal)

## 💡 Ejemplos de Uso

### Análisis rápido desde consola
```bash
python analisis.py
```

### Generar informe completo
```bash
python generar_datos.py  # Si no tienes datos
python analisis.py        # Genera gráficos
python generar_informe.py # Genera HTML
```

### Trabajar con Jupyter
```bash
jupyter lab analisis_ventas.ipynb
```

## 🎯 Próximos Pasos

Para expandir este proyecto puedes:

1. **Conectar con base de datos real**
   - SQLite, PostgreSQL, MySQL
   - Leer directamente desde la BD

2. **Agregar más análisis**
   - Análisis de tendencias
   - Predicciones con machine learning
   - Análisis de estacionalidad

3. **Crear dashboard interactivo**
   - Streamlit
   - Dash (Plotly)
   - Panel

4. **Automatizar reportes**
   - Programar ejecución automática
   - Enviar por email
   - Subir a la nube

## 📞 Soporte

Si tienes problemas:
1. Verifica que todos los archivos estén en la misma carpeta
2. Asegúrate de tener instaladas todas las dependencias
3. Ejecuta primero `generar_datos.py` si falta `ventas.csv`
4. Ejecuta `analisis.py` antes de `generar_informe.py` para generar los gráficos

---

**¡Disfruta analizando tus datos de ventas!** 📊✨


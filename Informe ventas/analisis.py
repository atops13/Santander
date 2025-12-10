"""
Análisis de ventas de una tienda
Supongamos que disponemos de un archivo CSV con datos de ventas de una tienda, 
con columnas como "fecha", "producto", "cantidad vendida", "precio". 
El objetivo es analizar estos datos para obtener:

- Ventas totales por mes.
- Producto más vendido (en cantidad) y producto con mayores ingresos.
- Visualizaciones: gráfico de ventas por mes, gráfico de ventas por producto (top 5).
Utilizaremos pandas para manipular los datos y matplotlib (o seaborn) para gráficas
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurar estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# 1. Cargar datos del CSV
print("=" * 60)
print("ANALISIS DE VENTAS")
print("=" * 60)

archivo_csv = 'ventas.csv'
try:
    df = pd.read_csv(archivo_csv)
    print(f"\n[OK] Datos cargados desde: {archivo_csv}")
    print(f"     Total de registros: {len(df)}")
except FileNotFoundError:
    print(f"\n[ERROR] No se encontro el archivo {archivo_csv}")
    print("        Ejecuta primero: python generar_datos.py")
    exit(1)

# Convertir fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Calcular ingresos por venta (cantidad * precio)
df['ingresos'] = df['cantidad'] * df['precio']

# Mostrar información básica
print(f"\nPrimeras filas del dataset:")
print(df.head())
print(f"\nInformacion del dataset:")
print(df.info())
print(f"\nEstadisticas descriptivas:")
print(df.describe())

# 2. Calcular ventas totales por mes
print("\n" + "=" * 60)
print("VENTAS TOTALES POR MES")
print("=" * 60)

# Extraer año-mes
df['año_mes'] = df['fecha'].dt.to_period('M')

# Agrupar por mes y calcular totales
ventas_por_mes = df.groupby('año_mes').agg({
    'ingresos': 'sum',
    'cantidad': 'sum'
}).reset_index()

ventas_por_mes.columns = ['mes', 'ingresos_totales', 'cantidad_total']
ventas_por_mes['mes_str'] = ventas_por_mes['mes'].astype(str)

print("\nVentas totales por mes:")
print(ventas_por_mes[['mes_str', 'ingresos_totales', 'cantidad_total']].to_string(index=False))

# 3. Determinar producto más vendido y con mayor ingresos
print("\n" + "=" * 60)
print("ANALISIS POR PRODUCTO")
print("=" * 60)

# Agrupar por producto
ventas_por_producto = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingresos': 'sum',
    'precio': 'mean'
}).reset_index()

ventas_por_producto.columns = ['producto', 'cantidad_total', 'ingresos_totales', 'precio_promedio']
ventas_por_producto = ventas_por_producto.sort_values('ingresos_totales', ascending=False)

print("\nResumen por producto:")
print(ventas_por_producto.to_string(index=False))

# Producto más vendido (en cantidad)
producto_mas_vendido = ventas_por_producto.sort_values('cantidad_total', ascending=False).iloc[0]
print(f"\n[PRODUCTO MAS VENDIDO (cantidad)]")
print(f"   Producto: {producto_mas_vendido['producto']}")
print(f"   Cantidad total: {producto_mas_vendido['cantidad_total']:.0f} unidades")
print(f"   Ingresos: ${producto_mas_vendido['ingresos_totales']:.2f}")

# Producto con mayores ingresos
producto_mayor_ingresos = ventas_por_producto.iloc[0]
print(f"\n[PRODUCTO CON MAYORES INGRESOS]")
print(f"   Producto: {producto_mayor_ingresos['producto']}")
print(f"   Ingresos totales: ${producto_mayor_ingresos['ingresos_totales']:.2f}")
print(f"   Cantidad vendida: {producto_mayor_ingresos['cantidad_total']:.0f} unidades")

# Top 5 productos por ingresos
top5_productos = ventas_por_producto.head(5)
print(f"\n[TOP 5 PRODUCTOS POR INGRESOS]")
print(top5_productos[['producto', 'ingresos_totales', 'cantidad_total']].to_string(index=False))

# 4. Graficar ventas por mes
print("\n" + "=" * 60)
print("GENERANDO GRAFICOS...")
print("=" * 60)

# Crear figura con subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Ventas por mes (ingresos)
ax1 = axes[0]
ax1.plot(ventas_por_mes['mes_str'], ventas_por_mes['ingresos_totales'], 
         marker='o', linewidth=2, markersize=8, color='#2ecc71')
ax1.set_title('Ventas Totales por Mes (Ingresos)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Ingresos ($)', fontsize=12)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.tick_params(axis='x', rotation=45)

# Agregar valores en los puntos
for i, (mes, ingreso) in enumerate(zip(ventas_por_mes['mes_str'], ventas_por_mes['ingresos_totales'])):
    ax1.annotate(f'${ingreso:.0f}', 
                (i, ingreso), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center',
                fontsize=9)

# Gráfico 2: Ventas por mes (cantidad)
ax2 = axes[1]
ax2.bar(ventas_por_mes['mes_str'], ventas_por_mes['cantidad_total'], 
        color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
ax2.set_title('Cantidad de Unidades Vendidas por Mes', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Mes', fontsize=12)
ax2.set_ylabel('Cantidad Total', fontsize=12)
ax2.grid(True, alpha=0.3, linestyle='--', axis='y')
ax2.tick_params(axis='x', rotation=45)

# Agregar valores en las barras
for i, (mes, cantidad) in enumerate(zip(ventas_por_mes['mes_str'], ventas_por_mes['cantidad_total'])):
    ax2.text(i, cantidad, f'{cantidad:.0f}', 
            ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('ventas_por_mes.png', dpi=300, bbox_inches='tight')
print("[OK] Grafico guardado: ventas_por_mes.png")
plt.show()

# 5. Graficar top 5 productos por ingresos
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 3: Top 5 productos por ingresos (barras horizontales)
ax3 = axes[0]
top5_ordenado = top5_productos.sort_values('ingresos_totales', ascending=True)
colores = sns.color_palette("viridis", len(top5_ordenado))
ax3.barh(top5_ordenado['producto'], top5_ordenado['ingresos_totales'], 
         color=colores, alpha=0.8, edgecolor='black', linewidth=1.5)
ax3.set_title('Top 5 Productos por Ingresos', fontsize=14, fontweight='bold', pad=15)
ax3.set_xlabel('Ingresos Totales ($)', fontsize=12)
ax3.set_ylabel('Producto', fontsize=12)
ax3.grid(True, alpha=0.3, linestyle='--', axis='x')

# Agregar valores en las barras
for i, (producto, ingreso) in enumerate(zip(top5_ordenado['producto'], top5_ordenado['ingresos_totales'])):
    ax3.text(ingreso, i, f'${ingreso:.0f}', 
            ha='left', va='center', fontsize=10, fontweight='bold', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

# Gráfico 4: Top 5 productos por cantidad vendida
ax4 = axes[1]
top5_cantidad = ventas_por_producto.sort_values('cantidad_total', ascending=False).head(5)
top5_cantidad_ordenado = top5_cantidad.sort_values('cantidad_total', ascending=True)
colores2 = sns.color_palette("plasma", len(top5_cantidad_ordenado))
ax4.barh(top5_cantidad_ordenado['producto'], top5_cantidad_ordenado['cantidad_total'], 
         color=colores2, alpha=0.8, edgecolor='black', linewidth=1.5)
ax4.set_title('Top 5 Productos por Cantidad Vendida', fontsize=14, fontweight='bold', pad=15)
ax4.set_xlabel('Cantidad Total (unidades)', fontsize=12)
ax4.set_ylabel('Producto', fontsize=12)
ax4.grid(True, alpha=0.3, linestyle='--', axis='x')

# Agregar valores en las barras
for i, (producto, cantidad) in enumerate(zip(top5_cantidad_ordenado['producto'], top5_cantidad_ordenado['cantidad_total'])):
    ax4.text(cantidad, i, f'{cantidad:.0f}', 
            ha='left', va='center', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

plt.tight_layout()
plt.savefig('top5_productos.png', dpi=300, bbox_inches='tight')
print("[OK] Grafico guardado: top5_productos.png")
plt.show()

# Resumen final
print("\n" + "=" * 60)
print("RESUMEN FINAL")
print("=" * 60)
print(f"Total de ingresos: ${df['ingresos'].sum():.2f}")
print(f"Total de unidades vendidas: {df['cantidad'].sum():.0f}")
print(f"Promedio de ingresos por venta: ${df['ingresos'].mean():.2f}")
print(f"Numero de productos diferentes: {df['producto'].nunique()}")
print(f"Periodo analizado: {df['fecha'].min().strftime('%d/%m/%Y')} - {df['fecha'].max().strftime('%d/%m/%Y')}")
print("\n" + "=" * 60)
print("Analisis completado exitosamente!")
print("=" * 60)

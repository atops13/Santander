"""
Script para generar datos sintéticos de ventas
Genera un CSV con columnas: fecha, producto, cantidad, precio
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuración
np.random.seed(42)  # Para reproducibilidad
random.seed(42)

# Productos disponibles
productos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Precios base por producto (en euros)
precios_base = {
    'A': 10.0,
    'B': 20.0,
    'C': 15.0,
    'D': 25.0,
    'E': 30.0,
    'F': 12.0,
    'G': 18.0,
    'H': 22.0
}

# Fecha inicial: 1 de enero de 2025
fecha_inicio = datetime(2025, 1, 1)
fecha_fin = datetime(2025, 4, 30)  # Hasta final de abril (4 meses de datos)

# Generar lista de ventas
ventas = []

# Generar aproximadamente 200 ventas distribuidas en los meses
num_ventas = 200

for _ in range(num_ventas):
    # Fecha aleatoria entre fecha_inicio y fecha_fin
    dias_aleatorios = random.randint(0, (fecha_fin - fecha_inicio).days)
    fecha = fecha_inicio + timedelta(days=dias_aleatorios)
    
    # Producto aleatorio
    producto = random.choice(productos)
    
    # Cantidad (1-10 unidades, con más probabilidad en rangos bajos)
    cantidad = random.choices(
        range(1, 11),
        weights=[30, 25, 20, 10, 5, 4, 3, 2, 1, 0.5]  # Más probabilidad de cantidades bajas
    )[0]
    
    # Precio con pequeñas variaciones (±10%)
    precio_base = precios_base[producto]
    variacion = random.uniform(-0.1, 0.1)
    precio = round(precio_base * (1 + variacion), 2)
    
    ventas.append({
        'fecha': fecha.strftime('%Y-%m-%d'),
        'producto': producto,
        'cantidad': cantidad,
        'precio': precio
    })

# Crear DataFrame
df_ventas = pd.DataFrame(ventas)

# Ordenar por fecha
df_ventas = df_ventas.sort_values('fecha').reset_index(drop=True)

# Guardar en CSV
archivo_csv = 'ventas.csv'
df_ventas.to_csv(archivo_csv, index=False, encoding='utf-8')

print(f"Datos generados exitosamente: {archivo_csv}")
print(f"Total de ventas: {len(df_ventas)}")
print(f"Rango de fechas: {df_ventas['fecha'].min()} a {df_ventas['fecha'].max()}")
print(f"Productos: {', '.join(sorted(df_ventas['producto'].unique()))}")
print(f"\nPrimeras 10 filas:")
print(df_ventas.head(10).to_string(index=False))
print(f"\nUltimas 10 filas:")
print(df_ventas.tail(10).to_string(index=False))

# Estadísticas rápidas
print(f"\nEstadisticas:")
print(f"   Total de ingresos: ${df_ventas['cantidad'].mul(df_ventas['precio']).sum():.2f}")
print(f"   Total de unidades vendidas: {df_ventas['cantidad'].sum()}")
print(f"   Promedio de ventas por dia: {len(df_ventas) / ((fecha_fin - fecha_inicio).days + 1):.2f}")


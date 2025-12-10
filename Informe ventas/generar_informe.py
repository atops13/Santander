"""
Genera un informe HTML con los resultados del análisis de ventas
Incluye gráficos embebidos y conclusiones
"""
import pandas as pd
import base64
from datetime import datetime
import os

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64 para embebarla en HTML"""
    try:
        with open(ruta_imagen, 'rb') as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode('utf-8')
            extension = os.path.splitext(ruta_imagen)[1][1:].lower()
            return f"data:image/{extension};base64,{img_base64}"
    except FileNotFoundError:
        return None

def generar_informe_html():
    """Genera un informe HTML completo con los resultados del análisis"""
    
    # Cargar datos
    df = pd.read_csv('ventas.csv')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['ingresos'] = df['cantidad'] * df['precio']
    df['año_mes'] = df['fecha'].dt.to_period('M')
    
    # Calcular métricas
    ventas_por_mes = df.groupby('año_mes').agg({
        'ingresos': 'sum',
        'cantidad': 'sum'
    }).reset_index()
    ventas_por_mes['mes_str'] = ventas_por_mes['año_mes'].astype(str)
    
    ventas_por_producto = df.groupby('producto').agg({
        'cantidad': 'sum',
        'ingresos': 'sum',
        'precio': 'mean'
    }).reset_index()
    ventas_por_producto.columns = ['producto', 'cantidad_total', 'ingresos_totales', 'precio_promedio']
    ventas_por_producto = ventas_por_producto.sort_values('ingresos_totales', ascending=False)
    
    producto_mas_vendido = ventas_por_producto.sort_values('cantidad_total', ascending=False).iloc[0]
    producto_mayor_ingresos = ventas_por_producto.iloc[0]
    top5_productos = ventas_por_producto.head(5)
    
    # Convertir imágenes a base64
    img_ventas_mes = imagen_a_base64('ventas_por_mes.png')
    img_top5 = imagen_a_base64('top5_productos.png')
    
    # Generar HTML
    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe de Análisis de Ventas</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .section h3 {{
            color: #764ba2;
            font-size: 1.3em;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .metric-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .metric-card h4 {{
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .metric-card .value {{
            font-size: 2em;
            font-weight: bold;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        table th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        
        table tr:hover {{
            background-color: #f5f5f5;
        }}
        
        .chart-container {{
            margin: 30px 0;
            text-align: center;
            background: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
        }}
        
        .chart-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .highlight-box {{
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .highlight-box h4 {{
            color: #856404;
            margin-bottom: 10px;
        }}
        
        .conclusion {{
            background: #d1ecf1;
            border-left: 5px solid #0c5460;
            padding: 25px;
            margin: 30px 0;
            border-radius: 5px;
        }}
        
        .conclusion h3 {{
            color: #0c5460;
            margin-bottom: 15px;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        
        ul {{
            margin-left: 20px;
            margin-top: 10px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Informe de Análisis de Ventas</h1>
            <p>Generado el {datetime.now().strftime('%d de %B de %Y a las %H:%M')}</p>
        </div>
        
        <div class="content">
            <!-- Resumen Ejecutivo -->
            <div class="section">
                <h2>📈 Resumen Ejecutivo</h2>
                <div class="metrics-grid">
                    <div class="metric-card">
                        <h4>Total de Ingresos</h4>
                        <div class="value">${df['ingresos'].sum():,.2f}</div>
                    </div>
                    <div class="metric-card">
                        <h4>Unidades Vendidas</h4>
                        <div class="value">{df['cantidad'].sum():,}</div>
                    </div>
                    <div class="metric-card">
                        <h4>Promedio por Venta</h4>
                        <div class="value">${df['ingresos'].mean():.2f}</div>
                    </div>
                    <div class="metric-card">
                        <h4>Total de Ventas</h4>
                        <div class="value">{len(df):,}</div>
                    </div>
                </div>
                <p style="margin-top: 20px; font-size: 1.1em;">
                    <strong>Periodo analizado:</strong> {df['fecha'].min().strftime('%d/%m/%Y')} - {df['fecha'].max().strftime('%d/%m/%Y')}<br>
                    <strong>Productos diferentes:</strong> {df['producto'].nunique()}
                </p>
            </div>
            
            <!-- Ventas por Mes -->
            <div class="section">
                <h2>📅 Ventas por Mes</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Mes</th>
                            <th>Ingresos Totales</th>
                            <th>Cantidad Total</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    # Agregar filas de la tabla de ventas por mes
    for _, row in ventas_por_mes.iterrows():
        html_content += f"""
                        <tr>
                            <td><strong>{row['mes_str']}</strong></td>
                            <td>${row['ingresos']:,.2f}</td>
                            <td>{row['cantidad']:.0f} unidades</td>
                        </tr>
"""
    
    html_content += f"""
                    </tbody>
                </table>
"""
    
    if img_ventas_mes:
        html_content += f"""
                <div class="chart-container">
                    <h3>Gráfico de Ventas Mensuales</h3>
                    <img src="{img_ventas_mes}" alt="Gráfico de ventas por mes">
                </div>
"""
    
    # Análisis por Producto
    html_content += f"""
            </div>
            
            <!-- Análisis por Producto -->
            <div class="section">
                <h2>🛍️ Análisis por Producto</h2>
                
                <div class="highlight-box">
                    <h4>⭐ Producto Más Vendido (Cantidad)</h4>
                    <p><strong>Producto {producto_mas_vendido['producto']}</strong>: {producto_mas_vendido['cantidad_total']:.0f} unidades vendidas, generando ${producto_mas_vendido['ingresos_totales']:,.2f} en ingresos.</p>
                </div>
                
                <div class="highlight-box">
                    <h4>💰 Producto con Mayores Ingresos</h4>
                    <p><strong>Producto {producto_mayor_ingresos['producto']}</strong>: ${producto_mayor_ingresos['ingresos_totales']:,.2f} en ingresos totales, con {producto_mayor_ingresos['cantidad_total']:.0f} unidades vendidas.</p>
                </div>
                
                <h3>Resumen Completo por Producto</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Cantidad Total</th>
                            <th>Ingresos Totales</th>
                            <th>Precio Promedio</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    for _, row in ventas_por_producto.iterrows():
        html_content += f"""
                        <tr>
                            <td><strong>{row['producto']}</strong></td>
                            <td>{row['cantidad_total']:.0f}</td>
                            <td>${row['ingresos_totales']:,.2f}</td>
                            <td>${row['precio_promedio']:.2f}</td>
                        </tr>
"""
    
    html_content += f"""
                    </tbody>
                </table>
"""
    
    if img_top5:
        html_content += f"""
                <div class="chart-container">
                    <h3>Top 5 Productos</h3>
                    <img src="{img_top5}" alt="Gráfico de top 5 productos">
                </div>
"""
    
    # Conclusiones
    mes_max_ingresos = ventas_por_mes.loc[ventas_por_mes['ingresos'].idxmax()]
    mes_max_cantidad = ventas_por_mes.loc[ventas_por_mes['cantidad'].idxmax()]
    
    html_content += f"""
            </div>
            
            <!-- Conclusiones -->
            <div class="section">
                <h2>💡 Conclusiones y Recomendaciones</h2>
                <div class="conclusion">
                    <h3>Hallazgos Principales</h3>
                    <ul>
                        <li><strong>Mejor mes en ingresos:</strong> {mes_max_ingresos['mes_str']} con ${mes_max_ingresos['ingresos']:,.2f}</li>
                        <li><strong>Mejor mes en cantidad:</strong> {mes_max_cantidad['mes_str']} con {mes_max_cantidad['cantidad']:.0f} unidades</li>
                        <li><strong>Producto estrella:</strong> El producto {producto_mayor_ingresos['producto']} genera los mayores ingresos, mientras que el producto {producto_mas_vendido['producto']} es el más vendido en cantidad.</li>
                        <li><strong>Tendencia:</strong> {'Crecimiento positivo' if ventas_por_mes.iloc[-1]['ingresos'] > ventas_por_mes.iloc[0]['ingresos'] else 'Estable'} en los ingresos a lo largo del periodo analizado.</li>
                    </ul>
                    
                    <h3 style="margin-top: 20px;">Recomendaciones</h3>
                    <ul>
                        <li>Incrementar el stock y promoción del producto {producto_mayor_ingresos['producto']} debido a su alto rendimiento en ingresos.</li>
                        <li>Analizar estrategias para aumentar las ventas del producto {producto_mas_vendido['producto']} que tiene alta rotación.</li>
                        <li>Replicar las estrategias exitosas del mes {mes_max_ingresos['mes_str']} en otros periodos.</li>
                        <li>Considerar promociones para productos con menor rendimiento para mejorar su participación en el mercado.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Informe generado automáticamente por el Sistema de Análisis de Ventas</p>
            <p>© {datetime.now().year} - Todos los derechos reservados</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Guardar archivo HTML
    with open('informe_ventas.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Informe HTML generado exitosamente: informe_ventas.html")

if __name__ == '__main__':
    # Verificar que existan los archivos necesarios
    archivos_requeridos = ['ventas.csv', 'ventas_por_mes.png', 'top5_productos.png']
    faltantes = [f for f in archivos_requeridos if not os.path.exists(f)]
    
    if faltantes:
        print(f"Error: Faltan los siguientes archivos: {', '.join(faltantes)}")
        print("Ejecuta primero: python analisis.py")
    else:
        generar_informe_html()


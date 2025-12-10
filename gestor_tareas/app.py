"""
Aplicación Flask simple - Esqueleto básico
"""
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Crear instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu-clave-secreta-aqui-cambiala-en-produccion'  # Necesaria para flash messages

# Datos de ejemplo (en una app real, usarías una base de datos)
tareas = [
    {'id': 1, 'titulo': 'Aprender Flask', 'completada': False},
    {'id': 2, 'titulo': 'Crear API REST', 'completada': False},
]


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html', tareas=tareas)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    """Agregar una nueva tarea"""
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        if titulo:
            nueva_tarea = {
                'id': len(tareas) + 1,
                'titulo': titulo,
                'completada': False
            }
            tareas.append(nueva_tarea)
            flash('Tarea agregada exitosamente', 'success')
            return redirect(url_for('index'))
        else:
            flash('El título no puede estar vacío', 'error')
    return render_template('agregar.html')


@app.route('/tarea/<int:tarea_id>')
def ver_tarea(tarea_id):
    """Ver detalles de una tarea"""
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    if tarea:
        return render_template('tarea.html', tarea=tarea)
    flash('Tarea no encontrada', 'error')
    return redirect(url_for('index'))


@app.route('/tarea/<int:tarea_id>/completar', methods=['POST'])
def completar_tarea(tarea_id):
    """Marcar una tarea como completada"""
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    if tarea:
        tarea['completada'] = not tarea['completada']
        estado = 'completada' if tarea['completada'] else 'pendiente'
        flash(f'Tarea marcada como {estado}', 'success')
    else:
        flash('Tarea no encontrada', 'error')
    return redirect(url_for('index'))


@app.route('/api/tareas')
def api_tareas():
    """API endpoint para obtener todas las tareas (JSON)"""
    return jsonify(tareas)


@app.route('/api/tarea/<int:tarea_id>')
def api_tarea(tarea_id):
    """API endpoint para obtener una tarea específica (JSON)"""
    tarea = next((t for t in tareas if t['id'] == tarea_id), None)
    if tarea:
        return jsonify(tarea)
    return jsonify({'error': 'Tarea no encontrada'}), 404


@app.errorhandler(404)
def pagina_no_encontrada(error):
    """Manejo de errores 404"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Ejecutar la aplicación en modo desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)


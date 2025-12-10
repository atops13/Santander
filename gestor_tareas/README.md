# Aplicación Flask - Esqueleto Simple

Esqueleto básico de una aplicación Flask con estructura organizada y funcionalidades comunes.

## Estructura del Proyecto

```
gestor_tareas/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── agregar.html      # Formulario para agregar tareas
│   ├── tarea.html        # Detalle de tarea
│   └── 404.html          # Página de error 404
└── static/               # Archivos estáticos
    └── css/
        └── style.css     # Estilos CSS
```

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:
```bash
python app.py
```

3. Abrir en el navegador:
```
http://localhost:5000
```

## Características

- ✅ Estructura organizada con templates y archivos estáticos
- ✅ Sistema de mensajes flash para notificaciones
- ✅ Manejo de errores 404
- ✅ API REST básica (endpoints JSON)
- ✅ Formularios y validación
- ✅ Diseño responsive con CSS moderno
- ✅ Sistema de rutas y navegación

## Rutas Disponibles

- `/` - Página principal (lista de tareas)
- `/agregar` - Formulario para agregar nueva tarea
- `/tarea/<id>` - Detalle de una tarea específica
- `/tarea/<id>/completar` - Marcar tarea como completada/pendiente
- `/api/tareas` - API JSON con todas las tareas
- `/api/tarea/<id>` - API JSON con una tarea específica

## Próximos Pasos

Para expandir esta aplicación, puedes:

1. **Base de datos**: Integrar SQLite, PostgreSQL o MySQL
2. **Autenticación**: Agregar login y registro de usuarios
3. **Validación**: Usar Flask-WTF para formularios más robustos
4. **Tests**: Agregar pruebas unitarias con pytest
5. **Despliegue**: Configurar para producción (gunicorn, nginx)

## Notas

- La clave secreta en `app.py` debe cambiarse en producción
- Los datos se almacenan en memoria (se pierden al reiniciar)
- El modo debug está activado (desactivar en producción)


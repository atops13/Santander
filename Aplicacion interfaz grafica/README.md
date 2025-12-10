# 📝 Editor de Notas - Aplicación de Escritorio con Tkinter

Aplicación de bloc de notas (notepad) simple creada con Tkinter, la biblioteca gráfica estándar de Python.

## 🚀 Características

- ✅ **Área de texto multi-línea** con scrollbar automático
- ✅ **Abrir archivos** de texto existentes
- ✅ **Guardar archivos** con nombre nuevo o existente
- ✅ **Guardar como** para crear copias
- ✅ **Deshacer/Rehacer** cambios
- ✅ **Cortar, Copiar y Pegar** texto
- ✅ **Seleccionar todo** el texto
- ✅ **Atajos de teclado** para todas las funciones
- ✅ **Barra de estado** que muestra el estado actual
- ✅ **Indicador de cambios** no guardados (asterisco en el título)
- ✅ **Confirmación** antes de cerrar si hay cambios sin guardar

## 📋 Requisitos

No se requieren instalaciones adicionales. Tkinter viene incluido con Python estándar.

**Nota**: En algunos sistemas Linux, puede ser necesario instalar tkinter:
```bash
sudo apt-get install python3-tk
```

## 🎮 Uso

### Ejecutar la aplicación

```bash
python notas.py
```

### Funcionalidades del Menú

#### Menú Archivo
- **Nuevo** (Ctrl+N): Crea un nuevo documento
- **Abrir** (Ctrl+O): Abre un archivo existente
- **Guardar** (Ctrl+S): Guarda el archivo actual
- **Guardar como...** (Ctrl+Shift+S): Guarda con un nombre nuevo
- **Salir** (Alt+F4): Cierra la aplicación

#### Menú Editar
- **Deshacer** (Ctrl+Z): Deshace la última acción
- **Rehacer** (Ctrl+Y): Rehace la acción deshecha
- **Cortar** (Ctrl+X): Corta el texto seleccionado
- **Copiar** (Ctrl+C): Copia el texto seleccionado
- **Pegar** (Ctrl+V): Pega el texto del portapapeles
- **Seleccionar todo** (Ctrl+A): Selecciona todo el texto

#### Menú Ayuda
- **Acerca de**: Muestra información de la aplicación

## ⌨️ Atajos de Teclado

| Acción | Atajo |
|--------|-------|
| Nuevo archivo | `Ctrl+N` |
| Abrir archivo | `Ctrl+O` |
| Guardar | `Ctrl+S` |
| Guardar como | `Ctrl+Shift+S` |
| Deshacer | `Ctrl+Z` |
| Rehacer | `Ctrl+Y` |
| Cortar | `Ctrl+X` |
| Copiar | `Ctrl+C` |
| Pegar | `Ctrl+V` |
| Seleccionar todo | `Ctrl+A` |
| Salir | `Alt+F4` |

## 💡 Características Adicionales

### Indicador de Cambios
- Cuando el documento tiene cambios sin guardar, aparece un asterisco (*) en el título de la ventana
- Al intentar cerrar o abrir otro archivo con cambios sin guardar, se pregunta si deseas guardar

### Barra de Estado
- Muestra mensajes informativos en la parte inferior
- Indica cuando se guarda, abre o crea un archivo
- Se actualiza automáticamente

### Soporte de Formatos
La aplicación puede abrir y guardar:
- Archivos de texto (.txt)
- Archivos Python (.py)
- Archivos Markdown (.md)
- Cualquier otro tipo de archivo de texto

### Codificación
- Los archivos se leen y guardan en UTF-8 por defecto
- Si hay problemas con UTF-8, intenta con Latin-1 automáticamente

## 🎨 Interfaz

La aplicación incluye:
- **Área de texto grande** con fuente monospace (Consolas)
- **Scrollbar automático** cuando el contenido es largo
- **Colores personalizados** para mejor legibilidad
- **Resaltado de selección** en azul
- **Barra de menú** completa con todas las opciones
- **Barra de estado** informativa

## 🔧 Personalización

Puedes modificar el archivo `notas.py` para personalizar:

### Cambiar el tamaño de la ventana
```python
self.geometry("800x600")  # Cambia estos valores
```

### Cambiar la fuente
```python
font=("Consolas", 11)  # Cambia el nombre y tamaño
```

### Cambiar los colores
```python
bg="white",           # Color de fondo
fg="black",           # Color del texto
selectbackground="#316AC5"  # Color de selección
```

## 📝 Ejemplo de Uso

1. **Ejecutar la aplicación**:
   ```bash
   python notas.py
   ```

2. **Escribir texto** en el área de texto

3. **Guardar el archivo**:
   - Menú: Archivo → Guardar (Ctrl+S)
   - O: Archivo → Guardar como... (Ctrl+Shift+S)

4. **Abrir un archivo existente**:
   - Menú: Archivo → Abrir (Ctrl+O)
   - Selecciona el archivo que deseas abrir

5. **Editar texto**:
   - Usa las opciones del menú Editar
   - O usa los atajos de teclado

## 🐛 Solución de Problemas

### La ventana no aparece
- Verifica que Tkinter esté instalado en tu sistema
- En Linux: `sudo apt-get install python3-tk`

### No se pueden guardar archivos
- Verifica los permisos de escritura en la carpeta
- Asegúrate de tener espacio en disco

### Los caracteres especiales no se muestran correctamente
- La aplicación usa UTF-8 por defecto
- Si hay problemas, intenta guardar con otra codificación manualmente

## 📚 Recursos

- [Documentación de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Tutorial de Tkinter](https://realpython.com/python-gui-tkinter/)

## 🎯 Próximas Mejoras Posibles

- [ ] Búsqueda y reemplazo de texto
- [ ] Numeración de líneas
- [ ] Temas (claro/oscuro)
- [ ] Múltiples pestañas
- [ ] Resaltado de sintaxis
- [ ] Impresión de documentos
- [ ] Historial de archivos recientes

---

**¡Disfruta editando tus notas!** 📝✨


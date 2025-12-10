"""
Aplicación de Bloc de Notas (Notepad) con Tkinter
Editor de texto simple con funcionalidades de abrir y guardar archivos
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os


class EditorNotas(tk.Tk):
    """Editor de notas simple con interfaz gráfica"""
    
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.title("Editor de Notas - Sin título")
        self.geometry("800x600")
        self.minsize(400, 300)
        
        # Variable para rastrear el archivo actual
        self.archivo_actual = None
        self.modificado = False
        
        # Crear la interfaz
        self.crear_menu()
        self.crear_area_texto()
        self.crear_barra_estado()
        self.configurar_atajos()
        
        # Actualizar título cuando se modifica el texto
        self.text_area.bind('<KeyPress>', self.marcar_modificado)
        self.text_area.bind('<Button-1>', self.marcar_modificado)
        
    def crear_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(
            label="Nuevo", 
            command=self.nuevo_archivo,
            accelerator="Ctrl+N"
        )
        menu_archivo.add_command(
            label="Abrir", 
            command=self.abrir_archivo,
            accelerator="Ctrl+O"
        )
        menu_archivo.add_command(
            label="Guardar", 
            command=self.guardar_archivo,
            accelerator="Ctrl+S"
        )
        menu_archivo.add_command(
            label="Guardar como...", 
            command=self.guardar_como,
            accelerator="Ctrl+Shift+S"
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir", 
            command=self.salir,
            accelerator="Alt+F4"
        )
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        
        # Menú Editar
        menu_editar = tk.Menu(menubar, tearoff=0)
        menu_editar.add_command(
            label="Deshacer", 
            command=lambda: self.text_area.event_generate("<<Undo>>"),
            accelerator="Ctrl+Z"
        )
        menu_editar.add_command(
            label="Rehacer", 
            command=lambda: self.text_area.event_generate("<<Redo>>"),
            accelerator="Ctrl+Y"
        )
        menu_editar.add_separator()
        menu_editar.add_command(
            label="Cortar", 
            command=lambda: self.text_area.event_generate("<<Cut>>"),
            accelerator="Ctrl+X"
        )
        menu_editar.add_command(
            label="Copiar", 
            command=lambda: self.text_area.event_generate("<<Copy>>"),
            accelerator="Ctrl+C"
        )
        menu_editar.add_command(
            label="Pegar", 
            command=lambda: self.text_area.event_generate("<<Paste>>"),
            accelerator="Ctrl+V"
        )
        menu_editar.add_separator()
        menu_editar.add_command(
            label="Seleccionar todo", 
            command=lambda: self.text_area.event_generate("<<SelectAll>>"),
            accelerator="Ctrl+A"
        )
        menubar.add_cascade(label="Editar", menu=menu_editar)
        
        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(
            label="Acerca de", 
            command=self.mostrar_acerca_de
        )
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        
        self.config(menu=menubar)
    
    def crear_area_texto(self):
        """Crea el área de texto con scrollbar"""
        # Frame para el área de texto y scrollbar
        frame_texto = tk.Frame(self)
        frame_texto.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Área de texto con scrollbar automático
        self.text_area = scrolledtext.ScrolledText(
            frame_texto,
            wrap=tk.WORD,
            undo=True,
            font=("Consolas", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            selectbackground="#316AC5",
            selectforeground="white"
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Configurar deshacer/rehacer
        self.text_area.config(undo=True, maxundo=50)
    
    def crear_barra_estado(self):
        """Crea la barra de estado en la parte inferior"""
        self.barra_estado = tk.Label(
            self,
            text="Listo",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padx=5
        )
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
    
    def configurar_atajos(self):
        """Configura los atajos de teclado"""
        self.bind('<Control-n>', lambda e: self.nuevo_archivo())
        self.bind('<Control-o>', lambda e: self.abrir_archivo())
        self.bind('<Control-s>', lambda e: self.guardar_archivo())
        self.bind('<Control-Shift-S>', lambda e: self.guardar_como())
        self.bind('<Control-a>', lambda e: self.text_area.event_generate("<<SelectAll>>"))
        self.bind('<Control-z>', lambda e: self.text_area.event_generate("<<Undo>>"))
        self.bind('<Control-y>', lambda e: self.text_area.event_generate("<<Redo>>"))
    
    def marcar_modificado(self, event=None):
        """Marca el documento como modificado"""
        if not self.modificado:
            self.modificado = True
            self.actualizar_titulo()
            self.actualizar_barra_estado("Documento modificado")
    
    def actualizar_titulo(self):
        """Actualiza el título de la ventana"""
        if self.archivo_actual:
            nombre_archivo = os.path.basename(self.archivo_actual)
            titulo = f"{nombre_archivo}"
            if self.modificado:
                titulo += " *"
            self.title(f"Editor de Notas - {titulo}")
        else:
            titulo = "Sin título"
            if self.modificado:
                titulo += " *"
            self.title(f"Editor de Notas - {titulo}")
    
    def actualizar_barra_estado(self, mensaje):
        """Actualiza el mensaje en la barra de estado"""
        self.barra_estado.config(text=mensaje)
        self.after(3000, lambda: self.barra_estado.config(text="Listo"))
    
    def nuevo_archivo(self):
        """Crea un nuevo archivo"""
        if self.modificado:
            if not self.confirmar_guardar():
                return
        
        self.text_area.delete(1.0, tk.END)
        self.archivo_actual = None
        self.modificado = False
        self.actualizar_titulo()
        self.actualizar_barra_estado("Nuevo archivo creado")
    
    def abrir_archivo(self):
        """Abre un archivo existente"""
        if self.modificado:
            if not self.confirmar_guardar():
                return
        
        filepath = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos Markdown", "*.md"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if not filepath:
            return
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, contenido)
            self.archivo_actual = filepath
            self.modificado = False
            self.actualizar_titulo()
            self.actualizar_barra_estado(f"Archivo abierto: {os.path.basename(filepath)}")
            
        except UnicodeDecodeError:
            # Intentar con otra codificación
            try:
                with open(filepath, "r", encoding="latin-1") as file:
                    contenido = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, contenido)
                self.archivo_actual = filepath
                self.modificado = False
                self.actualizar_titulo()
                self.actualizar_barra_estado(f"Archivo abierto: {os.path.basename(filepath)}")
            except Exception as e:
                messagebox.showerror(
                    "Error", 
                    f"No se pudo abrir el archivo:\n{e}"
                )
        except Exception as e:
            messagebox.showerror(
                "Error", 
                f"No se pudo abrir el archivo:\n{e}"
            )
    
    def guardar_archivo(self):
        """Guarda el archivo actual"""
        if self.archivo_actual:
            try:
                contenido = self.text_area.get(1.0, tk.END)
                with open(self.archivo_actual, "w", encoding="utf-8") as file:
                    file.write(contenido)
                self.modificado = False
                self.actualizar_titulo()
                self.actualizar_barra_estado(f"Archivo guardado: {os.path.basename(self.archivo_actual)}")
            except Exception as e:
                messagebox.showerror(
                    "Error", 
                    f"No se pudo guardar el archivo:\n{e}"
                )
        else:
            self.guardar_como()
    
    def guardar_como(self):
        """Guarda el archivo con un nombre nuevo"""
        filepath = filedialog.asksaveasfilename(
            title="Guardar archivo como",
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos Markdown", "*.md"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if not filepath:
            return
        
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            self.archivo_actual = filepath
            self.modificado = False
            self.actualizar_titulo()
            self.actualizar_barra_estado(f"Archivo guardado: {os.path.basename(filepath)}")
        except Exception as e:
            messagebox.showerror(
                "Error", 
                f"No se pudo guardar el archivo:\n{e}"
            )
    
    def confirmar_guardar(self):
        """Pregunta al usuario si desea guardar antes de continuar"""
        respuesta = messagebox.askyesnocancel(
            "Documento modificado",
            "El documento ha sido modificado. ¿Desea guardar los cambios?"
        )
        
        if respuesta is True:  # Usuario eligió "Sí"
            self.guardar_archivo()
            return True
        elif respuesta is False:  # Usuario eligió "No"
            return True
        else:  # Usuario eligió "Cancelar"
            return False
    
    def salir(self):
        """Sale de la aplicación"""
        if self.modificado:
            if not self.confirmar_guardar():
                return
        
        self.quit()
    
    def mostrar_acerca_de(self):
        """Muestra información sobre la aplicación"""
        messagebox.showinfo(
            "Acerca de",
            "Editor de Notas\n\n"
            "Aplicación simple de bloc de notas creada con Tkinter\n\n"
            "Funcionalidades:\n"
            "• Crear, abrir y guardar archivos de texto\n"
            "• Deshacer/Rehacer cambios\n"
            "• Cortar, copiar y pegar\n"
            "• Atajos de teclado\n\n"
            "Versión 1.0"
        )


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()

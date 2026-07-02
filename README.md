# 📝 Lista de Tareas en Consola (Python CLI)

Aplicación interactiva de línea de comandos (CLI) desarrollada completamente en **Python** para gestionar tareas de forma sencilla y eficiente. Está orientada a entornos **Linux**, priorizando la simplicidad, la rapidez de ejecución y la persistencia de datos mediante un archivo de texto, sin necesidad de utilizar bases de datos.

## 🚀 Características

- 📌 **Menú interactivo:** Interfaz en consola basada en un bucle continuo de ejecución.
- ✅ **Operaciones CRUD:** Permite listar, agregar, eliminar tareas individuales y vaciar la lista completa.
- 💾 **Persistencia de datos:** Guarda automáticamente las tareas en el archivo `tareas.txt`.
- 🔒 **Manejo seguro de archivos:** Uso de `with open()` y codificación **UTF-8** para soportar caracteres especiales en español.
- 🐍 **Sin dependencias externas:** Implementado únicamente con la biblioteca estándar de Python (`os` y `sys`).

---

## 📋 Requisitos

- Sistema operativo Linux (probado en **Ubuntu/Debian**).
- Python **3.13.7** o superior.

Verifica la versión instalada con:

```bash
python3 --version
```

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Katsuro03/Prompt_Engineering.git
```

2. Accede al directorio del proyecto:

```bash
cd Prompt_Engineering/lista_Tareas
```

3. Ejecuta la aplicación:

```bash
python3 todo.py
```

---

## 📂 Estructura del Proyecto

```text
lista_Tareas/
│
├── todo.py          # Lógica principal de la aplicación
├── tareas.txt       # Archivo generado automáticamente para almacenar las tareas
├── informe.pdf      # Reporte técnico (opcional)
├── informe.md       # Documentación en Markdown (opcional)
└── README.md        # Documentación del proyecto
```

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Biblioteca estándar de Python (`os` y `sys`)
- Archivos de texto plano para persistencia de datos

---

## 💡 Funcionalidades

- Agregar nuevas tareas.
- Mostrar todas las tareas almacenadas.
- Eliminar una tarea específica.
- Vaciar la lista de tareas.
- Guardado automático de la información.

---

## 👨‍💻 Autor

**Carlos Pilatuña**

Desarrollo inicial, implementación y documentación del proyecto.

GitHub: https://github.com/Katsuro03

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos y de aprendizaje. Puedes modificarlo y utilizarlo libremente como base para proyectos personales o académicos.

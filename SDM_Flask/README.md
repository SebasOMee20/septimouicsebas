# 🛡️ Sistema AntiCloaking Inteligente

Proyecto para detectar técnicas de *cloaking*: situaciones en las que un sitio web muestra contenido diferente dependiendo de quién realiza la petición.

El repositorio tiene dos partes:

1. **Sitio informativo (estático):** presenta el problema de forma visual y accesible, combinando conceptos de **Interacción Humano-Computadora (HCI/UX)** con técnicas de detección.
2. **Sistema web SDM_Flask:** aplicación en Flask con dashboard de reportes y almacenamiento en MySQL (XAMPP).

## 🌐 Ver demostración

👉 **[Abrir sitio informativo](https://sebasomee20.github.io/septimouicsebas/)**

> La demostración en GitHub Pages es la versión estática (explicación en audio, técnicas de cloaking y propuesta de detección). El sistema Flask con dashboard y base de datos se ejecuta de forma local, como se explica más abajo.

## ✨ Características

### Sitio informativo

- 🎯 Página de inicio con presentación del proyecto.
- 🔊 **Explicación en audio** sobre qué es el cloaking.
- 🧩 Técnicas de cloaking: User-Agent, dirección IP, retrasos y redirecciones, referencia de búsqueda.
- 🔍 Comparación visual entre lo que recibe un escáner y lo que ve una persona.
- 🤖 Sección conceptual de Machine Learning y comparación semántica.
- 🧠 Principios de HCI aplicados a la detección y prevención.
- ✨ Animaciones, partículas y efectos al hacer scroll.
- ♿ Soporte de `prefers-reduced-motion`.
- 📱 Diseño adaptable a diferentes pantallas.

### Sistema SDM_Flask

- 📊 Dashboard de reportes.
- 📝 Registro, consulta y edición de reportes de sitios sospechosos.
- 🗄️ Almacenamiento en base de datos MySQL.
- 🎨 Interfaz con el mismo diseño visual del sitio informativo.

## 🛠️ Tecnologías

- **HTML5, CSS3 y JavaScript** — interfaz, diseño responsive, animaciones e interacciones.
- **Canvas API y Web Audio API** — partículas de fondo y visualización del audio.
- **Python y Flask** — servidor web, rutas y plantillas.
- **Jinja2** — plantillas HTML (`templates/`).
- **MySQL / MariaDB (XAMPP)** — base de datos de reportes.
- **Google Fonts / Inter** — tipografía.

## 📁 Estructura del proyecto

```text
septimouicsebas/
├── index.html                      # Sitio informativo (GitHub Pages)
├── style.css
├── favicon.svg
├── anticloaking-explicacion.mp3
├── audio-explicativo-bg.jpg
├── cloaking-examples.jpg
├── wisteria-hero.jpg
└── SDM_Flask/                      # Sistema web con Flask
    ├── app.py                      # Aplicación y rutas
    ├── conexion.py                 # Conexión a MySQL
    ├── requirements.txt            # Dependencias de Python
    ├── sql/
    │   └── reportes.sql            # Script de la base de datos
    ├── templates/
    │   ├── index.html
    │   ├── dashboard.html
    │   └── editar_reporte.html
    └── static/                     # CSS, imágenes y audio
```

## 🚀 Ejecutar el sistema SDM_Flask

### Requisitos

- Python 3.10 o superior
- XAMPP (con MySQL/MariaDB)
- Git

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/SebasOMee20/septimouicsebas.git
cd septimouicsebas/SDM_Flask
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Abre **XAMPP** y enciende el módulo **MySQL**.

5. Entra a `http://localhost/phpmyadmin`, crea la base de datos `sebastian` e importa el archivo `sql/reportes.sql`.

6. Verifica que los datos de `conexion.py` coincidan con tu XAMPP (por defecto: host `localhost`, usuario `root`, contraseña vacía).

7. Ejecuta la aplicación:

```bash
python app.py
```

8. Abre `http://127.0.0.1:5000` en el navegador.

## 🖥️ Ver solo el sitio informativo

No requiere instalación. Abre `index.html` en la raíz del repositorio, o usa **Live Server** en Visual Studio Code (`http://localhost:5500`).

## 🔎 ¿Qué es el AntiCloaking?

El *cloaking* ocurre cuando un mismo sitio web entrega respuestas diferentes según características de la petición o del visitante. Por ejemplo, un sistema de seguridad podría recibir una versión aparentemente legítima mientras que una persona recibe otra.

La propuesta busca identificar estas diferencias mediante señales como:

1. **User-Agent:** comparación entre respuestas para rastreadores y navegadores.
2. **Dirección IP:** detección de respuestas condicionadas por rangos de IP.
3. **Tiempo:** cambios que aparecen después de una demora.
4. **Referencia de búsqueda:** comparación según el origen del acceso.

## 🤖 Propuesta de detección

```text
              ┌─────────────────────┐
              │      Sitio web      │
              └──────────┬──────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      Petición como bot       Petición como usuario
             │                       │
             ▼                       ▼
       Contenido A              Contenido B
             │                       │
             └───────────┬───────────┘
                         ▼
                Comparación semántica
                         │
                         ▼
                 Evidencia de cambio
                         │
                         ▼
                  Clasificación
```

Como parte de la propuesta de Machine Learning se contemplan técnicas como **SBERT, Random Forest y XGBoost**, además de un dataset etiquetado para distinguir entre sitios legítimos y casos de cloaking.

> **Nota:** los modelos de Machine Learning se plantean como parte del sistema completo y no están incluidos en esta versión.

## 🎓 Contexto académico

Proyecto desarrollado como parte del trabajo académico de **Ingeniería de Software** en la Universitaria de Colombia, enfocado en la investigación y propuesta de un sistema para la detección de sitios que utilizan técnicas de cloaking.

### Objetivo general

Diseñar una solución capaz de identificar diferencias sospechosas entre el contenido mostrado a sistemas automatizados y el contenido mostrado a usuarios reales, proporcionando evidencia que permita explicar la clasificación.

---

## 👨‍💻 Estado del proyecto

- **Sitio informativo:** implementado
- **Reproductor de audio e interacciones:** implementados
- **Backend Flask y dashboard:** implementado
- **Base de datos (MySQL/XAMPP):** implementada
- **Modelo de Machine Learning:** pendiente de integración

## 👤 Autor

Sebastián De la Ossa muñoz — Universitaria de Colombia
# SDM + Flask + MySQL

Landing "Sistema AntiCloaking Inteligente" servida con Flask, con el formulario
de reporte y el dashboard conectados a MySQL (XAMPP) en lugar de `localStorage`.

## 1. Base de datos

Con XAMPP corriendo (Apache + MySQL), abre phpMyAdmin, entra a la base de
datos **sebastian** (la misma que ya usa ProyectoFlask) y ejecuta el script
`sql/reportes.sql` para crear la tabla `reportes`.

## 2. Instalar dependencias

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## 3. Ejecutar

```bash
python app.py
```

Abre `http://127.0.0.1:5000/`.

## Rutas

| Ruta | Método | Qué hace |
|---|---|---|
| `/` | GET | Landing completa (SDM) |
| `/reportar` | POST | Guarda un reporte (nombre, correo) en la tabla `reportes` |
| `/dashboard` | GET | Página que lista todos los reportes guardados |
| `/dashboard/eliminar/<id>` | GET | Borra un reporte puntual |
| `/dashboard/vaciar` | GET | Borra todos los reportes |

## Qué cambió respecto al SDM original

- El formulario ya no escribe en `localStorage`: hace un POST real a `/reportar`,
  que inserta en MySQL.
- El botón "Dashboard" ya no abre un modal — ahora es un link a una página
  Flask (`/dashboard`) que consulta la tabla `reportes` y la renderiza con Jinja.
- Se eliminó todo el JS de `localStorage` (guardar, listar, borrar) que estaba
  en el `<script>` inicial del `index.html`.
- Todas las rutas de imágenes, CSS, favicon y audio pasaron a `static/` y usan
  `url_for('static', ...)`.

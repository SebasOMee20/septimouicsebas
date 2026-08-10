# 🛡️ Sistema AntiCloaking Inteligente

Sitio web informativo e interactivo desarrollado para presentar el proyecto **Sistema AntiCloaking Inteligente**, una propuesta orientada a detectar técnicas de *cloaking*: situaciones en las que un sitio web muestra contenido diferente dependiendo de quién realiza la petición.

La página explica el problema de forma visual y accesible, combinando conceptos de **Interacción Humano-Computadora (HCI/UX)** con técnicas de detección basadas en comparación de contenido y aprendizaje automático.

## ✨ Características

- 🎯 Página de inicio con presentación del proyecto.
- 🔊 **Explicación en audio** sobre qué es el cloaking.
- 🧩 Explicación de técnicas de cloaking:
  - User-Agent.
  - Dirección IP.
  - Retrasos y redirecciones.
  - Referencia de búsqueda.
- 🔍 Comparación visual entre lo que puede recibir un escáner y lo que puede ver una persona.
- 🤖 Sección conceptual sobre entrenamiento y clasificación mediante Machine Learning.
- 📊 Explicación de la comparación dual de contenido y similitud semántica.
- 🧠 Principios de HCI aplicados a la detección y prevención.
- 📝 Formulario demostrativo para reportar un sitio sospechoso.
- ✨ Animaciones, partículas, efectos de interacción y aparición progresiva al hacer scroll.
- ♿ Consideración de `prefers-reduced-motion` para reducir animaciones cuando el usuario lo solicita.
- 📱 Diseño adaptable a diferentes tamaños de pantalla.
- 🌐 Favicon y recursos visuales integrados.

## 🛠️ Tecnologías

- **HTML5** — estructura y contenido.
- **CSS3** — diseño visual, responsive design, tarjetas, gradientes y animaciones.
- **JavaScript** — interacciones, partículas, reproductor de audio, waveform, validación del formulario y efectos de scroll.
- **Canvas API** — partículas de fondo y visualización de la onda del audio.
- **Google Fonts / Inter** — tipografía utilizada en la interfaz.
- **MP3** — explicación de audio integrada en la página.

## 📁 Estructura del proyecto

```text
septimouicsebas/
├── index.html
├── style.css
├── favicon.svg
├── anticloaking-explicacion.mp3
├── audio-explicativo-bg.jpg
├── cloaking-examples.jpg
└── wisteria-hero.jpg
```

## 🔊 Audio explicativo

La página incorpora una explicación de aproximadamente un minuto para que cualquier visitante pueda comprender rápidamente qué es el cloaking y cuál es el propósito del proyecto.

El audio se carga directamente desde:

```text
anticloaking-explicacion.mp3
```

El reproductor utiliza JavaScript y la **Web Audio API** para generar una visualización dinámica de la frecuencia del audio.

## 🔎 ¿Qué es el AntiCloaking?

El *cloaking* ocurre cuando un mismo sitio web puede entregar respuestas diferentes dependiendo de características de la petición o del visitante.

Por ejemplo, un sistema automatizado de seguridad podría recibir una versión aparentemente legítima mientras que una persona recibe una versión diferente.

La propuesta AntiCloaking busca identificar estas diferencias mediante señales como:

1. **User-Agent:** comparación entre respuestas para rastreadores y navegadores.
2. **Dirección IP:** detección de respuestas condicionadas por rangos de IP.
3. **Tiempo:** observación de cambios que aparecen después de una demora.
4. **Referencia de búsqueda:** comparación según el origen desde el que se accede al sitio.

## 🤖 Propuesta de detección

El proyecto plantea una comparación entre dos perspectivas:

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

> **Nota:** este repositorio contiene principalmente el frontend y la demostración visual/informativa del proyecto. El backend, API y modelos de Machine Learning se plantean como componentes del sistema completo y no están incluidos en esta versión del sitio.

## 🚀 Ejecutar el proyecto

No requiere instalación de dependencias para visualizar la página.

### Opción 1 — Abrir directamente

Abre:

```text
index.html
```

### Opción 2 — Visual Studio Code

Puedes utilizar **Live Server** u otro servidor local para ejecutar el proyecto.

Por ejemplo:

```text
http://localhost:5500
```

## 🌐 Publicación

El proyecto está preparado para publicarse como sitio estático mediante **GitHub Pages**, ya que todos los recursos principales se encuentran dentro del repositorio y se cargan mediante rutas relativas.

## 🎓 Contexto académico

Proyecto desarrollado como parte del trabajo académico de **Ingeniería de Software**, enfocado en la investigación y propuesta de un sistema para la detección de sitios que utilizan técnicas de cloaking.

### Objetivo general

Diseñar una solución capaz de identificar diferencias sospechosas entre el contenido mostrado a sistemas automatizados y el contenido mostrado a usuarios reales, proporcionando evidencia que permita explicar la clasificación.

---

## 👨‍💻 Estado del proyecto

**Frontend:** En desarrollo / demostración funcional  
**Contenido AntiCloaking:** Implementado  
**Reproductor de audio:** Implementado  
**Interacciones JavaScript:** Implementadas  
**Backend/API:** Pendiente de integración  
**Modelo de Machine Learning:** Pendiente de integración

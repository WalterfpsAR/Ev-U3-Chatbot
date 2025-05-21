# 🎓 Chatbot Escolar Interactivo

Este proyecto es un chatbot web desarrollado en **Python** con el microframework **Flask**, diseñado para instituciones educativas que desean automatizar la atención de sus estudiantes. El sistema permite resolver preguntas frecuentes como fechas de reinscripción, trámites, horarios y también brinda atención personalizada mediante el número de control del alumno.

---

## 🚀 Funcionalidades principales

- ✅ Consultas generales: fechas, trámites, horarios, contacto.
- 🔐 Modo personalizado: permite al alumno consultar:
  - Calificaciones
  - Perfil académico
  - Adeudos
- 💬 Interfaz tipo mensajería con burbujas de texto.
- ⚡ Envío con tecla Enter.
- 🧠 Animación de escritura simulada (., .., ...).
- 🎯 Botones rápidos para interacción sin texto.

---

## 📁 Estructura del proyecto

```
chatbot_escolar/
├── app.py                     # Backend principal en Flask
├── informacion_escolar.json  # Datos simulados (alumnos y plantel)
├── static/
│   └── style.css              # Estilos visuales del chatbot
└── templates/
    └── index.html             # Interfaz HTML del chat
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología    | Uso                                |
|---------------|-------------------------------------|
| Python 3.13    | Lógica principal del backend       |
| Flask          | Microframework web ligero          |
| HTML + CSS     | Interfaz del chatbot               |
| JavaScript     | Animaciones, interactividad        |
| JSON           | Simulación de base de datos        |

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Navegador web actualizado

---

## ▶️ Cómo ejecutar

1. Clona este repositorio:
```bash
git clone https://github.com/WalterfpsAR/Ev-U3-Chatbot.git
cd chatbot-escolar
```
2. Instala Flask
```bash
pip install flask
```
4. Ejecuta el servidor Flask:
```bash
python app.py
```

4. Abre tu navegador en:
```
http://localhost:5000
```

---

## 🧪 Datos de prueba

Puedes usar los siguientes números de control para probar el modo personalizado:

- `21020041`

Consulta opciones como:
```
inicio
1
2
3
salir
```

---

## 🐞 Problemas resueltos

- `FileNotFoundError`: reubicación del JSON junto al `app.py`.
- Mensajes anchos: ajustado el ancho máximo y padding vía CSS.
- Comando “inicio” se confundía con “salir”: separados en la lógica.
- No se podía enviar con Enter: se añadió evento `keydown`.

---

## 📦 Entregables

- `app.py` – servidor Flask
- `index.html` – frontend del chatbot
- `style.css` – diseño visual
- `informacion_escolar.json` – base de datos simulada
- Este README

---

## 📌 Licencia

Este proyecto es de uso educativo y puede ser modificado o extendido libremente. Atribución no obligatoria, pero bienvenida.


from flask import Flask, render_template, request, jsonify, session
import json

app = Flask(__name__)
app.secret_key = "clave-supersecreta"

# Cargar la base completa
with open("informacion_escolar.json", "r", encoding="utf-8") as f:
    base = json.load(f)

# Separar parte general y alumnos
datos_generales = {
    "fechas": base["fechas"],
    "fichas_pago": base["fichas_pago"],
    "tramites": base["tramites"],
    "horarios": base["horarios"],
    "contacto": base["contacto"]
}
alumnos = base.get("alumnos", [])

def buscar_alumno(numero_control):
    return next(
        (alumno for alumno in alumnos if alumno["numero_control"].lower() == numero_control.lower()),
        None
    )

@app.route("/")
def home():
    session.clear()
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    mensaje_original = data.get("mensaje", "").strip()
    mensaje = mensaje_original.lower()

    if any(p in mensaje for p in ["fecha", "ficha", "constancia", "credencial", "documento", "horario", "contacto", "correo", "email", "teléfono"]):
        session["esperando_menu"] = False
        return jsonify({"respuesta": responder_pregunta(mensaje)})

    if mensaje == "salir":
        session.clear()
        return jsonify({"respuesta": "Has salido del modo alumno. Puedes hacer una nueva consulta o escribir 'inicio' para empezar."})

    if session.get("esperando_menu"):
        alumno = session.get("alumno")
        if mensaje in ["1", "calificaciones"]:
            calif = "\n".join(f"{mat}: {nota}" for mat, nota in alumno["calificaciones"].items())
            return jsonify({"respuesta": f"Tus calificaciones:\n{calif}"})
        elif mensaje in ["2", "perfil"]:
            perfil = f"Nombre: {alumno['nombre']}\nCarrera: {alumno['carrera']}\nSemestre: {alumno['semestre']}"
            return jsonify({"respuesta": perfil})
        elif mensaje in ["3", "adeudos"]:
            adeudos = alumno.get("adeudos", [])
            return jsonify({"respuesta": "Adeudos:\n" + "\n".join(adeudos) if adeudos else "No tienes adeudos."})
        else:
            return jsonify({"respuesta": "Opción inválida. Escribe 1, 2 o 3, o 'salir' para volver."})

    if session.get("esperando_control"):
        alumno = buscar_alumno(mensaje_original)
        if alumno:
            session["alumno"] = alumno
            session["esperando_control"] = False
            session["esperando_menu"] = True
            return jsonify({"respuesta": (
                f"Hola {alumno['nombre']} 👋\n¿Qué deseas consultar?\n"
                "1) Calificaciones\n2) Perfil\n3) Adeudos\nEscribe 'salir' para volver al inicio."
            )})
        else:
            return jsonify({"respuesta": "Número de control no encontrado. Intenta de nuevo."})

    if any(p in mensaje for p in ["consultar", "calificaciones", "perfil", "adeudos", "ver datos", "inicio"]):
        session["esperando_control"] = True
        return jsonify({"respuesta": "Por favor, ingresa tu número de control:"})

    return jsonify({"respuesta": "Lo siento, no entendí tu mensaje. Puedes preguntar por fechas, constancia, ficha de pago o escribir 'consultar'."})

def responder_pregunta(pregunta):
    if any(p in pregunta for p in ["fecha", "cuándo", "cuando", "día"]):
        return "\n".join(f"{k.capitalize()}: {v}" for k, v in datos_generales["fechas"].items())
    elif any(p in pregunta for p in ["ficha", "pago", "cuánto", "costo", "precio"]):
        ficha = datos_generales["fichas_pago"]["inscripcion"]
        return f"Monto: {ficha['monto']}\nFecha límite: {ficha['fecha_limite']}\nPasos: {ficha['pasos']}"
    elif any(p in pregunta for p in ["constancia", "credencial", "trámite", "documento"]):
        return "\n".join(f"{k.capitalize()}: {v}" for k, v in datos_generales["tramites"].items())
    elif "horario" in pregunta:
        return "\n".join(f"{k.replace('_', ' ').capitalize()}: {v}" for k, v in datos_generales["horarios"].items())
    elif any(p in pregunta for p in ["contacto", "correo", "email", "teléfono"]):
        return "\n".join(f"{k.replace('_', ' ').capitalize()}: {v}" for k, v in datos_generales["contacto"].items())
    return "Lo siento, no entendí tu pregunta. Intenta con: 'fechas', 'constancia', 'ficha de pago', etc."

if __name__ == "__main__":
    app.run(debug=True)

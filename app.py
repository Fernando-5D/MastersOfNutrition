import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages
app = Flask(__name__)

sesion = None
usuarios = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sesion")
def sesion():
    return render_template("sesion.html")

@app.route("/iniciandoSesion", methods = ("GET", "POST"))
def iniciandoSesion():
    if request.method == "POST":
        correo = request.form.get("correo")
        if correo in usuarios:
            passw = request.form.get("passw")
            if passw == usuarios[correo].passw:
                sesion = correo
            else:
                flash("La contraseña es incorrecta.")
        else:
            flash("No se encontro el usuario, ingresaste el correo correctamente?")
        
        if get_flashed_messages():
            return redirect(url_for("sesion"))
        else:
            return render_template("aqui la url de la plantilla principal")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registrando", methods = ("GET", "POST"))
def registrando():
    error = []
    if request.method == "POST":
        fechaNacim = datetime.strptime(request.form["fechaNac"], '%Y-%m-%d').date()

if __name__ == "__main__":
    app.run(debug=True)

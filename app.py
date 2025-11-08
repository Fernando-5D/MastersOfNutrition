import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages, session
app = Flask(__name__)

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
                nombre = usuarios[correo].nombre
                fechaNacim = usuarios[correo].fechaNacim
                genero = usuarios[correo].genero
                
                session["nombre"] = nombre
                session["fechaNacim"] = fechaNacim
                session["genero"] = genero
                session["correo"] = correo
                session["passw"] = passw
            else:
                flash("La contraseña es incorrecta.")
        else:
            flash("No se encontro el usuario, ingresaste el correo correctamente?")
        
        if get_flashed_messages():
            return redirect(url_for("sesion"))
        else:
            return render_template("index.html")

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

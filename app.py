import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)

sesion = None
usuarios = {}

@app.route("/sesion")
def sesion():
    return render_template("sesion.html")

@app.route("/iniciandoSesion", methods = ("GET", "POST"))
def iniciandoSesion():
    if request.method == "POST":
        correo = request.form.get("correo")
        for u in usuarios:
            if correo in usuarios:
                passw = request.form.get("passw")
                if passw == usuarios[correo].passw:
                    sesion = correo
                else:
                    flash("La contraseña es incorrecta.")
                    break
            else:
                flash("No se encontro el usuario, ingresaste el correo correctamente?")
                break
        
        return render_template("aqui la url de la plantilla principal")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registrando", methods = ("GET", "POST"))
def registrando():
    return

if __name__ == "__main__":
    app.run(debug=True)

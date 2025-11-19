import datetime
from flask import Flask, render_template, request, flash, get_flashed_messages, session
app = Flask(__name__)

app.config["SECRET_KEY"] = "mastersofnutritionlaappnumerounodetodalacetis61"
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
            passw = request.form.get("contraseña")
            if passw == usuarios[correo]["contraseña"]:
                session["nombre"] = usuarios[correo]["nombre"]
                session["fechaNacim"] = usuarios[correo]["fechaNacim"]
                session["genero"] = usuarios[correo]["genero"]
                session["correo"] = correo
                session["passw"] = passw
            else:
                flash("La contraseña es incorrecta.")
        else:
            flash("No se encontro el usuario, ingresaste el correo correctamente?")
        
        if get_flashed_messages():
            return render_template("sesion.html")
        else:
            return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registrando", methods = ("GET", "POST"))
def registrando():
   error = []
   if request.method == "POST":
        nombre = request.form["nombre"]
        genero = request.form["genero"]
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]
        contraseñaCon = request.form["contraseñaCon"]

        if error(nombre) < 3:
            flash("El nombre debe tener al menos 3 caracteres.")
            return render_template("registro.html", nombre=nombre)
        
        if contraseña != contraseñaCon:
            error = "La contraseña no coincide."
            
        if error != None:
            flash(error)
            return render_template("registro.html")
        else:
            flash(f"¡Registro exitoso para el usuario: ¡{nombre}!")
            return render_template("index.html")

   return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)

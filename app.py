from datetime import datetime, date
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
                return render_template("index.html")
            else:
                flash("La contraseña es incorrecta.")
        else:
            flash("No se encontro el usuario, ingresaste el correo correctamente?")
        
        return render_template("sesion.html")

@app.route("/cerrarSesion")
def cerrarSesion():
    session.clear()
    return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registrando", methods = ("GET", "POST"))
def registrando():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        fecha = datetime.strptime(request.form.get("fecha"), "%Y-%m-%d").date()
        genero = request.form.get("genero")
        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")
        contraseñaCon = request.form.get("contraseñaCon")

        if len(nombre) < 3:
            flash("El nombre debe tener al menos 3 caracteres.")
            return render_template("registro.html", nombre=nombre)
        
        if contraseña != contraseñaCon:
            flash("La contraseña no coincide.")
            return render_template("registro.html")
        
        if correo in usuarios:
            flash("El correo ya está registrado.")
            return render_template("registro.html")
        
        usuarios[correo] = {
            "nombre": nombre,
            "genero": genero,
            "contraseña": contraseña,
            "fechaNacim": fecha
        }
        
        session["nombre"] = nombre
        session["fechaNacim"] = fecha
        session["genero"] = genero
        session["correo"] = correo
        flash(f"¡Registro exitoso para el usuario: {nombre}!")
        return render_template("index.html")
    
    return render_template("registro.html")

if __name__ == "__main__":
    app.run(debug=True)

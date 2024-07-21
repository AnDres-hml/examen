from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unidad = 9000
        total_precio = precio_unidad * cantidad
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_sin_descuento = total_precio
        total_descuento = total_precio * descuento
        total_con_descuento = total_precio * (1 - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_descuento=total_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        usuarios = {
            "juan": "admin",
            "pepe": "user"
        }
        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == "juan":
                return f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                return f"Bienvenido usuario {usuario}"
        else:
            return "Nombre de usuario o contraseña incorrectos"

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from conexion import ConexionDB

app = Flask(__name__)

db = ConexionDB(app)
mysql = db.mysql


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/reportar', methods=['POST'])
def reportar():
    nombre = request.form['name']
    correo = request.form['email']
    link_sospechoso = request.form['link']
    mensaje = request.form['mensaje']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO reportes (nombre, correo, link_sospechoso, mensaje) VALUES (%s, %s, %s, %s)",
        (nombre, correo, link_sospechoso, mensaje)
    )
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('inicio', enviado=1))


@app.route('/dashboard')
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre, correo, link_sospechoso, mensaje, fecha_envio FROM reportes ORDER BY fecha_envio DESC")
    reportes = cur.fetchall()
    cur.close()
    return render_template('dashboard.html', reportes=reportes)


@app.route('/dashboard/editar/<int:id>', methods=['GET', 'POST'])
def editar_reporte(id):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']
        link_sospechoso = request.form['link']
        mensaje = request.form['mensaje']

        cur.execute(
            "UPDATE reportes SET nombre = %s, correo = %s, link_sospechoso = %s, mensaje = %s WHERE id = %s",
            (nombre, correo, link_sospechoso, mensaje, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('dashboard'))

    cur.execute("SELECT id, nombre, correo, link_sospechoso, mensaje FROM reportes WHERE id = %s", (id,))
    registro = cur.fetchone()
    cur.close()

    return render_template('editar_reporte.html', registro=registro)


@app.route('/dashboard/eliminar/<int:id>')
def eliminar_reporte(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM reportes WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dashboard'))


@app.route('/dashboard/vaciar')
def vaciar_reportes():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM reportes")
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = '!@#$%^&*()'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/registrar_cliente", methods=['GET', 'POST'])
def registrar_cliente():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM clientes')
        clientes = cur.fetchall()
        print(clientes)
        print(len(clientes))
        return render_template("registrar_cliente.html", clientes=clientes)
    elif request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        nro_carnet = request.form['nroCarnet']
        nro_telefono = request.form['nroTelefono']
        direccion = request.form['direccion']
        tipo_cliente = request.form['tipoCliente']
        
        print(request.form)

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO clientes (nombre, apellidos, nro_carnet, telefono, direccion, tipo) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, nro_carnet, nro_telefono, direccion, tipo_cliente))

        mysql.connection.commit()
        flash('Cliente registrado exitosamente!')
        return redirect(url_for("registrar_cliente"))


@app.route("/registrar_motociclista", methods=['GET', "POST"])
def registrar_motociclista():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM motociclistas')
        motociclistas = cur.fetchall()
        print(motociclistas)
        print(len(motociclistas))
        return render_template("registrar_motociclista.html", motociclistas=motociclistas)
    elif request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        nro_carnet = request.form['nroCarnet']
        nro_telefono = request.form['nroTelefono']
        direccion = request.form['direccion']
        nro_placa = request.form['placa']
        print(request.form)

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO motociclistas (nombre, apellidos, nro_carnet, telefono,direccion, placa) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, nro_carnet, nro_telefono, direccion, nro_placa))

        mysql.connection.commit()
        flash('Motociclista registrado exitosamente!')
        return redirect(url_for("registrar_motociclista"))


@app.route("/registrar_envio", methods=['POST', 'GET'])
def registrar_envio():
    if request.method == 'GET':

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM clientes WHERE tipo = \'Emisor\'')
        clientes_emisores = cur.fetchall()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM clientes WHERE tipo = \'Receptor\'')
        clientes_receptores = cur.fetchall()


        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM motociclistas')
        motociclistas = cur.fetchall()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM documentos')
        documentos = cur.fetchall()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM pagos')
        pagos = cur.fetchall()


        return render_template("registrar_envio.html",clientes_emisores=clientes_emisores,
        clientes_receptores=clientes_receptores, motociclistas=motociclistas, documentos=documentos, pagos=pagos)
    elif request.method == 'POST':
        emisor_id = request.form['emisorId']
        print(f"emisor id: {emisor_id}")



        direccion_recojo = request.form['direccionRecojo']
        print(f"direccion recojo: {direccion_recojo}")
        latitud_recojo = request.form['latitudRecojo']
        longitud_recojo = request.form['longitudRecojo']
        print(f"Latitud recojo: {latitud_recojo}")
        print(f"Longitud recojo: {longitud_recojo}")

        # insertar lugar recojo
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO lugares (direccion, latitud, longitud) VALUES (%s, %s, %s)', (direccion_recojo, latitud_recojo, longitud_recojo))

        mysql.connection.commit()
        
        # obtener id del ultimo lugar
        cur = mysql.connection.cursor()
        cur.execute('''SELECT MAX(id_lugar) FROM lugares''')

        max_id = cur.fetchone()
        id_lugar_recojo = max_id[0]
        print(f"max id: {max_id[0]}")
        if max_id[0] == None:
            id_lugar_recojo = 1

        print(f"max id: {max_id}")
        print(f"id lugar recojo: {id_lugar_recojo}")



        receptor_id = request.form['receptorId']
        print(f"receptor_id: {receptor_id} and type: {type(receptor_id)}")


        direccion_entrega = request.form['direccionEntrega']
        print(f"direccion entrega: {direccion_entrega}")

        latitud_entrega = request.form['latitudEntrega']
        longitud_entrega = request.form['longitudEntrega']

        print(f"Latitud entrega: {latitud_entrega} and type: {type(latitud_entrega)}")
        print(f"Longitud entrega: {longitud_entrega}")

        # insertar lugar entrega
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO lugares (direccion, latitud, longitud) VALUES (%s, %s, %s)', (direccion_entrega, latitud_entrega, longitud_entrega))

        mysql.connection.commit()


        cur = mysql.connection.cursor()
        cur.execute('''SELECT MAX(id_lugar) FROM lugares''')

        max_id = cur.fetchone()
        id_lugar_entrega = max_id[0]
        print(f"max id: {max_id[0]}")
        if max_id[0] == None:
            id_lugar_entrega = 1

        print(f"max id: {max_id}")
        print(f"id lugar recojo: {id_lugar_entrega}")



        
        motociclista_id = request.form['motociclistaId']

        print(f"motociclista_id: {motociclista_id}")

        documento_id = request.form['documentoId']
        print(f"documento id: {documento_id}")

        pago_id = request.form['pagoId']
        print(f"pago_id: {pago_id}")
        
        estado = 'Procesando'
        # insertar envio entrega
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO envios (id_cliente_emisor, id_cliente_receptor, id_lugar_recojo, id_lugar_entrega, id_motociclista, id_pago, id_documento, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (emisor_id, receptor_id, id_lugar_recojo, id_lugar_entrega, motociclista_id, pago_id, documento_id, estado))

        mysql.connection.commit()

        return redirect(url_for('registrar_envio'))



if __name__ == "__main__":
    app.run(debug=True)
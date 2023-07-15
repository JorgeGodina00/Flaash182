from flask import Flask, render_template, request, redirect, url_for, flash #Importacion de librerias
from flask_mysqldb import MySQL




app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="db_floreria"

app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("Select * from tbflores")
    consulta= cursorSelect.fetchall()
    
    return render_template('index.html', listflores= consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad= request.form['txtCantidad']
        Vprecio= request.form['txtPrecio']
      
        CS = mysql.connection.cursor() 
        CS.execute("INSERT INTO tbflores (nombre, cantidad, precio) VALUES (%s, %s, %s)", (Vnombre, Vcantidad, Vprecio))
        mysql.connection.commit()
    flash('Album Agregado Correctamente')    
    return redirect(url_for('index'))


@app.route('/eliminar/<id>')
def eliminar(id):
    id= request.args.get('id')
    curEliminar= mysql.connection.cursor()
    curEliminar.execute('Select * from tbflores where id= %s', (id,))
    consulId= curEliminar.fetchone()
    return render_template('eliminarflores.html',flor= consulId)


@app.route('/eliminar2/<id>', methods=['POST'])
def eliminar2(id):

    if request.method == 'POST':
        Vnombre= request.form['txtNombre']
        Vcantidad= request.form['txtCantidad']
        Vprecio= request.form['txtPrecio']

        CS= mysql.connection.cursor()
        CS.execute("delete from tbflores WHERE id= %s", (Vnombre, Vcantidad, Vprecio, id))
        mysql.connection.commit()
        
    flash("Registro Eliminado Correctamente")
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(port=5000, debug=True)
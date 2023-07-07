from flask import Flask, render_template, request, redirect, url_for, flash #Importacion de librerias
from flask_mysqldb import MySQL


#iniciar servidor Flask
#configuracion de BD
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="db_fruteria"

app.secret_key='mysecretkey'

mysql = MySQL(app)

#Declaracion de la ruta
#Ruta index
#La ruta se compone de la ruta y su funcion
@app.route('/')
def index():
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("Select * from tbfrutas")
    consulta= cursorSelect.fetchall()
    #print(consulta)
    return render_template('index.html', listfruta= consulta)

@app.route('/consultarunica/<fruta>')
def consultaunica(fruta):
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("Select * from tbfrutas where fruta= %s",(fruta,))
    consulta= cursorSelect.fetchall()
    return render_template('consultaunica.html', fruta=consulta)
@app.route('/consultarfrutas/')
def consultar():
     cursorSelect= mysql.connection.cursor()
     cursorSelect.execute("Select * from tbfrutas")
     consulta= cursorSelect.fetchall()
     return render_template('consultarfrutas.html', listfruta= consulta)
    

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock=request.form['txtStock']
        
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO tbfrutas (fruta, temporada, precio, stock) VALUES (%s, %s, %s, %s)", (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()
    flash('Frutas Agregadas Correctamente')    
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):  
    curEditar= mysql.connection.cursor()
    curEditar.execute('Select * from tbfrutas Where id= %s ', (id,))
    consulId= curEditar.fetchone()
    return render_template('editarfruta.html',fruta= consulId)

@app.route('/eliminar/<id>')
def eliminar(id):
    id= request.args.get('id')
    curEliminar= mysql.connection.cursor()
    curEliminar.execute('Select * from tbfrutas where id= %s', (id,))
    consulId= curEliminar.fetchone()
    return render_template('eliminarfruta.html',fruta= consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']

        CS= mysql.connection.cursor()
        CS.execute("UPDATE tbfrutas SET fruta= %s, temporada= %s, precio= %s, stock= %s WHERE id= %s", (Vfruta, Vtemporada, Vprecio, Vstock, id))
        mysql.connection.commit()
        
    flash("Frutas Actualizadas Correctamente")
    return redirect(url_for('index'))

@app.route('/eliminar2/<id>', methods=['POST'])
def eliminar2(id):
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']

        CS= mysql.connection.cursor()
        CS.execute("delete from tbfrutas WHERE id= %s", (Vfruta, Vtemporada, Vprecio, Vstock,id))
        mysql.connection.commit()
        
    flash("Frutas Actualizadas Correctamente")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
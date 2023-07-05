from flask import Flask, render_template, request, redirect, url_for, flash #Importacion de librerias
from flask_mysqldb import MySQL


#iniciar servidor Flask
#configuracion de BD
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysecretkey'

mysql = MySQL(app)

#Declaracion de la ruta
#Ruta index
#La ruta se compone de la ruta y su funcion
@app.route('/')
def index():
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("Select * from albums")
    consulta= cursorSelect.fetchall()
    #print(consulta)
    return render_template('index.html', listAlbums= consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        #print()
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO albums (titulo, artista, anio) VALUES (%s, %s, %s)", (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
    flash('Album Agregado Correctamente')    
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):  
    curEditar= mysql.connection.cursor()
    curEditar.execute('Select * from albums Where id= %s ', (id,))
    consulId= curEditar.fetchone()
    return render_template('editarAlbum.html',album= consulId)

@app.route('/eliminar/<id>')
def eliminar(id):
    id= request.args.get('id')
    curEliminar= mysql.connection.cursor()
    curEliminar.execute('Select * from albums where id= %s', (id,))
    consulId= curEliminar.fetchone()
    return render_template('eliminarAlbum.html',album= consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']

        CS= mysql.connection.cursor()
        CS.execute("UPDATE albums SET titulo= %s, artista= %s, anio= %s WHERE id= %s", (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        
    flash("Album Actualizado Correctamente")
    return redirect(url_for('index'))

@app.route('/eliminar2/<id>', methods=['POST'])
def eliminar2(id):
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']

        CS= mysql.connection.cursor()
        CS.execute("delete from albums WHERE id= %s", (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        
    flash("Album Actualizado Correctamente")
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(port=5000, debug=True)
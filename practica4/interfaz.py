from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from logica import *

# Creamos una instancia de tipo controlador
controlador = controladorBD()

# Procedemos a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarBebida(varnom.get(), varprecio.get(), varclas.get(), varmarca.get())
    varnom.set("")
    varprecio.set("")
    varclas.set("")
    varmarca.set("")
    

def ejecutaSelectU():
    rsbebida = controlador.consultarbebida(varBus.get())

    if rsbebida:
        textBus.delete("1.0","end")
        # usuario_data = str(rsUsuario[0])
        # Extraemos solamente nombre y correo
        usuario_data = f"Nombre: {rsbebida[0][1]}\nPrecio: {rsbebida[0][2]}"
        textBus.insert(tk.INSERT, usuario_data) 
    
    else:
        messagebox.showinfo("Cuidado", "Registro no registrado en la BD")
        textBus.delete("1.0","end")
        return
    

def ejecutaSelectA():
    rsUsuarios = controlador.consultarbebidas()
    # Limpiamos el treeview
    tree.delete(*tree.get_children())
    # Insertamos los datos en el treeview
    for usuario in rsUsuarios:
        tree.insert("", tk.END, values=usuario)
    return

  
def ejecutaUpdate():
    controlador.actualizarbebida(varid2.get(), varnom2.get(), varclas2.get(), varprecio2.get(), varmarca2.get())
    textBus.delete("1.0","end")
    varid2.set("")
    varnom2.set("")
    varclas2.set("")
    varprecio2.set("")
    return
 
def prombebidas():
    controlador.prombebida(precio3.get())
    precio3.set("")
    messagebox.showinfo("Promedio", "El promedio de bebidas es: ")
    return

def ejecutaDelete():
    controlador.eliminarbebida(varBuseliminar.get())  
    textBus.delete("1.0","end")
    varBuseliminar.set("")
    return


            
# Funcion para limpiar los campos   
def limpiarCampos():
    txtNom.delete(0, END)
    txtCor.delete(0, END)
    txtCon.delete(0, END)
    textBus.delete("1.0","end")
    return
 

# Creamos la ventana principal
ventana = Tk()
ventana.title("CRUD de Almacen de Bebidas")
ventana.geometry("650x400")

# Creamos el Notebook
panel = ttk.Notebook(ventana, style='TNotebook')
panel.pack(fill="both", expand="yes")

# Creamos un estilo para el Notebook
estilo = ttk.Style()
estilo.configure('TNotebook', tabposition='n')

# Creamos las pestañas
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)


# Agregamos las pestañas al Notebook
panel.add(pestana1, text="Registrar Bebida")
panel.add(pestana2, text="Buscar Registro")
panel.add(pestana3, text="Consultar Registros")
panel.add(pestana4, text="Actualizar Registro")
panel.add(pestana5, text="Eliminar Registro")


# Pestaña1: Formulario de Usuario
titulo1 = Label(pestana1, text="Registro de Bebida", font=("Arial", 20, "bold"), bg = '#535e57')
titulo1.pack(pady=10)

varnom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ")
lblNom.pack(pady=5)
txtNom = Entry(pestana1, textvariable=varnom, width=30)
txtNom.pack()

varprecio = tk.IntVar()
lblCor = Label(pestana1, text="Precio: ")
lblCor.pack(padx=5)
txtCor = Entry(pestana1, textvariable=varprecio, width=30)
txtCor.pack()

lblCon = Label(pestana1, text="Clasificacion: ")
lblCon.pack(pady=5)
varclas = tk.StringVar()
txtCon = Entry(pestana1, textvariable=varclas, width=30)
txtCon.pack()

lblMarca = Label(pestana1, text="Marca: ")
lblMarca.pack(pady=5)
varmarca = tk.StringVar()
txtMarca = Entry(pestana1, textvariable=varmarca, width=30)
txtMarca.pack()

btnGuardar = Button(pestana1, text="Guardar Registro", command=ejecutaInsert, bg="#008CBA", fg="white")
btnGuardar.pack(pady=10)

btnLimpiar = Button(pestana1, text="Limpiar Campos", command=limpiarCampos, bg="#008CBA", fg="white")
btnLimpiar.pack(pady=10)


# Creamos los elementos para la pestaña 2 (Buscar Registro)
titulo2= Label(pestana2, text="Buscar Registro", font=("Arial", 20, "bold"), bg = '#d2f5e0')
titulo2.pack(pady=10)

varBus = tk.StringVar()
lblid = Label(pestana2, text="Identificador de Registro: ")
lblid.pack(pady=5)

txtid = Entry(pestana2, textvariable=varBus, width=30)
txtid.pack()

btnBusqueda = Button(pestana2, text="Buscar Registro: ", command=ejecutaSelectU, bg="#008CBA", fg="white")
btnBusqueda.pack(pady=10)


subBus= Label(pestana2, text="Registro: ", font=("Arial", 10, "bold"), bg = '#0c0261')   
subBus.pack()

textBus = Text(pestana2, width=40, height=5)
textBus.pack(pady=10)


# Creamos los elementos para la pestaña 3 (Consultar usuarios)
titulo3 = Label(pestana3, text="Consultar Registros:", font=("Arial", 20, "bold"), bg= '#c6c6c5')
titulo3.pack(pady=10)

# Creamos un Treeview
tree = ttk.Treeview(pestana3, columns=(1,2,3, 4, 5), show="headings", height="5")
tree.pack()

# Creamos las columnas del Treeview
tree.heading(1, text="ID")
tree.heading(2, text="Nombre")
tree.heading(3, text="Precio")
tree.heading(4, text="Clasificacion")
tree.heading(5, text="Marca")

# Creamos un botón para consultar todos los usuarios
btnConsulta = Button(pestana3, text="Consultar Registros", command=ejecutaSelectA, bg="#008CBA", fg="white")
btnConsulta.pack(pady=10)


btnprom = Button(pestana3, text="Promedio Precio", command=prombebidas, bg="#008CBA", fg = "white")
btnprom.pack(pady=10)
precio3 = tk.DoubleVar()
txtprecio3 = Label(pestana3, textvariable=precio3, width=15)
txtprecio3.pack()

#btncontmarca = Button(pestana3, text="Total Por Marca", command=)

# Creamos los elementos para la pestaña 4 (Actualizar usuario)
titulo4 = Label(pestana4, text="Actualizar Registro", font=("Arial", 20, "bold"))
titulo4.pack(pady=10)

varid2 = tk.IntVar()
lblid = Label(pestana4, text="Identificador de Registro: ")
lblid.pack(pady=5)
txtid = Entry(pestana4, textvariable=varid2, width=30)
txtid.pack()

varnom2 = tk.StringVar()
lblNom = Label(pestana4, text="Nombre: ")
lblNom.pack(pady=5)
txtNom = Entry(pestana4, textvariable=varnom2, width=30)
txtNom.pack()


varclas2 = tk.StringVar()
lblCor = Label(pestana4, text="Clasificacion: ")
lblCor.pack(padx=5)
txtCor = Entry(pestana4, textvariable=varclas2, width=30)
txtCor.pack()

lblprecio = Label(pestana4, text="Precio: ")
lblprecio.pack(pady=5)
varprecio2 = tk.IntVar()
txtCon = Entry(pestana4, textvariable=varprecio2, width=30)
txtCon.pack()

varmarca2 = tk.StringVar()
lblmarcad = Label(pestana4, text="Marca: ")
lblmarcad.pack(pady=5)
txtmarcad = Entry(pestana4, textvariable=varmarca2, width=30)

btnActualizar = Button(pestana4, text="Actualizar usuario", command=ejecutaUpdate, bg="#008CBA", fg="white")
btnActualizar.pack(pady=5)

btnLimpiar = Button(pestana4, text="Limpiar campos", command=limpiarCampos, bg="#008CBA", fg="white")
btnLimpiar.pack(pady=5)

# Creamos los elementos para la pestaña 5 (Eliminar usuario)
titulo5 = Label(pestana5, text="Eliminar usuario", font=("Arial", 20, "bold"))
titulo5.pack(pady=10)

varBuseliminar = tk.StringVar()
lblid = Label(pestana5, text="Identificador de Usuario: ")
lblid.pack(pady=5)
    
txtid = Entry(pestana5, textvariable=varBuseliminar, width=30)
txtid.pack()

# Creamos un botón para eliminar un usuario
btnEliminar = Button(pestana5, text="Eliminar usuario", command=ejecutaDelete, bg="#008CBA", fg="white")
btnEliminar.pack(pady=10)



ventana.mainloop()
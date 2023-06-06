from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3



class controladorBD:
    
    def __init__(self):
        pass
        
    #1. preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/JABOW/Documents/GitHub/Flask182/practica4/bebidas.db")
            print("conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
      
    #Metodo para Insertar      
    def guardarBebida(self, nom, precio, clasificacion, marca):
        #1. llamar a la conexion
        conx = self.conexionBD()
        
        #2. Revisar parametros vacios
        if(nom == "" or precio == "" or clasificacion == "" or marca == ""):
            messagebox.showwarning("Cuidado", "Campos Vacios")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            
            
            #validad si el correo ya esta registrado
            sqlSelect = "select * from almacenbebidas where nombre=?"
            cursor.execute(sqlSelect, (nom,))
            rsUsuario = cursor.fetchall()
            
            if len(rsUsuario) > 0:
                messagebox.showerror("Error", "La bebida ya esta registrado")
                return
            
            datos = (nom, precio, clasificacion, marca)
            qrInsert = "insert into almacenbebidas(nombre, precio, clasificacion, marca) values(?,?,?,?)"
            
            #4. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "Registro exitoso")
            
       
    def consultarbebida(self, id):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. verificar el ID no este vacio
        if id =="":
            messagebox.showwarning("Cuidado", "Id vacio con escribe un valor")
         
            return
        else:
            try:
                #4. Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from almacenbebidas where id=?"
                    
                #5. Ejecutar la consulta y recuperar los datos
                cursor.execute(sqlSelect, (id,))
                rsbebida = cursor.fetchall()
                
                #6. cerrar conexion y devolver los datos
                print(rsbebida)
                conx.close()
                return rsbebida
            except Exception as ex:
                messagebox.showwarning("Error", str(ex))
                conx.close()
                return None
            
    def consultarbebidas(self):
        #1. preparar la conexion
        conx= self.conexionBD()
        
        #2. Preparar lo necesario para el select
        cursor= conx.cursor()
        sqlSelect="select * from almacenbebidas"
                
                #3. Ejecutar la consulta y recuperar los datos
        cursor.execute(sqlSelect)
        rsUsuarios = cursor.fetchall()
                
        #4. cerrar conexion y devolver los datos
        #print(rsUsuarios)
        conx.close()
        return rsUsuarios

    def actualizarbebida(self, id, nom, precio, clasificacion, marca):
        #1. preparar la conexion
        conx= self.conexionBD()
        
        #2. Revisar parametros vacios
        if(id == "" or nom == "" or precio == "" or clasificacion == "" or marca == ""):
            messagebox.showwarning("Cuidado", "Campos Vacios")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (nom, precio, clasificacion, marca, id)
            qrUpdate = "update almacenbebidas set nombre=?, precio=?, clasificacion=?, marca=? where id=?"
            
            #4.verificamos que el Usuario exista en la base de datos
            sqlSelect = "select * from almacenbebidas where id=?"
            cursor.execute(sqlSelect, (id,))
            rsUsuario = cursor.fetchall()

            if len(rsUsuario) == 0:
                messagebox.showerror("Error", "Registro no encontrado en la base de datos")
                return
            
            #5. confirmacion de guardad cambios
            confirmacion = messagebox.askquestion("Actualizar", "¿Estas seguro de guardar los cambios?")
            if confirmacion == "no":
                return    
            
            #6. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrUpdate, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Actualización", "Actualización exitosa")
            
            return None
     
    def prombebida(self, precio):
       conx = self.conexionBD()
       
       cursor = conx.cursor()
       sqlSelect = "select avg(precio) as PrecioPromedio from almacenbebidas"
       cursor.execute(sqlSelect)
       rsbebidas = cursor.fetchall()
       
       conx.close()
       return rsbebidas

    def cantidadmarca(self, marca):
        conx = self.conexionBD()
        
        cursor = conx.cursor()
        sqlSelect = "select count(marca) from almacenbebidas where marca=?"
        cursor.execute(sqlSelect)
        rsbebidas = cursor.fetchall()
        
        conx.close()
        return rsbebidas
    
    def cantidadclas(self, clasificacion):
        conx = self.conexionBD()
        
        cursor = conx.cursor()
        sqlSelect = "select count(clasificacion) from almacenbebidas where clasificacion=?"
        cursor.execute(sqlSelect)
        rsbebidas = cursor.fetchall()
        
        conx.close()
        return rsbebidas
        
    
    def eliminarbebida(self, id):
        #1. preparar la conexion
        conx= self.conexionBD()
            
        #2. Revisar parametros vacios
        if(id == ""):
            messagebox.showwarning("Cuidado", "Favor de llenaar todos los campos")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (id,)
            qrDelete = "delete from almacenbebidas where id=?"
            
            #4.confirmacion de eliminar usuario
            confirmacion = messagebox.askquestion("Eliminar", "¿Estas seguro de eliminar el Registro?")
            if confirmacion == "no":
                return  
            
            #5. verificamos si el usuario aun existe en nuestra base de datos
            sqlSelect = "select * from almacenbebidas where id=?"
            cursor.execute(sqlSelect, (id,))
            rsUsuario = cursor.fetchall()

            if len(rsUsuario) == 0:
                messagebox.showerror("Error", "El usuario no existe")
                return

            #6. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrDelete, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Eliminación", "Eliminación exitosa")
            
            return None
         
    


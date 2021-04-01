import mysql.connector
import tkinter as tk
from tkinter import messagebox 

dbConnect = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'prueba'
}

try:
    conexion = mysql.connector.connect(**dbConnect)
    cursor = conexion.cursor()
    try:
        sql = "select nombre, saldo from cliente, cuenta where cliente.identificacion = cuenta.identificacion"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(resultados)
    except:
        messagebox.showerror('Error', 'Error de consulta')
except:
    messagebox.showerror('Error', 'Error de conexion')
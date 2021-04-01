#FELIX CASTRO - TALLER 2 GUI CORTE 2

#importamos la clase tkinder
import tkinter as tk
from tkinter import messagebox

#funciones
def imprimir(lista, caso):
    try:
        if (caso == 1):
            for ventas in lista:
                cedula = str(ventas[0])
                nombre = ventas[1]
                cantidadComprada = int(ventas[2])
                subtoMenos5 = cantidadComprada * int(txtPrecio.get())
                descuentoMenos5 = subtoMenos5 * 10 / 100
                totalMenos5 = subtoMenos5 - descuentoMenos5
                #resulMenos5 = "Cedula:", cedula, "Nombre:", nombre, "Cantidad:", cantidadComprada, "Subtotal:", subtoMenos5, "Descuento 10%:", descuentoMenos5, "Total:", totalMenos5
                #lblRes.configure(text=resulMenos5)
                mensaje = ""
                mensaje += str(cedula)+" "+str(nombre)+" "+str(totalMenos5)
                messagebox.showinfo("Resultados", mensaje)
        elif (caso == 2):
            for ventas in lista:
                cedula = str(ventas[0])
                nombre = ventas[1]
                cantidadComprada = int(ventas[2])
                subtoMayIgu5Men10 = cantidadComprada * int(txtPrecio.get())
                descuentoMayIgu5Men10 = subtoMayIgu5Men10 * 10 / 100
                totMayIgu5Men10 = subtoMayIgu5Men10 - descuentoMayIgu5Men10
                resulMayIgu5Men10 = "Cedula:", cedula, "Nombre:", nombre, "Cantidad:", cantidadComprada, "Subtotal:", subtoMayIgu5Men10, "Descuento 10%:", descuentoMayIgu5Men10, "Total:", totMayIgu5Men10
                lblRes.configure(text=resulMayIgu5Men10)
        elif (caso == 3):
            for ventas in lista:
                cedula = str(ventas[0])
                nombre = ventas[1]
                cantidadComprada = int(ventas[2])
                subtoMay10 = cantidadComprada * int(txtPrecio.get())
                descuMay10 = subtoMay10 * 35 / 100
                totMay10 = subtoMay10 - descuMay10
                resulMay10 = "Cedula:", cedula, "Nombre:", nombre, "Cantidad:", cantidadComprada, "Subtotal:", subtoMay10, "Descuento 10%:", descuMay10, "Total:", totMay10
                lblRes.configure(text=resulMay10)
        else:
            print("Caso no encontrado")
    except ValueError:
        lblRes.configure(text="Verifica los datos")

def leer():
    try:
        menor5pc = []
        mayorigual5menor10 = []
        mayorigual10 = []
        todos = []

        f = open("ventaspc.txt", "r")

        for linea in f:
            linea = linea.strip()
            linea = linea.split(",")

            todos.append(linea)

            cedula = linea[0]
            nombre = linea[1]
            pcBuy = int(linea[2])

            if (pcBuy < 5):
                menor5pc.append(linea)
            
            if (pcBuy >= 5 and pcBuy < 10):
                mayorigual5menor10.append(linea)

            if (pcBuy >= 10):
                mayorigual10.append(linea)
        
        # primer parametro de la funcion imprimir es la lista
        # segundo parametro de la funcion imprimir es el caso
        # caso 1
        if(len(menor5pc) != 0):
            imprimir(menor5pc, 1)

        # caso 2
        if(len(mayorigual5menor10) != 0):
            imprimir(mayorigual5menor10, 2)

        # caso 3
        if(len(mayorigual10) != 0):
            imprimir(mayorigual10, 3)
    except ValueError:
        lblRes.configure(text="ERROR DE LECTURA DE ARCHIVO")

def escribir():
    try:
        f = open("ventaspc.txt", "a")
        cedula = input("Cédula del cliente:")
        nombre = input("Nombre del cliente:")
        cantidad = input("cantidad de pc:")

        registro = cedula+","+nombre+","+cantidad+"\n"
        f.write(registro)
        f.close
    except ValueError:
        lblRes.configure(text="ERROR DE ESCRITURA")

def limpar():
    txtCedula.delete(0, 'end')
    txtNombre.delete(0, 'end')
    txtCantidad.delete(0, 'end')
    txtPrecio.delete(0, 'end')

def main():
    leer()
    escribir()
    limpar()

#formulario
#ventana
ventas = tk.Tk()
ventas.iconbitmap("OIP.ico")
ventas.title("Hardware y Servicios - Ventas")
ventas.geometry("500x500")
ventas.resizable(0, 0)

#cedula
lblCedula = tk.Label(ventas, text="Cedula")
lblCedula.grid(pady = 5, row = 0, column = 0)
txtCedula = tk.Entry(ventas)
txtCedula.grid(pady = 5, row = 0, column = 1)

#nombre
lblNombre = tk.Label(ventas, text="Nombre")
lblNombre.grid(pady = 5, row = 1, column = 0)
txtNombre = tk.Entry(ventas)
txtNombre.grid(pady = 5, row = 1, column = 1)

#cantidad
lblCantidad = tk.Label(ventas, text="Cantidad")
lblCantidad.grid(pady = 5, row = 2, column = 0)
txtCantidad = tk.Entry(ventas)
txtCantidad.grid(pady = 5, row = 2, column = 1)

#precio
lblPrecio= tk.Label(ventas, text="Precio x PC")
lblPrecio.grid(pady = 5, row = 3, column = 0)
txtPrecio = tk.Entry(ventas)
txtPrecio.grid(pady = 5, row = 3, column = 1)

#convetir
convertMoneda = tk.IntVar()
radioDolar = tk.Radiobutton(ventas, text="Dolar", variable=convertMoneda, value="1")
radioDolar.grid(pady = 5, row = 4, column = 0)
radioDolar = tk.Radiobutton(ventas, text="Euro", variable=convertMoneda, value="2")
radioDolar.grid(pady = 5, row = 4, column = 1)

#botones
btnEnviar = tk.Button(ventas, text="Enviar", command=main)
btnEnviar.grid(pady = 5, row = 5, column = 0)
btnCancelar= tk.Button(ventas, text="Cancelar")
btnCancelar.grid(pady = 5, row = 5, column = 1)

#resultado
lblTotal= tk.Label(ventas, text="Total")
lblTotal.grid(pady = 5, row = 6, column = 0)
lblRes = tk.Text(ventas, width=25, height=15)
lblRes.grid(pady=5, row=6, column=1)
""" scrollver = tk.Scrollbar(ventas, command=textTotal.yview)
scrollver.grid(row=6, column=2, sticky="nsew")
textTotal.config(yscrollcommand=scrollver.set) """

ventas.mainloop()
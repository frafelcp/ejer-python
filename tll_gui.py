#FELIX CASTRO - TALLER 2 GUI CORTE 2

#inicio
def imprimir(lista, caso):
    if (caso == 1):
       print("----------------------------------------------------------------------")
       print("Compras menores de 5 computadoras")
       for compras in lista:
           cedula = str(compras[0])
           nombre = compras[1]
           cantidadComprada = compras[2]
           print("Cedula:", cedula, "Nombre:", nombre, "\nCantidad:", cantidadComprada)
    elif (caso == 2):
        print("----------------------------------------------------------------------")
        print("Compras mayores e iguales de 5 computadoras y menores de 10 computadores")
        for compras in lista:
           cedula = str(compras[0])
           nombre = compras[1]
           cantidadComprada = compras[2]
           print("Cedula:", cedula, "Nombre:", nombre, "\nCantidad:", cantidadComprada)
    elif (caso == 3):
        print("----------------------------------------------------------------------")
        print("Compras mayores e iguales de 10 computadores")
        for compras in lista:
           cedula = str(compras[0])
           nombre = compras[1]
           cantidadComprada = compras[2]
           print("Cedula:", cedula, "Nombre:", nombre, "\nCantidad:", cantidadComprada)
    else:
        print("Caso no encontrado")

def leer():
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

def escribir():
    f = open("ventaspc.txt", "a")
    print("----------------------------------------------------------------------")
    print("Inserte los datos correspondientes")
    cedula = input("Cédula del cliente:")
    nombre = input("Nombre del cliente:")
    cantidad = input("cantidad de pc:")

    registro = cedula+","+nombre+","+cantidad+"\n"
    f.write(registro)
    f.close

def main():
    salir = False
    while(salir != True):
        print("----------------------------------------------------------------------")
        print("MENU PRINCIPAL")
        print("Selecione una funcion:")
        option = int(input("1.Ver Ventas\n2.Ingresar ventas\n3.Salir\n:"))
        print(option)
        if(option == 1):
            leer()
        elif(option == 2):
            escribir()
        elif(option == 3):
            salir = True
        else:
            print("Opcion no valida")

#main()

import tkinter as tk

ventas = tk.Tk()
ventas.iconbitmap("OIP.ico")
ventas.title("Hardware y Servicios - Ventas")
ventas.geometry("500x500")
ventas.resizable(0, 0)

lblCedula = tk.Label(ventas, text="Cedula")
lblCedula.grid(pady = 5, row = 0, column = 0)

txtCedula = tk.Entry(ventas)
txtCedula.grid(pady = 5, row = 0, column = 1)

lblNombre = tk.Label(ventas, text="Nombre")
lblNombre.grid(pady = 5, row = 1, column = 0)

txtNombre = tk.Entry(ventas)
txtNombre.grid(pady = 5, row = 1, column = 1)

lblCantidad = tk.Label(ventas, text="Cantidad")
lblCantidad.grid(pady = 5, row = 2, column = 0)

txtCantidad = tk.Entry(ventas)
txtCantidad.grid(pady = 5, row = 2, column = 1)

lblPrecio= tk.Label(ventas, text="Precio x PC")
lblPrecio.grid(pady = 5, row = 3, column = 0)

txtPrecio = tk.Entry(ventas)
txtPrecio.grid(pady = 5, row = 3, column = 1)

convertMoneda = tk.IntVar()
radioDolar = tk.Radiobutton(ventas, text="Dolar", variable=convertMoneda, value="1")
radioDolar.grid(pady = 5, row = 4, column = 0)
radioDolar = tk.Radiobutton(ventas, text="Euro", variable=convertMoneda, value="2")
radioDolar.grid(pady = 5, row = 4, column = 1)

btnEnviar = tk.Button(ventas, text="Enviar")
btnEnviar.grid(pady = 5, row = 5, column = 0)
btnCancelar= tk.Button(ventas, text="Cancelar")
btnCancelar.grid(pady = 5, row = 5, column = 1)

lblTotal= tk.Label(ventas, text="Total")
lblTotal.grid(pady = 5, row = 6, column = 0)

textTotal = tk.Text(ventas, width=25, height=15)
textTotal.grid(pady=5, row=6, column=1)
scrollver = tk.Scrollbar(ventas, command=textTotal.yview)
scrollver.grid(row=6, column=2, sticky="nsew")
textTotal.config(yscrollcommand=scrollver.set)

ventas.mainloop()
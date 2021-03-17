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

main()
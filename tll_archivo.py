def imprimir(lista, caso):
    if(caso == 1):
        print("----------------------------------------------------------------------")
        print("Trabajadores con más de 20 años de servicio y 50 o más años de edad")
        for empleado in lista:
            cedula = str(empleado[0])
            nombre = empleado[1]
            print("Cédula:", cedula, "\nEmpleado:", nombre)
    elif(caso == 2):
        print("----------------------------------------------------------------------")
        print("Trabajadores con más de 5 hijos y menos de 10 años de servicio")
        for empleado in lista:
            cedula = str(empleado[0])
            asignacionMensual = float(empleado[4])
            hijos = str(empleado[6])
            print("Cédula:", cedula, "\n# de Hijos: " + hijos +
                  "\n20% de la asignacion mensual:", str(asignacionMensual*20/100))
    elif(caso == 3):
        print("----------------------------------------------------------------------")
        print("Trabajadores con subsido\n# de trabajadores "+str(len(lista)))
        for empleado in lista:
            cedula = str(empleado[0])
            hijos = int(empleado[6])
            print("Cédula:", cedula, "\nValor por pagar: $" + str(hijos*20000))
    else:
        print("Caso no encontrado")


def promedio(lista):
    suma = 0
    for empleado in lista:
        asignacionMensual = float(empleado[4])
        suma = suma + asignacionMensual

    promedio = suma / len(lista)

    print("Promedio de asignacion mensual:", str(promedio))


def leer():
    mas20anios = []
    mas5hijosMenos10anios = []
    subsidioFamiliar = []
    todos = []
    f = open("archivo.txt", "r")

    for linea in f:
        linea = linea.strip()
        linea = linea.split(",")

        todos.append(linea)

        
        edad = int(linea[2])
        aniosServicio = int(linea[3])
        estadoCivil = int(linea[5])
        hijos = int(linea[6])

        if(aniosServicio > 20 and edad >= 50):
            mas20anios.append(linea)

        if(hijos > 5 & aniosServicio < 10):
            mas5hijosMenos10anios.append(linea)

        if(estadoCivil == 1):
            subsidioFamiliar.append(linea)

    # primer parametro de la funcion imprimir es la lista
    # segundo parametro de la funcion imprimir es el caso
    # caso 1
    if(len(mas20anios) != 0):
        imprimir(mas20anios, 1)

    # caso 2
    if(len(mas5hijosMenos10anios) != 0):
        imprimir(mas5hijosMenos10anios, 2)

    # caso 3
    if(len(subsidioFamiliar) != 0):
        imprimir(subsidioFamiliar, 3)

    promedio(todos)


def escribir():
    f = open("archivo.txt", "a")
    print("----------------------------------------------------------------------")
    print("Inserte los datos correspondientes")
    cedula = input("Cédula del trabajador:")
    nombre = input("Nombre del trabajador:")
    edad = input("Edad del trabajador:")
    tiempoServicio = input("Tiempo de servicio del trabajador:")
    asignacionMensual = input("Asignación mensual del trabajador:")
    estadoCivil = input("Estado civil del trabajador\n1.Casado\n2.Soltero\n3.Viudo\n:")
    hijos = input("Numero de hijos del trabajador:")

    registro = cedula+","+nombre+","+edad+","+tiempoServicio+","+asignacionMensual+","+estadoCivil+","+hijos+"\n"
    f.write(registro)
    f.close

def main():
    salir = False
    while(salir != True):
        print("----------------------------------------------------------------------")
        print("MENU PRINCIPAL")
        print("Selecione una funcion:")
        option = int(input("1.Leer\n2.Escribir\n3.Salir\n:"))
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

def registrarCuentas(cuentas):
    #leemos usuario
    user = input("Usuario -x para cortar:")
    while user != "x":
        #leemos contraseña
        passw = input("Ingrese contraseña :")
        #guardamos usuarios y sus contraseñas
        cuentas[0].append(user)
        cuentas[1].append(passw)
        #leemos usuario
        #user = input("Usuario -x para cortar :")
        #retornamos usuarios y contraseñas en una lista de listas
        return cuentas
    
        

def imprimirCuentas(cuentas):
    print(cuentas)


#programa principal
cuentas = [[], []]

while True:
    #menu
    print("1. Insertar usuarios")
    print("2. Usuarios registrados")
    print("3. Iniciar sesion")
    print("4. Salir del programa")

    opcion = int(input("Accion a ejecutar: "))

    if opcion == 1:
        print("INSERTAR NUEVO USUARIOS")
        cuentas = registrarCuentas(cuentas)
    elif opcion == 2:
        print("USUARIOS REGISTRADOS")
        cuentas = imprimirCuentas(cuentas)
    elif opcion == 3:
        print("INICIAR SESION")
    elif opcion == 4:
        print("SALIR DEL PROGRAMA")
        break
    else:
        print("Opcion invalida")

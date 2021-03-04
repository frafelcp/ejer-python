def registrar(cuentas):
    #leemos usuario
    user = input("Usuario -x para cortar:")
    #leemos contraseña
    passw = input("Ingrese contraseña :")
    #guardamos usuarios y sus contraseñas
    cuentas[0].append(user)
    cuentas[1].append(passw)
    #retornamos usuarios y contraseñas en una lista de listas
    return cuentas
    
        

def imprimirCuentas(cuentas):
    for row in cuentas:
        for elem in row:
            print(elem, end=' ')
        print() 


#programa principal
#lista bidimimensional que almacenara los usuarios y contraseñas
cuentas = [[], []]

while True:
    #menu principal
    print("****************************")
    print("MENU PRINCIPAL")
    print("1. REGISTRARSE")
    print("2. INICIAR SESION")
    print("3. CERRAR")

    #escogemos una opcion del menu principal
    opcion = int(input("Accion a ejecutar: "))

    if opcion == 1:
        #menu registro de usuarios
        print("++++++++++++++++++++++++++++++")
        print("MENU REGISTRO DE USUARIO")
        while True:
            print("REGISTRO")
            print("1. REGISTRAR USUARIO")
            print("2. REGRESAR")

            #escogemos una opcion del menu principal registrar
            opcionRegistrar = int(input("Accion a ejecutar: "))

            if opcionRegistrar == 1:
                cuentas = registrar(cuentas)
            elif opcionRegistrar == 2:
                print("REGRESAR A MENU PRINCIPAL")
                break
            else:
                print("Opcion invalida")
    elif opcion == 2:
        print("INICIAR SESION")
        cuentas = imprimirCuentas(cuentas)
    elif opcion == 3:
        print("SALIR DEL PROGRAMA")
        break
    else:
        print("Opcion invalida")

#Ingresar una serie de valores
#almacenar los valores en un vector
#sumar los valores pares e impares por separados

salir = False

while not salir:
    print("MENU PRINCIPAL")
    print("------------------------------------")
    print ("1. Ingresar valores")
    print ("2. Mostrar valores")
    print ("3. Sumar valores")
    print ("4. Salir")

    print ("Elige una opcion")

    num = int(input("Introduce tu opcion: "))

    if num == 1:
        print("------------------------------------")
        print ("INGRESAR VALORES Y GUARDARLOS")
        nNum = int(input("Ingrese cuantos de valores se digitaran: "))
        valores = []
        for i in range(nNum):
            valores.append(int(input("Ingrese un valor: ")))
        
    elif num == 2:
        print("------------------------------------")
        print ("MOSTRAR VALORES")
        print(valores)
    elif num == 3:
        print("------------------------------------")
        print("SUMAR VALORES")
        sumPar = 0
        sumImpar = 0
        for i in valores:
            if i%2==0:
                sumPar = sumPar + i
            else:
                sumImpar = sumImpar + i
        print("La suma Par: ", sumPar)
        print("La suma impar: ", sumImpar)
        
    elif num == 4:
        salir = True
    else:
        print("------------------------------------")
        print ("Introduce un numero entre 1 y 3")

print("FIN DEL PROGRAMA")

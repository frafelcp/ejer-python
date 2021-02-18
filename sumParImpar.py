
n = 1
while n != 0 :
    op = input("escoja entre las opciones"+'\n'+"1) Uno"+'\n'+"2) Dos"+'\n'+"0) Salir"+'\n')
    print(op)
    if op == "1":
         lista = []
         nu_valores = int(input("ingese la cantidad de valores que desea ingresar "+'\n'))
         for x in range(nu_valores):
             aux = int(input("ingese un numero : "))
             lista.append(aux)
             print(lista)
         aux_for = 0
         suma_par =0
         suma_in =0
         for x in lista:
             aux_for=aux_for+1
             if ((aux_for % 2) == 0):
                 suma_par = suma_par +x
                
             else:
                 suma_in = suma_in +x
         print("La suma de los pares es: ",suma_par)
         print("La suma de los impares es: ",suma_in)    
    

    else:

        if op == "2":
            print("2")
        else:
            if op == "0":
                n = 0    
             
    
    
        

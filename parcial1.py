def agregarArticulos(articulos):
    nombArticulo = input("Articulo -x para cortar: ")
    while nombArticulo != "x":
        codAr = int(input("ID: "))
        existencia = int(input("Cantidad: "))
        articulos.append((nombArticulo,codAr,existencia))
        nombArticulo=input("Articulo -x para cortar: ")
        return articulos

def mostrarArticulos(articulos):
    for i in articulos:
        print(i)

def ingresarVenta(articulos):
    codP=int(input("Codigo producto vendido: "))
    cantP=int(input("Cantidad vendida: "))
    for i in len(articulos):
        if articulos[1] == codP:
            articulos[2] = articulos[2 - cantP]
            return articulos

#programa principal
articulos=[]
while True:
    print("1. Agregar articulos")
    print("2. Mostrar articulos")
    print("3. Ingresar ventas")
    print("3. No aplica")
    print("3. No aplica")
    print("3. No aplica")
    print("7. Salir del programa")
    
    opcion=int(input("Acción a ejecutar: "))
    
    if opcion==1:
        print("AGREGAR ARTICULOS")
        articulos=agregarArticulos(articulos)
    elif opcion==2:
        print("MOSTRAR ARTICULOS")
        mostrarArticulos(articulos)
    elif opcion==3:
        print("INGRESAR VENTAS")
        articulos=ingresarVenta(articulos)
    elif opcion==4:
        print("NO APLICA")
    elif opcion==5:
        print("NO APLICA")
    elif opcion==6:
        print("NO APLICA")
    elif opcion==7:
        break
    else:
        print("Opción inválida")


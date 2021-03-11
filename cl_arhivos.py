def abrirEscribir():    
    #leemos usuario
    archivo = open("archivo.txt", "w") #metod para abrir el archivo
    #escribimos en el archivo
    frase = "Felix Castro estudiante de cuarto cuatrimestre de Tecnico Profesional en Sistemas Informatico"
    archivo.write(frase) #metodo para escribir en el archivo
    #cerramos la edicion del archivo
    archivo.close() #metodo para cerrar archivo

def abrirLeer():
    #abrir y leer archivo linea por linea
    archivoF = open("archivo.txt", "r")
    lineas = archivoF.readlines()
    archivoF.close()
    print(lineas)

def addArchivo():
    archivoAdd = open("archivo.txt", "a")
    archivoAdd.write("\nestas es otra linea")
    leer = abrirLeer()


print("-------------------------------")
escribir = abrirEscribir()
print("-------------------------------")
read = abrirLeer()
print("-------------------------------")
agregar = addArchivo()
print("-------------------------------")
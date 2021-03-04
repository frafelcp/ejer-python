from io import open

def openFile():
    text=open("file1.txt","w")
    f="Bienvenidos"
    text.write(f)
    f="Linea 1"
    text.write(f)
    text.close()

def viewFile():
    text=open("file1.txt","r")
    line_text=text.readlines()
    print(line_text)
    text.close()

def addFile():
    text=open("file1.txt","a")
    f="\nLinea2\nLinea3"
    text.write(f)

def fileExercise ():
    text = open ("file1.txt","w");
    nombre =" Datos del Nombre "
    telefono =" Datos del Telefono"
    direccion =" Datos de la Direccion"
    print (nombre)
    print (telefono)
    print (direccion)
    text.write(nombre)
    text.close()
    iniciar= False
    while iniciar ==False:
        text = open ("file1.txt","w")
        data = input (' Por Favor Digite su Nombre: ')
        text.write(data)
        text.write(",")
        text.write("\n ")
        text.close()
        text = open ("file1.txt","w")
        data = input (' Por Favor Digite su Telefono: ')
        text.write(data)
        text.write(",")
        text.write("\n ")
        text.close()
        text = open ("file1.txt","w")
        data = input (' Por Favor Digite su Direccion: ')
        text.write(data)
        text.write(",")
        text.write("\n ")
        text.close()
        
        
        
#openFile()
fileExercise()
viewFile()
addFile()
viewFile()

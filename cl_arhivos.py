#leemos usuario
archivo = open("archivo.txt", "w") #metod para abrir el archivo
#escribimos en el archivo
frase = "Felix Castro estudiante de cuarto cuatrimestre de Tecnico Profesional en Sistemas Informatico"
archivo.write(frase) #metodo para escribir en el archivo
#cerramos la edicion del archivo
archivo.close() #metodo para cerrar archivo
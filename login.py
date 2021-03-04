def ingresarUsuarios(usuarios):
  usuario = input("Usuario -x para cortar :")
  while usuario != "x":
    contrasena = input("Ingrese contraseña: ")
    usuarios.append(usuario, contrasena)
    usuario = input("Usuario -x para cortar :")
    return usuarios

""" def iniciarSesion(usuarios):
  usu = input("Usuario: ")
  cont = input("Contrasena")
  user = validarUsuario(usuarios, usu)
  contra = validarPass(usuarios, user) """

# def validarUsuario(usuarios, usu):
  

#programa principal
usuarios=[]
while True:
  print("1. Ingresar usuarios")
  print("2. Iniciar sesion")
  print("3. Salir del programa")

  opcion=int(input("Acción a ejecutar: "))

  if opcion == 1:
    print("INGRESAR USUARIOS")
    usuarios = ingresarUsuarios(usuarios)
  elif opcion == 2:
    print("INICIAR SESION")
  elif opcion == 3:
    break
  else:
    print("Opción inválida")
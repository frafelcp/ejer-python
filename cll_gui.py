import tkinter as tk

def escribir():
    try:
        f = open("areas.txt", "a")
        dni = entId.get()
        alumno = entEstudiante.get()

        registro = dni+","+alumno+"\n"
        f.write(registro)
        f.close
    except ValueError:
        lblArea.configure(text="Error de archivo")

def leer():
    todos = []
    f = open("areas.txt", "r")

    for linea in f:
       linea = linea.strip()
       linea = linea.split(",")

       todos.append(linea)

    if (len(todos) != 0):
        imprimir(todos)
    
    #area()

def imprimir(lista):
    try:
        for ventas in lista:
            ide = str(ventas[0])
            nombre = ventas[1]
            base = int(entBase.get())
            altura = int(entAltura.get())
            ar = (base * altura)#area
            res = "ID:", ide, "Nombre:", nombre, "Area:", ar
            lblArea.configure(text="El area es ")
            lblResp.configure(text=res)
            #print("ID:", ide, "Nombre:", nombre, "\nArea:", ar)
            lblArea
    except ValueError:
        lblArea.configure(text="VERIFICAR DATOS")
            
def main():
    leer()
    escribir()
    limpar()

def limpar():
    entId.delete(0, 'end')
    entEstudiante.delete(0, 'end')
    entBase.delete(0, 'end')
    entAltura.delete(0, 'end')

ventana = tk.Tk()
ventana.title("CALCULADORA GEOMETRICA")
ventana.geometry("500x500")
ventana.resizable(0, 0)

lblId = tk.Label(ventana, text="ID")
lblId.grid(pady=5, padx=5, row=0, column=0)
entId = tk.Entry(ventana)
entId.grid(pady=5, row=0, column=1)

lblEstudiantes = tk.Label(ventana, text="ESTUDIANTE")
lblEstudiantes.grid(pady=10, padx=10, row=0, column=2)
entEstudiante = tk.Entry(ventana)
entEstudiante.grid(pady=10, padx=10, row=0, column=3)

lblBase = tk.Label(ventana, text="BASE")
lblBase.grid(pady=5, padx=5, row=2, column=0)
entBase = tk.Entry(ventana)
entBase.grid(pady=5, row=2, column=1)

lblAltura = tk.Label(ventana, text="ALTURA")
lblAltura.grid(pady=10, padx=10, row=1, column=2)
entAltura = tk.Entry(ventana)
entAltura.grid(pady=11, padx=10, row=1, column=3)

btnCalcular = tk.Button(ventana, text="Enviar", command=main)
btnCalcular.grid(pady=5, padx=5, row=3, column=0)
btnCancelar = tk.Button(ventana, text="Cancelar")
btnCancelar.grid(pady=5, padx=5, row=3, column=1)

lblArea = tk.Label(ventana, text="The area in cm2 is ")
lblArea.grid(pady=5, padx=5, row=4, column=0)

lblResp = tk.Label(ventana, text=": ")
lblResp.grid(pady=5, padx=5, row=4, column=1)

ventana.mainloop()
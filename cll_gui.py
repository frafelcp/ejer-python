import tkinter as tk

def area():
    try:
        base = int(entBase.get())
        altura = int(entAltura.get())
        ar = (base * altura)
        lblArea.configure(text="El area en cm2 es ")
        lblResp.configure(text=ar)
    except ValueError:
        lblArea.configure(text="VERIFICAR DATOS")

ventana = tk.Tk()
ventana.title("Hola mundo")
ventana.geometry("300x150")
ventana.resizable(0, 0)

lblBase = tk.Label(ventana, text="Base")
lblBase.grid(pady=5, padx=5, row=0, column=0)
entBase = tk.Entry(ventana)
entBase.grid(pady=5, row=0, column=1)

lblAltura = tk.Label(ventana, text="Altura")
lblAltura.grid(pady=5, padx=5, row=1, column=0)
entAltura = tk.Entry(ventana)
entAltura.grid(pady=5, row=1, column=1)

btnCalcular = tk.Button(ventana, text="Enviar", command=area)
btnCalcular.grid(pady=5, padx=5, row=2, column=0)
btnCancelar = tk.Button(ventana, text="Cancelar")
btnCancelar.grid(pady=5, padx=5, row=2, column=1)

lblArea = tk.Label(ventana, text="The area in cm2 is ")
lblArea.grid(pady=5, padx=5, row=3, column=0)

lblResp = tk.Label(ventana, text=": ")
lblResp.grid(pady=5, padx=5, row=3, column=1)

ventana.mainloop()
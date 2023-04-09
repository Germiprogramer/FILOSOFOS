from tkinter import Tk, Label, Button, Entry, Text
import tkinter as tk


class VentanaEjemplo:

    def __init__(self, master):

        self.master = master
        master.title("Una simple interfaz gráfica")

        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()

        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()

        self.botonCerrar = Button(master, text="Cerrar", font = "arial" , fg="green", command=master.quit)
        self.botonCerrar.pack()

        self.entradatexto = Entry(master, width=50, bg="blue")
        self.entradatexto.pack()
        
        self.texto = Text(master, height=2, pady=5)
        self.texto.insert( "Filosofo 1")
        self.texto.pack()

        self.texto = Text(master, width=50)
        self.texto.insert(tk.END, "Filosofo 2")
        self.texto.pack()

        self.texto = Text(master, width=50)
        self.texto.insert(tk.END, "Filosofo 3")
        self.texto.pack()

        self.texto = Text(master, width=50)
        self.texto.insert(tk.END, "Filosofo 4")
        self.texto.pack()

        self.texto = Text(master, width=50)
        self.texto.insert(tk.END, "Filosofo 5")
        self.texto.pack()

    def saludar(self):
        print("¡Hey!")

root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()
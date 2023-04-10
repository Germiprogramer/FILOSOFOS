import threading
import tkinter as tk
import time
import random

class Filosofo:

    def __init__(self, nombre, palilloizq, palilloder, interfaz, x, y):

        self.nombre = nombre
        self.palilloizq = palilloizq
        self.palilloder = palilloder
        self.interfaz = interfaz
        self.x = x
        self.y = y
        self.estado = "Pensando"
        self.estado_label = tk.Label(self.interfaz, text=f"(self.nombre) : {self.estado}")
        self.estado_label.place(x=self.x, y=self.y)
        self.num_comidas = 0
        self.num_comidas_label = tk.Label(self.interfaz, text=f"Comidas: {self.num_comidas}")
        self.num_comidas_label.place(x = self.x + 580, y = self.y)

    def pensar(self):
        self.estado = "Pensando"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")
        time.sleep(random.uniform(1,5))

    def intentar_obtener_palillo(self, palillo):
        palillo.acquire()
        self.estado = f"Obtuvo {palillo}"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")

    def obtener_palillos(self):
        #primero intenta obtener el palillo izquierdo
        self.estado = "Intentando obtener palillo izquierdo"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")
        self.intentar_obtener_palillo(self.palilloizq)
        #luego intenta obtener el palillo derecho
        self.estado = "Intentando obtener palillo derecho"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")
        self.intentar_obtener_palillo(self.palilloder)

    def comer(self):
        self.estado = "Comiendo"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")
        self.obtener_palillos()
        self.palilloizq.release()
        self.palilloder.release()
        time.sleep(2)
        self.estado = "Ha terminado de comer"
        self.estado_label.config(text=f"(self.nombre) : {self.estado}")
        self.num_comidas += 1
        self.num_comidas_label.config(text=f"Comidas: {self.num_comidas}")
        time.sleep(random.uniform(1,5))

    def ciclo_vida(self):
        while True:
            self.pensar()
            self.comer()
            self.estado = f"Ha terminado de comer {self.num_comidas} veces"
            self.estado_label.config(text=f"(self.nombre) : {self.estado}")

class Interfaz:

    def __init__(self):
        self.raiz=tk.Tk()
        self.raiz.geometry("800x600")
        self.raiz.title("Cena de los Filósofos")
        self.palillos= [threading.Lock() for _ in range(5)]
        self.filosofos=[Filosofo("Filósofo"+str(i+1), self.palillos[i], self.palillos[(i+1)%5], self.raiz, 50, 50+50*i) for i in range(5)]
        self.etiquetas_comidas = [tk.Label(self.raiz, text=f"{f.nombre}: 0 comidas") for f in self.filosofos]
        for i, f in enumerate(self.filosofos):
                threading.Thread(target=self.iniciar, args=(f, self.etiquetas_comidas[i])).start()
      
        self.raiz.mainloop()
    
    def iniciar(self,filosofo,etiqueta_comidas):
      while True:
         filosofo.pensar()
         filosofo.comer()
         comidas=filosofo.num_comidas
         etiqueta_comidas.config(text=f"{filosofo.nombre}: {comidas} comidas")
         filosofo.estado=f"{comidas} comidas"
         filosofo.estado_label.config(text=f"{filosofo.nombre} : {filosofo.estado}")

    
if __name__=="__main__":
   Interfaz()


    

    


    



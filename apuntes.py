Para cambiar el color de un widget en tkinter, podemos utilizar la función `configure` junto con el parámetro `bg` para cambiar el color de fondo del widget. A continuación te presento un código de ejemplo que te permitirá cambiar el color de un botón en tkinter:

```python
import tkinter as tk

def cambiar_color(widget, color):
widget.configure(bg=color)

ventana = tk.Tk()
ventana.geometry("200x200")

# creamos un botón
boton = tk.Button(ventana, text="Cambiar color", command=lambda:cambiar_color(boton, "red"))
boton.pack()

ventana.mainloop()
```

En este código, definimos una función llamada `cambiar_color` que recibe dos parámetros: el widget al que queremos cambiar el color y el color que queremos utilizar. Utilizamos el método `configure` del widget para cambiar su color de fondo (`bg`) al color especificado.

Luego, creamos una ventana en tkinter y agregamos un botón que llama a la función `cambiar_color` cuando se hace clic en él. Al hacer clic en el botón, el color de fondo del mismo se cambia a rojo.

Puedes modificar el código para adaptarlo a tus necesidades cambiando el tipo de widget y los colores que deseas utilizar
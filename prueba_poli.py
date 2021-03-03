
# crear el archivo cvs (coordenadas)
# llamar al visual code
# primer paso definir la ventana
# cantidad de puntos
# construye for
# dibujar
# imprimir

import pandas as pd
import os


from turtle import *
mitortuga = Turtle()
mis_datos_poligonal_x = [300, 500, 500,-300,-500,200,500,300]
mis_datos_poligonal_y = [100, 350, -100,200,-500,-400,-200,100]

mitortuga.setup(600, 600,0, 0)
mitortuga.setposition(mis_datos_poligonal_x[0], mis_datos_poligonal_y[0])
for i in range(7):
    goto(mis_datos_poligonal_x[i], mis_datos_poligonal_y[i])


mitortuga.hideturtle()
mainloop()
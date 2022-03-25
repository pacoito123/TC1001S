"""
Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

import math


cache = {} # Para 'memoization'.


def line(start, end): #Funcion Linea crea una linea del punto inicial al punto final
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end): #Funcion cuadrado crea un cuadrado del punto inicial al punto final en los ejes x & y
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    dist = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    theta = math.degrees(math.atan2(end.y - start.y, end.x - start.x))
    setheading(theta)

    for _ in range(4):
        forward(dist)

        if abs(theta) >= 90:
            left(90)
        else:
            right(90)

    end_fill()
    setheading(0)


def cube(start, end): #Funcion cubo traza un cubo a traves del trazo de un cuadrado
    up()
    goto(start.x, start.y) # Comenzar a trazar en la posición inicial.
    down()

    dist = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2) # Obtener distancia entre los dos puntos.
    theta = math.degrees(math.atan2(end.y - start.y, end.x - start.x)) # Obtener ángulo entre los dos puntos.
    direccion = -1 if abs(theta) >= 90 else 1 # Determinar dirección del trazado.

    setheading(theta)

    for _ in range(4): # Trazar cuadrado inicial.
        forward(dist)
        right(90 * direccion)

    left(45 * direccion)
    forward(dist / 2.0) # Conectar primera vértice.
    right(45 * direccion)

    for _ in range(4):
        curr = heading()
        forward(dist) # Trazar siguiente lado.

        setheading(theta - 135 * direccion)
        forward(dist / 2.0) # Conectar siguiente vértice.
        forward(-dist / 2.0)
        setheading(curr - 90 * direccion)

    setheading(0)


def circle(start, end): #Funcion circulo crea un circulo a traves de los puntos dados
    """Draw circle from start to end."""
    up()

    mid = vector((start.x + end.x) / 2.0, (start.y + end.y) / 2.0) # Obtener punto medio.
    radius = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2) / 2.0 # Calcular radio.

    goto(radius + mid.x, mid.y) # Comenzar a trazar en la primera posición.

    down()
    begin_fill()

    for i in range(1, 360, 10):
        if i not in cache.keys(): # 'Memoization' para funciones trigonométricas.
            cache[i] = [math.cos(math.radians(i)), math.sin(math.radians(i))]

        goto(radius * cache[i][0] + mid.x, radius * cache[i][1] + mid.y) # Ir a la siguiente posición.

    end_fill()


"""
    Se usó el mismo concepto que en la función 'cuadrado()', solo que cada número avanza a una
    distancia diferente (Δx o Δy) dependiendo si es par o impar.
"""
def rectangle(start, end): #Funcion rectangulo crea un rectangulo con giros en los puntos x & y
    """Draw rectangle from start to end."""
    up()

    goto(start.x, start.y)

    down()
    begin_fill()

    for i in range(4):
        if i % 2 == 0:
            forward(end.x - start.x)
            left(90)
        else:
            forward((end.y - start.y))
            left(90)

    end_fill()


def triangle(start, end): #Funcion triangulo tiene un fucionamiento parecido a rectangulo pero con 3 lados y otro angulo
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    dist = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    theta = math.degrees(math.atan2(end.y - start.y, end.x - start.x))
    setheading(theta)

    for _ in range(3):
        forward(dist)

        if abs(theta) >= 90:
            left(120)
        else:
            right(120)

    end_fill()
    setheading(0)


def tap(x, y): #Funcion tap es la que crea los puntos
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value): #Funcion store es la que almacena los valores
    """Store value in state at key."""
    state[key] = value

title("Equipo 6: Act 1 - paint.py") # Nombre de la ventana
speed(10000) # Velocidad del cursor.

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('pink'), 'P') # Agregamos color de la lista de colores del programa.
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', cube), 'C') # Agregamos función para trazar un cubo.
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

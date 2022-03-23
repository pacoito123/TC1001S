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


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
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


def circle(start, end):
    """Draw circle from start to end."""
    up()

    mid = vector((start.x + end.x) / 2.0, (start.y + end.y) / 2.0) # Obtener punto medio.
    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2) / 2.0 # Calcular radio.

    goto(radius + mid.x, mid.y) # Comenzar a trazar en la primera posición.

    down()
    begin_fill()

    for i in range(1, 360):
        if i not in cache.keys(): # 'Memoization' para funciones trigonométricas.
            cache[i] = [math.cos(math.radians(i)), math.sin(math.radians(i))]

        goto(radius * cache[i][0] + mid.x, radius * cache[i][1] + mid.y) # Ir a la siguiente posición.

    end_fill()


"""
    Se usó el mismo concepto que en la función 'cuadrado()', solo que cada número avanza a una
    distancia diferente (Δx o Δy) dependiendo si es par o impar.
"""
def rectangle(start, end):
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


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value

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
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

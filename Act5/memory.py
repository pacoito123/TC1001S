"""
Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

import math


# Se implementó esta constante para cambiar el número de casillas.
num_tiles = 8 # TODO: Arreglar con números impares.

car = path('car.gif')
tiles = list(range(math.ceil(num_tiles**2 / 2.0))) * 2
state = {'mark': None}
hide = [True] * (num_tiles**2)

# Contador(es)
counter_turtle = Turtle() # Crear instancia nueva de 'Turtle()'.
counter = counter_last = 0 # Inicializar en 0.
# ...


def square(x, y): #Funcion que genera el tablero
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y): #Funcion indez que convierte coordenadas en casillas
    """Convert (x, y) coordinates to tiles index."""
    half = num_tiles / 2.0 # Calcular la mitad del número de casillas.
    return int((x + (50 * half)) // 50 + ((y + (50 * half)) // 50) * num_tiles)


def xy(count): #Convierte casillas en coodenadas
    """Convert tiles count to (x, y) coordinates."""
    half = num_tiles / 2.0 # Calcular la mitad del número de casillas.
    return (count % num_tiles) * 50 - (50 * half), (count // num_tiles) * 50 - (50 * half)


def tap(x, y): #Funcion que permite la respuesta al dar los clicks
    """Update mark and hidden tiles based on tap."""
    half = num_tiles / 2.0 # Calcular la mitad del número de casillas.
    if x > 50 * half or x < -50 * half or y > 50 * half or y < -50 * half:
        return # Ignorar 'taps' fuera de la cuadrícula.

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # TODO: Añadir condición de salida cuando se agoten los números.

    global counter
    counter += 1 # Aumentar contador de 'taps'.


def draw(): #Funcion draw que dibuja los objetos
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(num_tiles**2):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y) # Se cambió de '+ 2' a '+ 25' para alinear valor al centro.
        color((tiles[mark] * 10 % 255, 128, tiles[mark] * 10 % 255))

        print(tiles[mark] * 10 % 255, ", ", 128, ", ", tiles[mark] * 10 % 255)
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center') # Se añadió 'align' para alinear valor al centro.

    update()
    updateCounter() # Actualizar contador.
    ontimer(draw, 100)


"""
    Función para actualizar el contador de taps.

    Se utilizó otra instancia de la clase 'Turtle()' para evitar el parpadeo del número a causa
    de la tortuga original teniendo que ir al otro lado de la ventana para desplegar el número.
"""
def updateCounter(): #Funcion que genera el contador
    global counter_last

    if counter != counter_last: # Para únicamente desplegar el contador cuando haya un cambio.
        counter_turtle.clear() # Limpiar pantalla.
        counter_turtle.write('Taps: ' + str(counter), font=('Arial', 30, 'normal')) # Desplegar 'taps'.

        counter_last = counter # Actualizar último valor del contador.


# Configuración de tortuga para contador:
counter_turtle.hideturtle()
counter_turtle.up()
counter_turtle.goto(-50 * (num_tiles / 2.0 + 1), -50 * (num_tiles / 2.0 + 1))
counter_turtle.down()
# ...

colormode(255) # Cambiar color a 0-255, en lugar de 0..1 (por default).

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
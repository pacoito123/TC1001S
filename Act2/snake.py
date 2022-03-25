"""
Snake, classic arcade game.

Exercises

1. Comida con color al azar.
2. Serpiente con color al azar.
3. La comida puede moverse.
"""

from turtle import *
from freegames import square, vector

import random


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# creamos una lista de colores en donde no esta el rojo
colors = ["yellow", "pink", "orange", "black", "blue", "green"]

# asignamos un calor aleatorio a las variables para el color del cuerpo y comida
body_color = random.choice(colors)
food_color = random.choice(colors)

# para evitar que los colores sean iguales, iniciamos un ciclo while que
# funciona mientras que ambos colores sean iguales, y termina hasta que estos son distintos
while body_color == food_color:
    food_color = random.choice(colors)

skip_move = 0 # Contador para movimiento de la comida.
lock_move = False # Para sólo registrar un input a la vez.
pause = False # Para pausar el juego.


# Función para trazar el borde del juego.
def draw_borders():
    up()
    goto(-200, 200)
    down()

    for _ in range(4):
        forward(400)
        right(90)


def change(x, y): #Funcion change que genera el cambio del curso de la serpiente
    "Change snake direction."
    global lock_move
    if lock_move or aim.x == -x or aim.y == -y: # Ignorar inputs de 'reversa'.
        return

    # Ajustar camino de la serpiente.
    aim.x = x
    aim.y = y

    lock_move = True # Tomar sólo un input hasta que la serpiente se mueva.


def inside(head): # Función inside que valida que la cabeza este dentro del tablero.
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def inside_food(food): # Función inside que valida que la comida esté dentro del tablero.
    return -200 < food.x < 190 and -200 < food.y < 190


def move(): # Funcion move que genera el movimiento de la serpiente y la comida.
    "Move snake forward one segment."

    if pause: # Condición para pausar el juego.
        ontimer(move, 75) # Seguir leyendo inputs, para continuar jugando.
        return

    head = snake[-1].copy()
    head.move(aim)

    # Calcular movimiento de comida.
    global skip_move
    if skip_move < 4: # Saltar cada cuatro iteraciones (la comida se mueve a 1/4 velocidad).
        skip_move += 1
    else:
        # damos las distintas opciones de movimiento a la comida
        options = [vector(10, 0),
                   vector(-10, 0),
                   vector(0, 10),
                   vector(0, -10),
                   vector(0, 0)]

        # elige una opcion aleatoria de estas 5, que son arriba, abajo, izquierda, derecha y esperar
        plan = random.choice(options)

        food.move(plan) # Mover comida de acuerdo al plan.
        skip_move = 0 # Resetear contador.

    # si la comida se sale del limite es teletransportada dentro del mismo
    if not inside_food(food):
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake: ', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    draw_borders()

    for body in snake:
        square(body.x, body.y, 9, body_color) # asignamos el color aleatorio al cuerpo

    square(food.x, food.y, 9, food_color) # asignamos el color aleatorio a la comida

    update()
    ontimer(move, 75)

    global lock_move
    lock_move = False # Permitir otro input.


def toggle_pause(): # Función para pausar el juego o continuar jugando.
    global pause
    pause = not pause # Cambiar estado de pausa.


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: toggle_pause(), 'p') # Pausar/continuar jugando.
onkey(lambda: exit(), 'q') # Salir del programa.
move()
done()

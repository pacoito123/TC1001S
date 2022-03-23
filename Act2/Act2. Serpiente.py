"""
Paint, for drawing shapes.

Exercises

1. Comida con color al azar.
2. Serpiente con color al azar.
3. La comida puede moverse.
"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
##creamos una lista de colores en donde no esta el rojo
colors = ["yellow", "pink","orange","black","blue","green"]




##asignamos un calor aleatorio a las variables para el color del cuerpo y comida
body_color = random.choice(colors)
food_color = random.choice(colors)
##para evitar que los colores sean iguales, iniciamos un ciclo while que
##funciona mientras que ambos colores sean iguales, y termina hasta que estos son distintos
while body_color == food_color:
    food_color = random.choice(colors)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
def inside_food(food):
    return -200 < food.x < 190 and -200 < food.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    ##damos las distintas opciones de movimiento a la comida
    options = [vector(10, 0),
               vector(-10, 0),
               vector(0, 10),
               vector(0, -10),]
    ##elige una opcion aleatoria de estas 4, que son arriba, abajo, izquierda y derecha
    plan = random.choice(options)
    ##hace el movimiento
    food.move(plan)
    
    ##si la comida se sale del limite es teletransportada dentro del mismo
    if not inside_food(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, body_color  )##asignamos el color aleatorio al cuerpo
        
    square(food.x, food.y, 9,food_color )##asignamos el color aleatorio a la comida
    
    
        



    update()
    ontimer(move, 100)
    

    
    

    
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
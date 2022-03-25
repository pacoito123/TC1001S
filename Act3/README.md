# Actividad 3 - pacman.py

> Herramientas computacionales: el arte de la programación

Programa sencillo para simular el juego de Pacman, cambiamos el mapa, la velocidad de los fantasmas y la forma en que los fantasmas buscan al usuario '[turtle, random](https://docs.python.org/3/library/turtle.html)'.

## Controles
*Mover a Pacman:*
* **[↑]** - Mover arriba
* **[↓]** - Mover abajo
* **[←]** - Mover a la izquierda
* **[→]** - Mover a la derecha

[========]

*Juego:*
* **[p]** - Pausar/continuar juego
* **[q]** - Salir del juego

## Nuevas Funciones
* **Creación del mapa con un nuevo camino:**
```python
tiles = [1,0,1,0,1,0]
```
* **Incremento en la velocidad de los fantasmas:**
```python
options = [
	vector(10, 0),
	vector(-10, 0),
	vector(0, 10),
	vector(0, -10),
]
```
* **Decisión de movimiento de los fantasmas:**
```python
plan = choice(options)
```
* **Movimiento de los fantasmas:**
```python
if valid(point + course, 0):
	point.move(course)
```
* **Permitir inputs menos precisos:**
```python
# método change()
if valid(pacman + vector(x, y), 20):
        new_aim.x = x
        new_aim.y = y
# método move()
if not aim == new_aim and valid(pacman + new_aim, 0):
        aim.x = new_aim.x
        aim.y = new_aim.y
        pacman.move(aim)
```
* **Mostrar total de puntos a obtener:**
```python
total_tiles = sum(tiles)
```

[========]

## Autores

- **Cesar Hernandez** - [Zzar012345](https://github.com/Zzar012345)
- **Guillermo Garrido** - [Rockking01](https://github.com/Rockking01)
- **Francisco Rubio (A01284502)** - [pacoito123](https://github.com/pacoito123)
- **Genaro Rivero (A00833638)** - [Alponcho6594](https://github.com/Alponcho6594)

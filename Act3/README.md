# Actividad 3 - pacman.py

> Herramientas computacionales: el arte de la programación

Programa sencillo para simular el juego de Pacman, cambiamos el mapa, la velocidad de los fantasmas y la forma en que los fantasmas buscan al usuario '[turtle, random](https://docs.python.org/3/library/turtle.html)'.

## Controladores

*Nuevas Funciones:*
* **[tiles = [1,0,1,0,1,0]]** - Creación del mapa con un nuevo camino
* **[options = [**
                **vector(20, 0),**
                **vector(-20, 0),**
                **vector(0, 20),**
                **vector(0, -20),]** - Incremento en la velocidad
* **[plan = choice(options)]** - Cambio de posiciones más rapido
* **[if valid(point + course):**
            **point.move(course)]** - Fantasmas buscando al jugador

[========]

## Autores

- **Cesar Hernandez** - [Zzar012345](https://github.com/Zzar012345)
- **Guillermo Garrido** - [Rockking01](https://github.com/Rockking01)
- **Francisco Rubio (A01284502)** - [pacoito123](https://github.com/pacoito123)
- **Genaro Rivero (A00833638)** - [Alponcho6594](https://github.com/Alponcho6594)

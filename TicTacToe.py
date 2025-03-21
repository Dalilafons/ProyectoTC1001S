import turtle  # Gráficos con turtle
from freegames import line  # Dibujo de líneas


def grid():
    """Dibuja la cuadrícula del juego."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior


def drawx(x, y):
    """Dibuja una X morada y centrada."""
    turtle.color("purple")  # Color morado
    turtle.width(8)         # Grosor de línea
    offset = 30             # Espaciado para centrar la X

    line(x + offset, y + offset, x + 133 - offset, y + 133 - offset)
    line(x + offset, y + 133 - offset, x + 133 - offset, y + offset)


def drawo(x, y):
    """Dibuja una O rosa y centrada."""
    turtle.color("pink")  # Color rosa
    turtle.width(8)       # Grosor de línea

    turtle.up()
    turtle.goto(x + 67, y + 10)  # Centro ajustado
    turtle.down()
    turtle.circle(57)  # Tamaño ajustado para encajar en la casilla


def floor(value):
    """Redondea al tamaño de casilla."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}          # Jugador actual (0 = X, 1 = O)
players = [drawx, drawo]       # Lista de funciones


def tap(x, y):
    """Dibuja X u O donde se hace clic."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    turtle.update()
    state['player'] = not player  # Cambia de jugador


turtle.setup(420, 420, 370, 0)     # Tamaño de ventana
turtle.hideturtle()               # Oculta la flecha
turtle.tracer(False)             # Dibujo más rápido
grid()                           # Dibuja la cuadrícula
turtle.update()                  # Refresca pantalla
turtle.onscreenclick(tap)        # Clic para jugar
turtle.done()                    # Mantiene la ventana abierta

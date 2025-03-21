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
board = {}                     # Casillas ocupadas

# Crear un turtle para mostrar mensajes
msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.goto(0, -190)  # Posición baja de la pantalla


def mostrar_mensaje(texto):
    """Muestra un mensaje en pantalla y lo borra después."""
    msg.clear()
    msg.write(texto, align="center", font=("Arial", 14, "normal"))


def tap(x, y):
    """Dibuja X u O solo si está libre la casilla."""
    x = floor(x)
    y = floor(y)

    if (x, y) in board:
        mostrar_mensaje("¡Casilla ocupada!😅")
        return

    player = state['player']
    board[(x, y)] = players

    draw = players[player]
    draw(x, y)
    turtle.update()

    state['player'] = not player  # Cambia de jugador
    msg.clear()  # Limpia cualquier mensaje anterior


turtle.setup(420, 420, 370, 0)     # Tamaño de ventana
turtle.hideturtle()               # Oculta la flecha
turtle.tracer(False)             # Dibujo más rápido
grid()                           # Dibuja la cuadrícula
turtle.update()                  # Refresca pantalla
turtle.onscreenclick(tap)        # Clic para jugar
turtle.done()                    # Mantiene la ventana abierta

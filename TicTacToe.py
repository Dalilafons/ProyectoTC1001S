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


state = {'player': 0, 'game_over': False}  # game_over para bloquear clics
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
    msg.write(texto, align="center", font=("Arial", 16, "normal"))


def check_winner():
    """Verifica si hay un ganador antes de evaluar empate."""
    # Coordenadas ajustadas con floor(): -200, -67, 66
    C = [-200, -67, 66]

    posiciones_ganadoras = [
        # Filas
        [(C[0], C[2]), (C[1], C[2]), (C[2], C[2])],
        [(C[0], C[1]), (C[1], C[1]), (C[2], C[1])],
        [(C[0], C[0]), (C[1], C[0]), (C[2], C[0])],
        # Columnas
        [(C[0], C[2]), (C[0], C[1]), (C[0], C[0])],
        [(C[1], C[2]), (C[1], C[1]), (C[1], C[0])],
        [(C[2], C[2]), (C[2], C[1]), (C[2], C[0])],
        # Diagonales
        [(C[0], C[2]), (C[1], C[1]), (C[2], C[0])],
        [(C[0], C[0]), (C[1], C[1]), (C[2], C[2])]
    ]

    for jugador in [0, 1]:
        for combinacion in posiciones_ganadoras:
            if all(
                casilla in board and board[casilla] == jugador
                for casilla in combinacion
            ):
                return jugador  # Retorna el jugador ganador

    if len(board) == 9:
        return "empate"

    return None


def tap(x, y):
    """Dibuja X u O solo si está libre la casilla y verifica el resultado."""
    if state['game_over']:  # Evita clics tras finalizar el juego
        return

    x = floor(x)
    y = floor(y)

    if (x, y) in board:
        mostrar_mensaje("¡Casilla ocupada!😅")
        return

    player = state['player']
    board[(x, y)] = player
    draw = players[player]
    draw(x, y)
    turtle.update()

    resultado = check_winner()

    if resultado == 0:
        mostrar_mensaje("¡Ganó X! 🎉")
        state['game_over'] = True
        turtle.onscreenclick(None)  # Bloquea más clics
    elif resultado == 1:
        mostrar_mensaje("¡Ganó O! 🎉")
        state['game_over'] = True
        turtle.onscreenclick(None)
    elif resultado == "empate":
        mostrar_mensaje("¡Empate! 🤝")
        state['game_over'] = True
        turtle.onscreenclick(None)
    else:
        state['player'] = not player  # Cambia de turno
        msg.clear()


turtle.setup(420, 420, 370, 0)     # Tamaño de ventana
turtle.hideturtle()               # Oculta la flecha
turtle.tracer(False)             # Dibujo más rápido
grid()                           # Dibuja la cuadrícula
turtle.update()                  # Refresca pantalla
turtle.onscreenclick(tap)        # Clic para jugar
turtle.done()                    # Mantiene la ventana abierta

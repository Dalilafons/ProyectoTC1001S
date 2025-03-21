# ProyectoTC1001S
Proyecto de Herramientas computacionales: Arte de la programación.

# TicTacToe - Proyecto Mejorado

## Descripción
Este proyecto es una implementación del clásico juego de **Tic-Tac-Toe** en Python utilizando la librería `turtle`. Se han realizado mejoras en la lógica del juego y en la interfaz gráfica.

---

## Cambios Realizados

### **1. Validación de Casillas Ocupadas**
- Antes de permitir una jugada, el juego verifica si la casilla ya está ocupada.Evita que los jugadores sobrescriban movimientos anteriores.

### **2. Detección del Fin del Juego**
- Se implementó la detección de victoria o empate.
- Si un jugador gana, se muestra un mensaje en pantalla.
- El juego ahora finaliza correctamente cuando hay un ganador.

### **3. Corrección de Asignación en el Tablero**
- **Error corregido:** Se estaba guardando la lista de funciones `players` en el tablero en lugar del número del jugador.
- Ahora el tablero almacena correctamente `0` para "X" y `1` para "O".

### **4. Ajustes de Estilo con `flake8`**
- Se eliminaron espacios en blanco innecesarios (`W291, W293`).
- Se añadieron líneas en blanco donde era requerido (`E305`).


---

## Instrucciones para Ejecutar el Juego

1. Asegúrate de tener **Python** instalado.
2. Instala la librería `freegames` si no la tienes:
   ```bash
   pip install freegames
   ```
3. Ejecuta el script con:
   ```bash
   python TicTacToe.py
   ```
4. **¡Juega!** Haz clic en una casilla para colocar una "X" o "O".

---

# Pac-Man - Proyecto Mejorado

## Descripción
Este proyecto es una implementación del clásico juego de **Pac-Man** en Python utilizando la librería `turtle`. Se han realizado mejoras en la jugabilidad y la apariencia gráfica, además de ajustes en la inteligencia artificial de los fantasmas para hacer el juego más desafiante.

---

## Cambios Realizados

### **1. Aceleración de los Fantasmas**
- Se ajustó la velocidad de los fantasmas, lo que hace que se muevan más rápido a lo largo del tablero, aumentando la dificultad del juego.
- Se cambió el intervalo de tiempo entre cada movimiento de los fantasmas a **50 ms** para hacerlos más rápidos.

### **2. Mejora en la Apariencia Gráfica**
- Se cambió el color de fondo del tablero a **fucsia** para darle un aspecto más vibrante.
- Los puntos ahora tienen un color **naranja brillante**, lo que los hace más visibles en el tablero.
- El color de **Pac-Man** se ajustó a **rosa neón**, mientras que los fantasmas ahora son de color **azul eléctrico**.

### **3. Ajustes en el Tamaño de las Casillas**
- Se aumentó el tamaño de las casillas del tablero a **30 píxeles**, lo que proporciona una mejor visualización y mayor espacio para los elementos del juego.

### **4. Cambio en la Lógica de Movimiento de los Fantasmas**
- Los fantasmas ahora tienen una IA más avanzada para cambiar de dirección. Si no pueden moverse en su dirección actual, eligen aleatoriamente una nueva dirección.
- Se mejoró la detección de colisiones entre Pac-Man y los fantasmas, lo que ahora termina el juego si Pac-Man es tocado por un fantasma.

### **5. Ajustes de Estilo con `flake8`**
- Se eliminaron espacios en blanco innecesarios (`W291, W293`).
- Se añadieron líneas en blanco donde era requerido (`E305`).
- Se corrigieron líneas de código que excedían los **79 caracteres** (`E501`).

---

## Instrucciones para Ejecutar el Juego

1. Asegúrate de tener **Python** instalado.
2. Instala la librería `freegames` si no la tienes:
   ```bash
   pip install freegames


## Autores
**Dalila Fonseca Maya A01711722**
**Alejandro Lemus Salgado A01770848**  

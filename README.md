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

## Autor
**Dalila Fonseca Maya A01711722**  

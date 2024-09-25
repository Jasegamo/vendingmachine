import tkinter as tk

# Definir las transiciones del autómata
transiciones = {
    "Q0": {"1": "Q2", "5": "Q1"},
    "Q1": {"1": "Q3", "5": "Q4"},
    "Q2": {"1": "Q6", "5": "Q5"},
    "Q3": {"1": "Q7", "5": "Q8"},
    "Q4": {"1": "Q9", "5": "Q10"},
    "Q5": {"1": "Q12", "5": "Q11"},
    "Q6": {"1": "Q14", "5": "Q13"},
    "Q7": {"1": "Q15", "5": "Q16"},
    "Q8": {"1": "Q17", "5": "Q18"},
    "Q9": {"1": "Q19", "5": "Q20"},
    "Q10": {"1": "Q21", "5": "Q22"},
    "Q11": {"5": "Q23"},
    "Q12": {"1": "Q24"},
    "Q13": {"1": "Q25"},
    "Q14": {"1": "Q26"}
}

# Función para mostrar la tabla de transiciones y resaltar las celdas según la cadena
def mostrar_tabla_transiciones(cadena):
    ventana_tabla = tk.Toplevel()  # Crear una nueva ventana
    ventana_tabla.title("Tabla de Transiciones")
    
    # Crear el encabezado de la tabla (símbolos del alfabeto)
    tk.Label(ventana_tabla, text="Estado", bg="lightgray", width=10, height=2).grid(row=0, column=0)
    tk.Label(ventana_tabla, text="1", bg="lightgray", width=10, height=2).grid(row=0, column=1)
    tk.Label(ventana_tabla, text="5", bg="lightgray", width=10, height=2).grid(row=0, column=2)

    # Variables para almacenar el estado actual y su color
    estado_actual = "Q0"
    colores_resaltado = []

    # Recorrer la cadena y destacar las celdas correspondientes
    for simbolo in cadena:
        if estado_actual in transiciones and simbolo in transiciones[estado_actual]:
            siguiente_estado = transiciones[estado_actual][simbolo]
            colores_resaltado.append((estado_actual, simbolo))
            estado_actual = siguiente_estado
        else:
            break  # Salir si no hay transición válida

    # Mostrar la tabla con las transiciones
    for i, (estado, transicion) in enumerate(transiciones.items()):
        tk.Label(ventana_tabla, text=estado, bg="lightblue", width=10, height=2).grid(row=i+1, column=0)
        
        # Columna para las transiciones con '1'
        color_celda = "yellow" if (estado, "1") in colores_resaltado else "white"
        tk.Label(ventana_tabla, text=transicion.get("1", "-"), bg=color_celda, width=10, height=2).grid(row=i+1, column=1)
        
        # Columna para las transiciones con '5'
        color_celda = "yellow" if (estado, "5") in colores_resaltado else "white"
        tk.Label(ventana_tabla, text=transicion.get("5", "-"), bg=color_celda, width=10, height=2).grid(row=i+1, column=2)

# Ejemplo de cómo llamar a la función con la ventana principal y la cadena ingresada:
# mostrar_tabla_transiciones("5555")

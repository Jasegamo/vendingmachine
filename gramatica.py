import tkinter as tk

transiciones = {
    "S0": {"1": "Q2", "5": "Q1"},
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

# Función para mostrar la gramática del autómata y la expresión regular
def mostrar_gramatica(cadena):
    # Crear una nueva ventana de Tkinter para mostrar la gramática
    ventana_gramatica = tk.Toplevel()
    ventana_gramatica.title("Gramática y Expresión Regular")
    ventana_gramatica.geometry("600x400")
    
    # Etiqueta para el título
    etiqueta_titulo = tk.Label(ventana_gramatica, text="Gramática del Autómata y Expresión Regular", font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)
    
    # Generar la gramática basada en la cadena recibida
    gramatica_automata = generar_gramatica_automata(cadena)
    expresion_regular = generar_expresion_regular(cadena)
    
    # Mostrar la gramática del autómata
    etiqueta_gramatica = tk.Label(ventana_gramatica, text=f"Gramática del Autómata:\n{gramatica_automata}", font=("Arial", 12), justify="left")
    etiqueta_gramatica.pack(pady=10)
    
    # Mostrar la expresión regular correspondiente
    etiqueta_expresion = tk.Label(ventana_gramatica, text=f"Expresión Regular:\n{expresion_regular}", font=("Arial", 12), justify="left")
    etiqueta_expresion.pack(pady=10)
    

# Función para generar la gramática del autómata basada en la cadena
def generar_gramatica_automata(cadena):
    reglas = []
    estado_actual = "S0"  # Estado inicial

    for i, simbolo in enumerate(cadena):
        # Comprobamos si hay una transición válida para el estado actual y el símbolo de la cadena
        if simbolo in transiciones[estado_actual]:
            estado_siguiente = transiciones[estado_actual][simbolo]
            # Añadimos la regla gramatical
            reglas.append(f"{estado_actual} → {simbolo} {estado_siguiente}")
            # Actualizamos el estado actual
            estado_actual = estado_siguiente
        else:
            # Si no hay transición válida, devolvemos un mensaje de error
            return f"Error: no hay transición para el símbolo '{simbolo}' en el estado '{estado_actual}'"
    
    # Añadimos la regla final que lleva al estado de aceptación (ε-transición)
    reglas.append(f"{estado_actual} → ε")  # Estado de aceptación

    # Formatear las reglas en una sola cadena de texto
    return "\n".join(reglas)

# Función para generar una expresión regular basada en la cadena
def generar_expresion_regular(cadena):
    # Convertir la cadena en una expresión regular
    expresion = f"({'|'.join(set(cadena))})*"
    return expresion

import tkinter as tk

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
    # Ejemplo de generación de reglas dinámicas basadas en la cadena
    for i, simbolo in enumerate(cadena):
        reglas.append(f"S{i} → {simbolo} S{i+1}")
    reglas.append(f"S{len(cadena)} → ε")  # Estado de aceptación

    # Formatear las reglas en una sola cadena de texto
    return "\n".join(reglas)

# Función para generar una expresión regular basada en la cadena
def generar_expresion_regular(cadena):
    # Convertir la cadena en una expresión regular
    expresion = f"({'|'.join(set(cadena))})*"
    return expresion

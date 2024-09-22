import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Definir la función para dibujar el grafo del autómata
def dibujar_grafo():
    G = nx.MultiDiGraph()
    subset_map = {
        "Q0": 0,  "Q1": 1,  "Q2": 1,  "Q3": 2,  "Q4": 2,  "Q5": 2,  "Q6": 2,
        "Q7": 3,  "Q8": 3,  "Q9": 3,  "Q10": 3, "Q11": 3, "Q12": 3, "Q13": 3,
        "Q14": 3, "Q15": 4, "Q16": 4, "Q17": 4, "Q18": 4, "Q19": 4, "Q20": 4,
        "Q21": 4, "Q22": 4, "Q23": 4, "Q24": 4, "Q25": 4, "Q26": 4
    }

    G.add_nodes_from(subset_map.keys())
    
    # Lista de transiciones con valores 1 o 5
    transiciones = [
        ("Q0", "Q2", 1), ("Q0", "Q1", 5),
        ("Q1", "Q3", 1), ("Q1", "Q4", 5),
        ("Q3", "Q7", 1), ("Q3", "Q8", 5),
        ("Q7", "Q15", 1), ("Q7", "Q16", 5),
        ("Q8", "Q17", 1), ("Q8", "Q18", 5),
        ("Q4", "Q9", 1), ("Q4", "Q10", 5),
        ("Q9", "Q19", 1), ("Q9", "Q20", 5),
        ("Q10", "Q21", 1), ("Q10", "Q22", 5),
        ("Q2", "Q6", 1), ("Q2", "Q5", 5),
        ("Q5", "Q12", 1), ("Q5", "Q11", 5),
        ("Q11", "Q23", 5), ("Q12", "Q24", 1),
        ("Q6", "Q14", 1), ("Q6", "Q13", 5),
        ("Q13", "Q25", 1), ("Q14", "Q26", 1)
    ]

    # Añadir transiciones con etiquetas (valores 1 y 5)
    for (origen, destino, valor) in transiciones:
        if valor == 1:
            G.add_edge(origen, destino, label=str(f"$1000"))
        elif valor == 5:    
            G.add_edge(origen, destino, label=str(f"$500"))

    # Posiciones de los nodos
    pos = hierarchy_pos(G, subset_map)

    # Nodos de aceptación
    nodos_aceptacion = ["Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24", "Q25", "Q26"]
    
    # Colores de los nodos
    color_nodos = ['lightgreen' if node in nodos_aceptacion else 'blue' for node in G.nodes()]
    
    # Dibujar nodos y etiquetas
    nx.draw(G, pos, with_labels=True, node_color=color_nodos, node_size=2000, font_size=10, font_weight='bold')

    # Obtener etiquetas de las aristas y adaptarlas para MultiDiGraph
    edge_labels = {(origen, destino): G[origen][destino][0]['label'] for origen, destino in G.edges()}
    
    # Dibujar etiquetas de las aristas (1 o 5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el grafo
    plt.show()

# Función para crear y mostrar la tabla de transiciones en una ventana de Tkinter
def crear_tabla_transiciones():
    # Crear una nueva ventana de Tkinter
    ventana = tk.Tk()
    ventana.title("Tabla de Transiciones")

    # Crear la tabla de transiciones con los estados en las filas y las columnas '1' y '5'
    columnas = ('Estado', '1', '5')
    tabla_transiciones = ttk.Treeview(ventana, columns=columnas, show='headings')

    # Definir los encabezados de la tabla
    for col in columnas:
        tabla_transiciones.heading(col, text=col)

    # Definir los estados y las transiciones
    estados = ['Q' + str(i) for i in range(27)]
    
    # Transiciones dadas (Estado Actual, Símbolo, Estado Siguiente)
    transiciones = [
        ("Q0", 1, "Q2"), ("Q0", 5, "Q1"),
        ("Q1", 1, "Q3"), ("Q1", 5, "Q4"),
        ("Q3", 1, "Q7"), ("Q3", 5, "Q8"),
        ("Q7", 1, "Q15"), ("Q7", 5, "Q16"),
        ("Q8", 1, "Q17"), ("Q8", 5, "Q18"),
        ("Q4", 1, "Q9"), ("Q4", 5, "Q10"),
        ("Q9", 1, "Q19"), ("Q9", 5, "Q20"),
        ("Q10", 1, "Q21"), ("Q10", 5, "Q22"),
        ("Q2", 1, "Q6"), ("Q2", 5, "Q5"),
        ("Q5", 1, "Q12"), ("Q5", 5, "Q11"),
        ("Q11", 5, "Q23"), ("Q12", 1, "Q24"),
        ("Q6", 1, "Q14"), ("Q6", 5, "Q13"),
        ("Q13", 1, "Q25"), ("Q14", 1, "Q26")
    ]

    # Crear un diccionario para almacenar las transiciones de cada estado
    tabla_datos = {estado: {1: "-", 5: "-"} for estado in estados}

    # Rellenar el diccionario con las transiciones reales
    for origen, simbolo, destino in transiciones:
        tabla_datos[origen][simbolo] = destino

    # Agregar las filas a la tabla con los estados y las transiciones correspondientes
    for estado in estados:
        tabla_transiciones.insert('', tk.END, values=(estado, tabla_datos[estado][1], tabla_datos[estado][5]))

    # Empaquetar la tabla en la ventana
    tabla_transiciones.pack(fill=tk.BOTH, expand=True)

    # Configurar la ventana de Tkinter para que se ajuste al tamaño de la tabla
    ventana.geometry('400x600')

    # Ejecutar el bucle principal de Tkinter para mostrar la ventana con la tabla
    ventana.mainloop()


def hierarchy_pos(G, subset_map, width=1., vert_gap=0.2, vert_loc=0):
    pos = {}
    levels = set(subset_map.values())
    levels = sorted(levels)
    
    for level in levels:
        nodes_in_level = [node for node, subset in subset_map.items() if subset == level]
        dx = width / (len(nodes_in_level) + 1)
        for i, node in enumerate(nodes_in_level):
            pos[node] = (i * dx, vert_loc - level * vert_gap)
    return pos

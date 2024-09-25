import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(cadena=None):
    # Definición de los nodos y sus niveles
    subset_map = {
        "Q0": 0,  "Q1": 1,  "Q2": 1,  "Q3": 2,  "Q4": 2,  "Q5": 2,  "Q6": 2,
        "Q7": 3,  "Q8": 3,  "Q9": 3,  "Q10": 3, "Q11": 3, "Q12": 3, "Q13": 3,
        "Q14": 3, "Q15": 4, "Q16": 4, "Q17": 4, "Q18": 4, "Q19": 4, "Q20": 4,
        "Q21": 4, "Q22": 4, "Q23": 4, "Q24": 4, "Q25": 4, "Q26": 4
    }

    # Crear el grafo dirigido
    G = nx.MultiDiGraph()
    G.add_nodes_from(subset_map.keys())

    # Definir las transiciones entre nodos
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

    # Añadir las aristas con las etiquetas correspondientes
    for (origen, destino, valor) in transiciones:
        if valor == 1:
            G.add_edge(origen, destino, label="$1000")
        elif valor == 5:
            G.add_edge(origen, destino, label="$500")

    # Posición de los nodos (usamos una función para calcular la jerarquía)
    pos = hierarchy_pos(G, subset_map)

    # Nodos de aceptación
    nodos_aceptacion = {"Q15", "Q16", "Q17", "Q18", "Q19", "Q20", "Q21", "Q22", "Q23", "Q24", "Q25", "Q26"}

    # Colorear los nodos
    color_nodos = ['lightgreen' if nodo in nodos_aceptacion else 'lightblue' for nodo in G.nodes()]

    # Si se proporciona una cadena, resaltar los nodos recorridos
    if cadena:
        nodo_actual = "Q0"  # Nodo inicial
        for simbolo in cadena:
            # Identificar la transición correcta según el símbolo (1 o 5)
            siguiente_nodo = None
            for origen, destino, valor in transiciones:
                if origen == nodo_actual and str(valor) == simbolo:
                    siguiente_nodo = destino
                    break

            # Si encontramos un nodo siguiente, coloreamos ese nodo en naranja
            if siguiente_nodo:
                color_nodos[list(G.nodes()).index(siguiente_nodo)] = 'orange'
                nodo_actual = siguiente_nodo
            else:
                break  # Si no hay una transición válida, detenemos el recorrido

    # Dibujar el grafo
    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(G, pos, node_color=color_nodos, with_labels=True, node_size=500, ax=ax, font_weight='bold')
    
    # Dibujar las etiquetas de las aristas
    edge_labels = {(u, v): data['label'] for u, v, data in G.edges(data=True)}
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    
    plt.show()


# Función para definir la jerarquía del grafo (layout de árbol)
def hierarchy_pos(G, subset_map):
    pos = {}
    for nodo, nivel in subset_map.items():
        if nivel not in pos:
            pos[nivel] = []
        pos[nivel].append(nodo)

    pos_dict = {}
    for nivel, nodos in pos.items():
        num_nodos = len(nodos)
        spacing = 1.0 / (num_nodos + 1)
        for i, nodo in enumerate(nodos):
            pos_dict[nodo] = (i * spacing, -nivel)

    return pos_dict

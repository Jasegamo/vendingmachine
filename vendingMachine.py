import tkinter as tk
from PIL import Image, ImageTk
import grafo_automata

# Definir los productos con su costo y las cadenas válidas asociadas
productos = {
    '5111': 3500, '1111': 4000, '5511': 3000, '5551': 2500, '1511': 3500, '5515': 2500,
    '5151': 3000, '5115': 3000, '5555': 2000, '5155': 2500, '1555': 2500, '1151': 3500
}

# Definir el alfabeto del autómata
alfabeto = {'1', '5'}

# Variables para almacenar los bombillos y el índice del último bombillo encendido
bombillos = []
ultimo_bombillo_encendido = None  # Ningún bombillo está encendido inicialmente

# Función que procesa la cadena ingresada
def procesar_cadena(event):
    global ultimo_bombillo_encendido
    cadena = entrada_cadena.get()  # Obtener el texto ingresado
    entrada_cadena.delete(0, tk.END)  # Limpiar el campo de entrada

    # Apagar el último bombillo encendido, si hay uno
    if ultimo_bombillo_encendido is not None:
        bombillos[ultimo_bombillo_encendido].config(image=imagen_bombillo_apagado)
        bombillos[ultimo_bombillo_encendido].image = imagen_bombillo_apagado
        ultimo_bombillo_encendido = None  # Resetear la variable

    # Verificar si la cadena contiene solo elementos del alfabeto
    if validar_alfabeto(cadena):
        # Verificar si la cadena ingresada corresponde exactamente a un producto
        if cadena in productos:
            mostrar_producto(cadena)
        else:
            resultado_label.config(text="Pertenece al alfabeto, pero no es un estado de aceptación.", fg="red")
    else:
        resultado_label.config(text="La cadena contiene símbolos fuera del alfabeto.", fg="red")

# Función para validar que la cadena pertenece al alfabeto
def validar_alfabeto(cadena):
    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False
    return True

# Función para mostrar el producto comprado
def mostrar_producto(codigo_producto):
    global ultimo_bombillo_encendido

    indice_producto = list(productos.keys()).index(codigo_producto)
    imagen_comprada = Image.open(f"producto{indice_producto + 1}.png")
    imagen_resized = imagen_comprada.resize((100, 100), Image.Resampling.LANCZOS)
    imagen_turned = imagen_resized.rotate(90)
    imagen_tk = ImageTk.PhotoImage(imagen_turned)

    etiqueta_producto_comprado.config(image=imagen_tk)
    etiqueta_producto_comprado.image = imagen_tk
    resultado_label.config(text=f"Producto {codigo_producto} entregado.", fg="green")

    # Cambiar el bombillo a verde
    bombillos[indice_producto].config(image=imagen_bombillo_verde)
    bombillos[indice_producto].image = imagen_bombillo_verde

    # Actualizar el índice del último bombillo encendido
    ultimo_bombillo_encendido = indice_producto

# Función para mostrar la tabla de transiciones
def mostrar_tabla_transiciones():
    grafo_automata.crear_tabla_transiciones()

# Configuración inicial de la ventana
ventana = tk.Tk()
ventana.title("Máquina Expendedora")
ventana.geometry("1000x1000")
ventana.config(bg="black")

# Crear un frame común para la máquina expendedora y la ranura de entrega
frame_general = tk.Frame(ventana, bg="darkred")
frame_general.grid(row=0, column=0, padx=20, pady=5)

# Crear un frame para la máquina expendedora (productos)
frame_maquina = tk.Frame(frame_general, bg="brown")
frame_maquina.grid(row=0, column=0, padx=5, pady=5)

# Crear un frame para la apertura donde "cae" el producto
frame_apertura = tk.Frame(frame_general, bg="black", width=120, height=100)
frame_apertura.grid(row=1, column=0)
frame_apertura.pack_propagate(False)

# Etiqueta para mostrar el producto comprado en la apertura
etiqueta_producto_comprado = tk.Label(frame_apertura, bg="black")
etiqueta_producto_comprado.pack(anchor="center")

# Cargar y redimensionar las imágenes de los productos
imagenes_productos = []
for i in range(len(productos)):
    imagen = Image.open(f"producto{i+1}.png")
    imagen_resized = imagen.resize((100, 100), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_resized)
    imagenes_productos.append(imagen_tk)

# Cargar las imágenes de bombillos
imagen_bombillo_apagado = Image.open("bombillo_apagado.png").resize((20, 20), Image.Resampling.LANCZOS)
imagen_bombillo_apagado = ImageTk.PhotoImage(imagen_bombillo_apagado)

imagen_bombillo_verde = Image.open("bombillo_verde.png").resize((20, 20), Image.Resampling.LANCZOS)
imagen_bombillo_verde = ImageTk.PhotoImage(imagen_bombillo_verde)

# Crear botones para cada producto en la máquina expendedora
for i in range(4):
    for j in range(3):
        indice_producto = i * 3 + j
        if indice_producto < len(productos):
            etiqueta_producto = tk.Label(frame_maquina, image=imagenes_productos[indice_producto], bg="black")
            etiqueta_producto.grid(row=i*2, column=j, padx=5, pady=5)

            # Crear un contenedor para el precio y el bombillo
            frame_info = tk.Frame(frame_maquina, bg="black")
            frame_info.grid(row=i*2+1, column=j, padx=5, pady=5)

            codigo_producto = list(productos.keys())[indice_producto]
            costo_producto = productos[codigo_producto]

            etiqueta_info = tk.Label(frame_info, text=f"{costo_producto}", font=("Arial", 10), bg="black", fg="white")
            etiqueta_info.pack(side="left")

            # Colocar el bombillo junto a la etiqueta de información
            bombillo_label = tk.Label(frame_info, image=imagen_bombillo_apagado, bg="black")
            bombillo_label.pack(side="left", padx=5)
            bombillos.append(bombillo_label)

# Colocar el campo de entrada y el resultado en el mismo contenedor que la máquina expendedora
frame_interaccion = tk.Frame(ventana, bg="orange")
frame_interaccion.grid(row=0, column=1, pady=10)

# Crear un campo de entrada para la cadena del usuario
entrada_cadena = tk.Entry(frame_interaccion, width=20, font=("Arial", 14))
entrada_cadena.grid(row=0, column=0, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(frame_interaccion, text="", font=("Arial", 14), bg="white")
resultado_label.grid(row=1, column=0, pady=10)

# Asignar la tecla "Enter" para procesar la cadena
ventana.bind('<Return>', procesar_cadena)

# Iniciar la aplicación principal
ventana.mainloop()

# Mostrar el grafo
grafo_automata.dibujar_grafo()

# Después de que se cierra la ventana del grafo, mostrar la tabla de transiciones
mostrar_tabla_transiciones()

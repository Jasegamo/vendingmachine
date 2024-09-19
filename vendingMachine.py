import tkinter as tk
from PIL import Image, ImageTk

# Definir las monedas y sus valores
monedas = {'1': 1000, '2': 200, '5': 500}

# Definir los productos con su costo y las letras asociadas
productos = {
    'CB': 2500, 'CC': 4000, 'CL': 3000, 'CR': 2500, 'DR': 3500, 'MZ': 2500,
    'PL': 3000, 'PP': 3000, 'PS': 2500, 'QT': 2500, 'SP': 2500, 'UV': 2500
}

# Estado inicial de la máquina (dinero acumulado)
estado_actual = 0

# Alfabeto válido (monedas y letras)
alfabeto = set(monedas.keys()).union(set('BCDLMPQRSTUVZ'))

# Función que procesa la cadena ingresada
def procesar_cadena(event):
    global estado_actual
    estado_actual = 0
    codigo_producto = ''
    
    cadena = entrada_cadena.get()  # Obtener el texto ingresado
    entrada_cadena.delete(0, tk.END)  # Limpiar el campo de entrada

    # Verificar si todos los caracteres pertenecen al alfabeto
    for char in cadena:
        if char not in alfabeto:
            resultado_label.config(text="No pertenece al autómata.", fg="red")
            return

    # Procesar las monedas
    for char in cadena:
        if char in monedas:
            estado_actual += monedas[char]  # Sumar el valor de la moneda
        elif char.isalpha():
            codigo_producto += char  # Acumular las letras del producto

    # Verificar si las letras del producto y el valor son válidos
    if codigo_producto in productos:
        costo_producto = productos[codigo_producto]
        if isinstance(costo_producto, list):  # Si hay varios precios posibles
            if estado_actual in costo_producto:
                mostrar_producto(codigo_producto)
            else:
                resultado_label.config(text=f"Pertenece al autómata, pero la cantidad es incorrecta.", fg="red")
        else:
            if estado_actual == costo_producto:
                mostrar_producto(codigo_producto)
            else:
                resultado_label.config(text=f"Pertenece al autómata, pero la cantidad es incorrecta.", fg="red")
    else:
        resultado_label.config(text="Pertenece al autómata, pero no lleva a ningún producto.", fg="red")

# Función para mostrar el producto comprado girado
def mostrar_producto(codigo_producto):
    # Cargar la imagen del producto comprado
    indice_producto = list(productos.keys()).index(codigo_producto)
    imagen_comprada = Image.open(f"producto{indice_producto + 1}.png")
    
    # Girar la imagen 90 grados
    imagen_girada = imagen_comprada.rotate(90)
    
    # Redimensionar la imagen para que encaje en la apertura de la dispensadora
    imagen_resized = imagen_girada.resize((100, 100), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_resized)
    
    # Mostrar la imagen del producto en la apertura
    etiqueta_producto_comprado.config(image=imagen_tk)
    etiqueta_producto_comprado.image = imagen_tk  # Necesario para evitar que la imagen sea recolectada por el garbage collector
    resultado_label.config(text=f"Producto {codigo_producto} entregado.", fg="green")

# Configuración inicial de la ventana
ventana = tk.Tk()
ventana.title("Máquina Expendedora")
ventana.geometry("600x800")
ventana.config(bg="lightblue")

# Crear un frame para la máquina expendedora
frame_maquina = tk.Frame(ventana, bg="black")
frame_maquina.grid(row=0, column=0, padx=20, pady=20)

# Crear un frame para la apertura donde "cae" el producto
frame_apertura = tk.Frame(ventana, bg="black", width=200, height=200)
frame_apertura.grid(row=0, column=1, pady=0)
frame_apertura.pack_propagate(False)

# Etiqueta para mostrar el producto comprado en la apertura
etiqueta_producto_comprado = tk.Label(frame_apertura, bg="black")
etiqueta_producto_comprado.pack()

# Cargar y redimensionar las imágenes de los productos
imagenes_productos = []
for i in range(len(productos)):  # Asegurarse de no sobrepasar el número de productos
    imagen = Image.open(f"producto{i+1}.png")
    imagen_resized = imagen.resize((100, 100), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen_resized)
    imagenes_productos.append(imagen_tk)

# Crear botones para cada producto en la máquina expendedora (opcional, solo para mostrar los productos)
for i in range(4):
    for j in range(3):
        indice_producto = i * 3 + j
        if indice_producto < len(productos):  # Asegurarse de que el índice no sea mayor que el número de productos
            etiqueta_producto = tk.Label(frame_maquina, image=imagenes_productos[indice_producto])
            etiqueta_producto.grid(row=i*2, column=j, padx=5, pady=5)

            # Crear una etiqueta para mostrar el precio y el código del producto
            codigo_producto = list(productos.keys())[indice_producto]
            if isinstance(productos[codigo_producto], list):
                costo_producto = '/'.join(str(costo) for costo in productos[codigo_producto])
            else:
                costo_producto = productos[codigo_producto]

            etiqueta_info = tk.Label(frame_maquina, text=f"{costo_producto} - {codigo_producto}", font=("Arial", 10), bg="black", fg="white")
            etiqueta_info.grid(row=i*2+1, column=j)

# Crear un campo de entrada para la cadena del usuario
entrada_cadena = tk.Entry(ventana, width=20, font=("Arial", 14))
entrada_cadena.grid(row=1, column=0, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 14), bg="lightblue")
resultado_label.grid(row=1, column=1, pady=10)

# Asignar la tecla "Enter" para procesar la cadena
ventana.bind('<Return>', procesar_cadena)

# Iniciar la aplicación
ventana.mainloop()

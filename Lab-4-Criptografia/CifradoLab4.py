import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES, AES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

key_length = 0
iv_length = 0
block_size = 0

# Función para pasar a la segunda "página" donde se ingresa la clave y el IV
def mostrar_pagina_key_iv():
    global key_length, iv_length, block_size
    texto = texto_entrada.get()
    seleccion = opcion_var.get()
    
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un texto antes de seleccionar.")
        return
    
    if seleccion == 1:  # DES
        metodo = "DES"
        key_length = 8
        iv_length = 8
        block_size = 8
        
    elif seleccion == 2:  # AES-256
        metodo = "AES-256"
        key_length = 32
        iv_length = 16
        block_size = 16
        
    elif seleccion == 3:  # 3DES
        metodo = "3DES"
        key_length = 24
        iv_length = 8  # Típicamente 3DES usa un IV de 8 bytes
        block_size = 8
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un método.")
        return
    
    # Ocultar la primera página
    titulo.pack_forget()
    texto_entrada.pack_forget()
    frame_opciones.pack_forget()
    boton.pack_forget()
    
    # Mostrar la segunda página
    label_metodo.config(text=f"Método seleccionado: {metodo}")
    label_metodo.pack(pady=10)
    label_key.pack(pady=5)
    key_entry.pack(pady=5)
    label_iv.pack(pady=5)
    iv_entry.pack(pady=5)
    boton_procesar.pack(pady=20)

# Función para procesar los datos ingresados en la segunda "página"
def procesar_datos():
    key = key_entry.get()
    iv = iv_entry.get()
    
    if not key or not iv:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return
    
    key = key.encode()
    iv = iv.encode()
    
    if len(key) < key_length:
        key += get_random_bytes(key_length - len(key))
    elif len(key) > key_length:
        key = key[:key_length]
        
    if len(iv) < iv_length:
        iv += get_random_bytes(iv_length - len(iv))
    elif len(iv) > iv_length:
        iv = iv[:iv_length]

    seleccion = opcion_var.get()
    texto = texto_entrada.get().encode()  # Convertir el texto a bytes
    metodo = "DES" if seleccion == 1 else "AES-256" if seleccion == 2 else "3DES"

    if metodo == "DES":
        
        cipher = DES.new(key, DES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(texto, DES.block_size))
    elif metodo == "AES-256":
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(texto, AES.block_size))
    elif metodo == "3DES":
        
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(texto, DES3.block_size))
    
    # Aplicar padding y cifrar el texto
    
    encoded_ciphertext = base64.b64encode(ciphertext).decode()
    
    messagebox.showinfo("Datos Ingresados", f"Cifrado: {metodo}\nTexto plano: {texto.decode()}\nClave: {key}\nIV: {iv}\n \n Texto cifrado en {metodo}: {encoded_ciphertext}")
    
# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Laboratorio 4 Criptografía y Seguridad En Redes")
ventana.geometry("400x300")
ventana.configure(bg="#f0f0f5")

# Primera "página" de la ventana
titulo = tk.Label(ventana, text="Ingrese el texto a cifrar y seleccione el método:", 
                  font=("Arial", 14, "bold"), bg="#f0f0f5", fg="#333333")
titulo.pack(pady=15)

texto_entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
texto_entrada.pack(pady=10)

frame_opciones = tk.Frame(ventana, bg="#e6e6fa", bd=2, relief="groove")
frame_opciones.pack(padx=20, pady=10, fill="both")

opcion_var = tk.IntVar()
tk.Radiobutton(frame_opciones, text="DES", variable=opcion_var, value=1, 
               font=("Arial", 12), bg="#e6e6fa", fg="#333333", selectcolor="#c0c0f0").pack(anchor="w", padx=10, pady=5)
tk.Radiobutton(frame_opciones, text="AES-256", variable=opcion_var, value=2, 
               font=("Arial", 12), bg="#e6e6fa", fg="#333333", selectcolor="#c0c0f0").pack(anchor="w", padx=10, pady=5)
tk.Radiobutton(frame_opciones, text="3DES", variable=opcion_var, value=3, 
               font=("Arial", 12), bg="#e6e6fa", fg="#333333", selectcolor="#c0c0f0").pack(anchor="w", padx=10, pady=5)

boton = tk.Button(ventana, text="Seleccionar", command=mostrar_pagina_key_iv,
                  font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
boton.pack(pady=20)

# Segunda "página" de la ventana (inicialmente oculta)
label_metodo = tk.Label(ventana, font=("Arial", 12, "bold"), bg="#f0f0f5", fg="#333333")

label_key = tk.Label(ventana, text="Ingrese la clave.", font=("Arial", 12), bg="#f0f0f5")
key_entry = tk.Entry(ventana, font=("Arial", 12), width=30)

label_iv = tk.Label(ventana, text="Ingrese el Vector de Inicialización (IV).", font=("Arial", 12), bg="#f0f0f5")
iv_entry = tk.Entry(ventana, font=("Arial", 12), width=30)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_datos,
                           font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop()

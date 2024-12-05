from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Clave de 32 bytes (256 bits) para AES256
key = b'EstaEsUnaClaveDe32Bytes123456789'  # Clave de 32 bytes
iv = b'26S7eBSuDYedBQUM'  # Vector de inicialización (IV) de 16 bytes

# Texto a cifrar
data = input("Ingrese la contraseña a cifrar:  ")

# Crear el objeto AES en modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Padding al texto para que sea múltiplo de 16 bytes
ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))

# Convertir el cifrado a base64 para legibilidad
encoded_ciphertext = base64.b64encode(ciphertext).decode()

print(f'Cifrado: {encoded_ciphertext}')

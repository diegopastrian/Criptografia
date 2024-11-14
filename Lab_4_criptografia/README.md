# Laboratorio 4 - Criptografía y Seguridad en Redes

Este proyecto implementa un programa en Python para el cifrado y descifrado de mensajes utilizando algoritmos de cifrado simétrico: **DES**, **AES-256** y **3DES** en modo **CBC**, usando la biblioteca `PyCryptodome`.

## Funcionalidades

- **Selección del Algoritmo**: El usuario puede elegir entre DES, AES-256 y 3DES.
- **Ajuste de Clave e IV**: La clave y el IV se ajustan automáticamente al tamaño necesario para cada algoritmo.
- **Cifrado y Descifrado**: Los mensajes se cifran y descifran usando el modo CBC, y los resultados se muestran en Base64 para mayor legibilidad.

## Ejecución Básica

1. Ingrese el texto, clave e IV en el formato adecuado.
2. Seleccione el algoritmo deseado.
3. Visualice el texto cifrado en Base64.

## Aplicación

El cifrado simétrico es útil para proteger datos en aplicaciones de mensajería, transacciones financieras y almacenamiento seguro.


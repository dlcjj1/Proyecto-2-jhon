# La clave es un diccionario que mapea letras a otras letras.
# esta es la clave creada para asociar letra con simbolo
Clave = {'a': 'c', 'b': '-', 'c': '|', 'd': 'j', 'e': 'h', 'f': '|','g': 'x', 'h': '¿', 'i': '-', 'j': 'c', 'k': 'a', 'l': 'd','m': '|', 'n': '-', 'o': 'h', 'p': 'x', 'q': '|', 'r': '¿','s': '-', 't': 'c', 'u': 'a', 'v': 'j', 'w': '-', 'x': 'h','y': '¿', 'z': '|'}

# se pide al usuario que ingrese un mensaje
mensaje = str(input("ingrese un mensaje:"))




# se crea una funcion para poder encripar mensajes


def encriptar_mensaje(mensaje, Clave):
    
    encriptar_mensaje = ""
#el programa itera sobre las letras del mensaje 
#y reemplaza cada letra con la letra a la que está mapeada en la clave.

    for letra in mensaje:
        if letra in Clave:
            encriptar_mensaje += Clave[letra]
        else:
            encriptar_mensaje += letra
    return encriptar_mensaje



# Para desencriptar el programa itera sobre las letras del mensaje y reemplaza cada
# letra con la letra a la que está mapeada en la clave, pero en orden inverso
def desencriptar_mensaje(encriptar_mensaje, Clave):
    desencriptar_mensaje = ""
    for caracter in encriptar_mensaje:
        if caracter in Clave.values():
            for llave, value in Clave.items():
                if value == caracter:
                    desencriptar_mensaje += llave
        else:
            desencriptar_mensaje += caracter
    return desencriptar_mensaje






# Se llama a la funcion para poder darle print
encriptar = encriptar_mensaje(mensaje, Clave)

desencriptar = desencriptar_mensaje(encriptar, Clave)

# se inprime el mensaje encriptado y su decodificacion
print("Mensaje codificado:",  encriptar)
print("Mensaje decodificado:",  desencriptar)



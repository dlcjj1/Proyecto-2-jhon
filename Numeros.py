
def valInt(argumento_1, argumento_2=None):
    if argumento_2 is None:
        return isinstance(argumento_1, int)
    elif isinstance(argumento_1, int) and isinstance(argumento_2, (list, tuple)) and len(argumento_2) == 2:
        inicio, fin = argumento_2
        if type(argumento_2) == list:
            return argumento_1 >= argumento_2[0] and argumento_1 <= argumento_2[1]
        elif type(argumento_2) == tuple:
            return argumento_1 > argumento_2[0] and argumento_1 < argumento_2[1]
        else:
            raise ValueError("El segundo argumento debe estar ordenado de manera creciente")
    elif isinstance(argumento_1, int) and (not isinstance(argumento_2, (list, tuple)) or len(argumento_2) != 2):
        raise ValueError("El segundo argumento debe ser una lista o tupla de tamaño 2")
    else:
        raise TypeError("Se esperaba un argumento de tipo int y opcionalmente un argumento de tipo list o tuple de tamaño 2")

entero= valInt(2, [10,5])
print(entero)






def valFloat(argumento_1, argumento_2=None):
    if argumento_2 is None:
        return isinstance(argumento_1, float)
    elif isinstance(argumento_1, float) and isinstance(argumento_2, (list, tuple)) and len(argumento_2) == 2:
        inicio, fin = argumento_2
        if type(argumento_2) == list:
            return argumento_1 >= argumento_2[0] and argumento_1 <= argumento_2[1]
        elif type(argumento_2) == tuple:
            return argumento_1 > argumento_2[0] and argumento_1 < argumento_2[1]
        else:
            raise ValueError("El segundo argumento debe estar ordenado de manera creciente")
    elif isinstance(argumento_1, float) and (not isinstance(argumento_2, (list, tuple)) or len(argumento_2) != 2):
        raise ValueError("El segundo argumento debe ser una lista o tupla de tamaño 2")
    else:
        raise TypeError("Se esperaba un argumento de tipo float y opcionalmente un argumento de tipo list o tuple de tamaño 2")

reales= valFloat()
print(reales)



def valComplex(argumento_1, argumento_2=None):
    if argumento_2 is None:
        return isinstance(argumento_1, complex)
    elif isinstance(argumento_1, complex) and isinstance(argumento_2, (list, tuple)) and len(argumento_2) == 2:
        inicio, fin = argumento_2
        if type(argumento_2) == list:
            return abs(argumento_1) >= argumento_2[0] and abs(argumento_1) <= argumento_2[1]
        elif type(argumento_2) == tuple:
            return abs(argumento_1) > argumento_2[0] and abs(argumento_1) < argumento_2[1]
        else:
            raise ValueError("El segundo argumento debe estar ordenado de manera creciente")
    elif isinstance(argumento_1, complex) and (not isinstance(argumento_2, (list, tuple)) or len(argumento_2) != 2):
        raise ValueError("El segundo argumento debe ser una lista o tupla de tamaño 2")
    else:
        raise TypeError("Se esperaba un argumento de tipo int y opcionalmente un argumento de tipo list o tuple de tamaño 2")

complejo= valComplex()
print(complejo)








def valList(argumento_1, argumento_2=None, argumento_3=None):
    if argumento_3 is None:
        # Se pasa solo un argumento
        return isinstance(argumento_1, list)
#Comprueba si el segundo argumento es una lista y si el tercer 
# argumento es una cadena. Si no, la función devuelve False
    else:
        if isinstance(argumento_2, list) and isinstance(argumento_3, str):
            if argumento_3 == 'value':
                return argumento_1 == argumento_2
            elif argumento_3 == 'len':
                return len(argumento_1) == argumento_2
            else:
                raise ValueError("El tercer argumento debe ser 'value' o 'len'")
        elif isinstance(argumento_2, int) and isinstance(argumento_3, str):
#Comprueba si el valor del tercer argumento es value o len. Si no, la función devuelve False
            if argumento_3 == 'len':
#Comprueba si los elementos de las dos listas son iguales. Si son iguales,
#  la función devuelve True. Si no, la función devuelve False
                return len(argumento_1) == argumento_2
            else:
                raise ValueError("El tercer argumento debe ser 'len'")
        else:
            raise TypeError("Los tipos de los argumentos no son válidos")
lista=valList()
print( lista)
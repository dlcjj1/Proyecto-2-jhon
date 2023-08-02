print("La matriz")
print("=======Ingrese matrices cuadrada=====")

# primero se importa nummpy, para crear las matrices.
import numpy as np
Filas_de_a= int(input("filas:"))
columnas_de_a= int(input("columna:"))
Filas_de_b= int(input("filas:"))
columnas_de_b= int(input("columna:"))
# estos crea una matriz llena de ceros 
Matriz_1=np.zeros((Filas_de_a, columnas_de_a))
Matriz_2=np.zeros((Filas_de_b, columnas_de_b))

# se va llenando la matriz
print("introduce los elementos de la matriz 1")
for i in range(0,Filas_de_a):
  for j in range (0, columnas_de_a):
    Matriz_1[i,j]= input("ingrese los elementos:")

print("introduce los elementos de la matriz 2")
for i in range(0,Filas_de_b):
  for j in range (0, columnas_de_b):
    Matriz_2[i,j]= input("ingrese los elementos:")

print(Matriz_1)
print(Matriz_2)


# la funcion multiplica cada matriz, la columna de la 1 y la fila de 2 
def multiplicacon_de_matrices(Matriz_1, Matriz_2):
#si las matrices no son iguales sel un error
  if len(Matriz_1[0]) != len(Matriz_2):
    raise ValueError("Las dos matrices deben tener el mismo número de columnas.")

  Matriz_c = []
  for i in range(len(Matriz_1)):
    Filas_de_a = []
    for j in range(len(Matriz_2[0])):
      product = 0
      for k in range(len(Matriz_1[0])):
        product += Matriz_1[i][k] * Matriz_2[k][j]
      Filas_de_a.append(product)
    Matriz_c.append(Filas_de_a)

  return Matriz_c

Multiplica= multiplicacon_de_matrices(Matriz_1, Matriz_2)
print(Multiplica )


# Hacer la inversa atraves de una matriz identidad
print("=========== Gauss ==========")
import numpy as np
Filas_de_a= int(input("filas:"))
columnas_de_a= int(input("columna:"))


Matriz_3=np.zeros((Filas_de_a, columnas_de_a))


print("introduce los elementos de la matriz 3")
for i in range(0,Filas_de_a):
  for j in range (0, columnas_de_a):
    Matriz_3[i,j]= input("ingrese los elementos:")

import numpy as np

def gauss_jordan(Matriz_3):

# shape devuelve una tupla que contiene el número de filas
# el número de columnas y el número de dimensiones de la matriz
  n = Matriz_3.shape[0]

# Crea una matriz identidad de tamaño n
  Inversa = np.eye(n)

#  itera sobre las filas de la matriz Matriz_3
  for i in range(n):
    pivot = Matriz_3[i, i]
    if pivot == 0:
      raise ValueError("La matriz no es invertible.")

    Matriz_3[i] /= pivot
    Inversa[i] /= pivot
#recorre las columnas de la matriz y resta la fila actual
#multiplicada por el elemento de la columna actual de la matriz inversa de la fila actual.
    for j in range(n):
      if i != j:
        Matriz_3[j] -= Matriz_3[j, i] * Matriz_3[i]
        Inversa[j] -= Inversa[j, i] * Inversa[i]

  return Inversa

Invertir= gauss_jordan(Matriz_3)
print ("====La invertida ======")
print( Invertir)





print("=========== Producto vectorial ==========")

Numero_de_entrada_1= str(input("Aqui ingrese el numero_1 :"))
Numero_de_entrada_2= str(input("Aqui ingrese el numero_2 :"))

numero_1 = [int(digito) for digito in list(Numero_de_entrada_1)]
numero_2 = [int(digito) for digito in list(Numero_de_entrada_2)]
print(numero_1)
print(numero_2) 


def Producto_verctorial(numero_1, numero_2):
# Comprueba si los dos vectores tienen la misma longitud. Si no, levanta una excepción
  len(numero_1) == 3, "el primer  vector tiene que ser de longitud 3."
  len(numero_2) == 3, "el segundo  vector tiene que ser de longitud 3."
#Calcula el producto vectorial de los dos vectores. El producto vectorial se 
# calcula multiplicando los elementos de los dos vectores en orden alternado y sumando los productos.
  x = numero_1[1] * numero_2[2] - numero_1[2] * numero_2[1]
  y = numero_1[2] * numero_2[0] - numero_1[0] * numero_2[2]
  z = numero_1[0] * numero_2[1] - numero_1[1] * numero_2[0]

  return [x, y, z]
# devuelve el producto
producto= Producto_verctorial(numero_1, numero_2)
print("===== Producto vectorial===")
print( producto)




print("=========== Transpuesta ==========")
import numpy as np
Filas_de_a= int(input("filas:"))
columnas_de_a= int(input("columna:"))
Matriz_1=np.zeros((Filas_de_a, columnas_de_a))
print("introduce los elementos de la matriz 1")
for i in range(0,Filas_de_a):
  for j in range (0, columnas_de_a):
    Matriz_1[i,j]= input("ingrese los elementos:")
print(Matriz_1)

def transposicion_de_matriz(Matriz_1):
  
# Crea una matriz vacía para almacenar la matriz transpuesta.
  transposicion_de_matriz = []

#Itera sobre las filas de la matriz de entrada
  for i in range(len(Matriz_1[0])):
    transposicion_de_fila = []

#Para cada fila, itera sobre las columnas.
    for j in range(len(Matriz_1)):
      transposicion_de_fila.append(Matriz_1[j][i])
#Añade el elemento de la matriz de entrada a la matriz transpuesta
    transposicion_de_matriz.append(transposicion_de_fila)

  return transposicion_de_matriz 
transponer= transposicion_de_matriz(Matriz_1)
print("===== Transpuesta ===")
print (transponer)




print("=========== Sistema lineal ==========")
import numpy as np

Filas_de_a = int(input("filas:"))
columnas_de_a = int(input("columnas:"))

Matriz_1 = np.zeros((Filas_de_a, columnas_de_a))

print("introduce los elementos de la matriz 1")
for i in range(0, Filas_de_a):
  for j in range(0, columnas_de_a):
    Matriz_1[i, j] = input("ingrese los elementos:")


Numero_de_entrada_1 = str(input("Aqui ingrese el numero_1 :"))
numero_1 = [int(digito) for digito in list(Numero_de_entrada_1)]

print(Matriz_1)
print(numero_1)


def Sistema_linael_de_ecuaciones(Matriz_1, numero_1):
# Comprueba si la matriz y el vector tienen el mismo número de filas
  Matriz_1.shape[0] == len(numero_1), "La matriz_1 y el vector 1 tienen que tener el mismo numero de filas."
# Calcula la inversa de la matriz
  I = np.linalg.inv(Matriz_1)
#Multiplica la inversa de la matriz por el vector
  Vectro_solucion = I @ numero_1
# devuelve el vector solucion 
  return Vectro_solucion

resolver = Sistema_linael_de_ecuaciones(Matriz_1, numero_1)
print("===== Sistema lineal  ===")
print(resolver)






print("=========== Determinante ==========")

import numpy as np

Filas_de_a= int(input("filas:"))
columnas_de_a= int(input("columna:"))

Matriz_1=np.zeros((Filas_de_a, columnas_de_a))

print("introduce los elementos de la matriz 1")
for i in range(0,Filas_de_a):
  for j in range (0, columnas_de_a):
    Matriz_1[i,j]= input("ingrese los elementos:")


print(Matriz_1)



def determinante(Matriz_1):
# Comprueba si la matriz es cuadrada. Si no, levanta una excepción
  if len(Matriz_1) != len(Matriz_1[0]):
    raise ValueError("La matriz tiene que ser cuadrada.")

  if len(Matriz_1) == 1:
    return Matriz_1[0, 0]

  if len(Matriz_1) == 2:
    return Matriz_1[0, 0] * Matriz_1[1, 1] - Matriz_1[0, 1] * Matriz_1[1, 0]
# Calcula el determinante de la matriz
  determinante = 0
  for i in range(len(Matriz_1)):
    iniciar = (-1)**i
    submatriz = np.concatenate((Matriz_1[j][:i], Matriz_1[j][i+1:]))
    determinante += iniciar * Matriz_1[i, 0] * (submatriz)

  return determinante

Determinate = determinante(Matriz_1)
print("Determinante ===")
print(Determinate)

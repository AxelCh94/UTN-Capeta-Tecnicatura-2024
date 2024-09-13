# Las listas es lo que se conoce como otros lenguajes como arreglos o vectores


# 'Maradona' : 10  Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict (key , value)
diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (Key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrolo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un boleando

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar elementos
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear() # quedando vacio el {}
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro

# Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2 # concatenacion
print(lista3)

#
lista3.extend([7, 8, 9]) # sumamos las lista1 + lista2
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0))  esto daria error por no ser el elemento parte de la lista

# Como saber cuantos valotes repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

# Metodo de ordenamiento, en python es una funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordenada descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertit de tuplas a lista y de lista a tuplas
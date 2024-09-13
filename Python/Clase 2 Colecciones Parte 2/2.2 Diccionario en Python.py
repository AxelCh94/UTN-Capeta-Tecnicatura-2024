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

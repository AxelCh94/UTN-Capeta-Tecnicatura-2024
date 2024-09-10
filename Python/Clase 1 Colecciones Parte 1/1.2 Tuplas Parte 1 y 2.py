# Eliminar el ultimo elemento
#nombres.pop()
#print(nombres)

# Eliminar un indice especifico
#del nombres[2] # del significa delete (eliminar)
#print(nombres)

# Eliminar, borrar o limpiar todos los elementos
# nombres.clear()
#print(nombres)

# Eliminar la lista
# del nombres
# print(nombres) # Aqui nos mostrara un error


# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando /n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista [0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina esto es para eliminar la tupla

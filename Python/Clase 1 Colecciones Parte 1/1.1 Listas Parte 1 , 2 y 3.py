# lista = Axel , Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo", "Lily", "Axel"]
print(nombres)
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indice a mostrar 0, 1, 2

# Desde el indice indicador hasta el final
print(nombres[1: ])

# Modificar un valor
nombres[2] = "Liliana"
print(nombres)
nombres[0] = "Natalia"
print(nombres)

#Iterar una lista
for nombre in nombres: # nombres es singular, la lista es plurar
    print(nombres)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos parametros la lista

# Agregamos un elemento a la lista
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elementos
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice espesifico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres) # Aqui nos mostrar un error

#Agrego Test de GitHub
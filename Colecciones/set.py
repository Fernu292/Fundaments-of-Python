#no mantienen ningun orden en el conjunto de elementos

#set es una coleccion sin orden y sin indices, no permite elementos 
#repetidos y los elementos no se pueden modificar, pero si 
#agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}

print(planetas)
#largo

print(len(planetas))
#revisar si un elemento esta presente

print("Marte" in planetas)

#agregar 
 
planetas.add("Tierra")

print(planetas)

#eliminar

planetas.remove("Tierra")
print(planetas)

#eliminar con discard

planetas.discard("Jupiter")
print(planetas)

#limpiar el set

planetas.clear()
print(planetas)

#eliminar el set

del planetas
print(planetas)

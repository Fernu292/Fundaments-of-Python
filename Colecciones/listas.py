nombres = ["Juan", "Karla","Ricardo","Maria"]
print(nombres)

#conocer el largo de una lista
print(len(nombres))

# elemento 0

print(nombres[0])
print(nombres[3])

#navegacion inversa

print(nombres[-1]) #solicita el ultimo elemento de la lista 
print(nombres[-2]) #solicita el penultimo elemento de la lista 

#imprimir rango 
print(nombres [0:2])#sin incluir el indice 2 
#imprimir los elementos de inicio hasta indice proporcionado

print(nombres[:3])#sinnincluir el indice 3

#imprimir los elementos hasta el final desde el indice proporcionado

print(nombres[1:])

#cambiar elementos de una lista 

nombres[3] = "Ivone"

print(nombres)

#iterar lista con un ciclo for 

for nombre in nombres:
    print(nombre)
    
#revisar elementos en una lista

if "Carla" in nombres:
    print("Karla si existe en la lista")
else:
    print("El elemento buscado no esta en la lista")
    
#Agregar nuevo elemento en la lista

nombres.append("Lorenzo")
print(nombres)

#insertar un nuevo elemento en el indice proporcionado 

nombres.insert(1, "Octavio")
print(nombres)

#remover elemento de la lista

nombres.remove("Octavio")
print(nombres)

#remover ultimo elemento de la lista

nombres.pop()
print(nombres)

#remover el indice indicado de la lista 

del nombres[0]
print(nombres)

#limpiar elementos de la lista 

nombres.clear()
print(nombres)

#eliminar lista por completo 

#del nombres
#print(nombres)
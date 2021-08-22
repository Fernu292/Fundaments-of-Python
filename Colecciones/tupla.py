#Tupla mantiene el orden, pero no se puede modificar (inmutable)

frutas = ("Naranja", "Platano", "Guayaba")

print(frutas)

#largo de la tupla

print(len(frutas))

#acceder a elemento particular 

print(frutas[0])

#navegacion inversa

print(frutas[-1])
#rangos 
print(frutas[0:2])#excluyendo indice 2

#convertir un tupla a lista 

frutasLista = list(frutas)
frutasLista[1]="Platanito"

#convertir lista a tupla

frutas = tuple(frutasLista)
print(frutas)

#iterar tupla

for fruta in frutas:
    print(fruta, end=" ")#el end es para evitar el salto de linea 
    
#no se pueden agregar ni eliminar elementos de una tupla 
#solo se eliminan las tuplas 

#del frutas # el del borra la variable 
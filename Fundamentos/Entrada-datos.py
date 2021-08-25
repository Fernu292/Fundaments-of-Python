
#Para poder tomar datos como un input de un usuario podremos hacerlo 
#al igualar la variable donde guardaremos el dato 
#a un input() en este podremos mostrar un mensaje que le diga al usuario
#que hacer


dato = input("Ingresa un dato: ")
print(f'El dato es: {dato}')


#Input() con tipo del dato, si queremos tomar especificamente un tipo de
#dato lo haremos con la funcion del mismo nombre del tipo de dato 


#Tipo entero
numero = int(input('Digita un numero: '))
print(f'El numero es: {numero}')

#Tipo string 

mensaje = str(input("Digita un mensaje: "))
print(f'El mensaje es: {mensaje}')
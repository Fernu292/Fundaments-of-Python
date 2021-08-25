
#Las cadenas o strings son arrays de caracteres, y podemos acceder
#a sus elementos como un array normal, ademas de esto podemos concatenar 
#datos con numeros u otros strings


#Declaracion de un string 
cadena = "Aerosmith"


#Concatenar un string con otro
print("Mi grupo favorito es: " + cadena)


#Cuando los numeros se declaran como string solo los puedes concatenar 
numero1 = "1"
numero2 = "2"

print("concatenacion "+ numero1 +numero2)

#En cambio si lo declaras como entero se puede hacer suma 
#Y operaciones aritmeticas  
num1 = 1
num2 = 2

print("operacion de suma ", num1+num2)


#El f string es una forma de concatenar datos o variables con strings 

print(f'El primer numero es: {num1}')
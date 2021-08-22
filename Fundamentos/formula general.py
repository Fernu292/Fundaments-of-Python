from math import sqrt #importa la funcion a utilizar para el codigo 
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A) # Solucion positiva 
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A) #Solucion negativa 
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)
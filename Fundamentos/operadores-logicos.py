#a = int(input("Proporciona un valor: "))
a =3 
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a<=valorMaximo)
#print(dentroRango)

if(dentroRango):
    print("Dentro de rango")
else:
    print("Fuera de rango")
    

vaciones = True 
diaDescanso = False
if( not(vaciones or diaDescanso)):
    print("Tienes deberes que hacer")
else:
    print("Puedes ir al parque")
    
print(not (vaciones))
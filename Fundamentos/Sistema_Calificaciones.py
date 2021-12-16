print("***Pograma que calcula el promedio de un alumno***")

def promediar(pro,mat, fis, tec, red):
    return (pro+mat+fis+tec+red)/5



Cpro = int(input("Introduzca la calificacion de Programacion: "))
Cmat = int(input("Introduzca la calificacion de Matematicas: "))
Cfis = int(input("Introduzca la calificacion de Fisica: "))
Ctec = int(input("Introduzca la calificacion de Tecnologia: "))
Cred = int(input("Introduzca la calificacion de Redaccion: "))

promedio = promediar(Cpro, Cmat, Cfis, Ctec, Cred)

print(f'Tu promedio es: {promedio}')

if promedio == 5 or promedio<=6:
    print('Mal promedio')
    
elif promedio<=70:
    print("Promedio regular")
elif promedio<=80:
    print('Promedio suficiente')
elif promedio >= 9 or promedio ==10:
    print("Promedio excelente") 
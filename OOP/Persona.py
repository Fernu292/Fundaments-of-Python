
#Declaracion de una clase con la palabra reservada class 
class Persona:

    def __init__(self, nombre, apellido, edad):
    #El metodo __init__ permite inicializar objetos
        #Atributos de instancia para objetos
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad



#crear objeto de clase
# nombre = str(input('Digite su nombre: '))
# apellido = str(input('Digite su apellido: '))
# edad = int(input('Digite su edad: '))

persona1 = Persona('Luis Fernando', 'Nunez', 18)

persona1.nombre = 'Fernan'

print(f"\nEl nombre es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}")


persona2 = Persona('Maria', 'Perez', 28)

print(f'\nEl nombre es: {persona2.nombre} {persona2.apellido} y su edad es: {persona2.edad} ')
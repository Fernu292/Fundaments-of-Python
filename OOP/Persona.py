class Persona:

    def __init__(self, nombre, apellido, edad):
    #El metodo __init__ permite inicializar objetos
        #Atributos de instancia para objetos
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad



#crear objeto de clase
nombre = str(input('Digite su nombre: '))
apellido = str(input('Digite su apellido: '))
edad = int(input('Digite su edad: '))

persona1 = Persona(nombre, apellido, edad)


print(f"El nombre es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}")
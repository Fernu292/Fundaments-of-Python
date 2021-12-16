def mi_funcion(nombre, apellido):
    print("Saludos desde mi funcion")
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Luis', 'Fernando')

#def es una palabra reservada para declarar funciones 

#funcion de suma

def suma(a,b):
    return a+b #regresa el resultado de la suma 

resultado = suma(4, 67) 

print(resultado)


#funcion que busca una palabra en un texto 

text = input()
word = input()

def search(text, word ):
    if word in text:
        print('Word found')
    else:
        print('Word not found')
search(text, word)
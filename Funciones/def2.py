def suma(*args):# para pasar una tupla de valores a una funcion agregamos un *
    resultado = 0
    
    for valor in args:
        resultado+= valor
    return resultado

print(suma(3,5,9))


def mult(*args):
    producto = 0
    
    for i in args:
        producto*=i
    return producto
print(mult(3,4,5))



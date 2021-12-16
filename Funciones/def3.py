
def listarTerminos(**terminos):#Los ** permiten pasar como parametro un diccionario 
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
        
listarTerminos(IDE = 'Integrated developement enviroment', PK = 'Primary key')
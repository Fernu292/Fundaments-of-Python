frase  =  input()


def resolve(s):
    frase  = s.split()
    
    for i in range( len(frase) ):
        frase[i] = frase[i].capitalize()
        i+=1
    
    respuesta = ' '.join(frase)
    
    return respuesta 
        

print(resolve(frase))
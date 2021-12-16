#Crate an union bewtween two arrays 

n = input()
queries = list( map(int, input().split()))#llenar una lista en una sola linea
n = input()
queries2 = list( map(int, input().split()))


def unilistas( list1, list2):
    querie = list1+list2
    
    result = list(set(querie))#set para eliminar datos repetidos 
    result.sort()#ordenar lista de menor a mayor
    return len(result)

print(unilistas(queries, queries2))

n = int(input())
lista = []
for i in range(n):
    comant = input().split()
    
    if comant[0] == 'insert':
        numbers = comant[1], comant[2]
        lista.insert(int(comant[1]), int(comant[2]))
    elif comant[0] == 'print':
        print(lista)
    elif comant[0] == 'remove':
        number = int(comant[1])
        lista.remove(number)
    elif comant[0] == 'append':
        number = int(comant[1])
        lista.append(number)
    elif comant[0] == 'sort':
        lista.sort()
    elif comant[0] == 'pop':
        lista.pop()
    elif comant[0] == 'reverse':
        lista.reverse()
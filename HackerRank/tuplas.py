n = int(input())

l = list( map(int, input().split()) ) 
t = tuple(l)
result = hash(t)

print(result)

from collections import Counter
import collections

numShoes = int(input())

shoes = Counter(map(int, input().split()))

numCost = int(input())

total = 0

for i in range(numCost):
    size, price = map(int, input().split())
    
    if(shoes[size]):
        total+= price
        shoes[size]-=1
print(total)
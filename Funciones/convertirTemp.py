celc = int(input())
far = int(input())



def celcius(f):
    return (5/9)*(f-32)


def faren(c):
    return (9/5)*c+32


cel = celcius(far)
fare = faren(celc)


print(cel)
print(fare)

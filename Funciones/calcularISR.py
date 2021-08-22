

def calcular_total(sinImpuesto, impuesto):
    impuesto  = (sinImpuesto/100)*impuesto
    
    total = sinImpuesto + impuesto
    
    return total


pago = float(input())
ISR = float(input())

total = calcular_total(pago, ISR)

print(total)
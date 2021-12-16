print("Proporcione los siguientes datos del libro")

nombre = input("Proporcione el nombre:")
id = int(input("Proporcione el ID:"))

precio = float(input("Proporcione el precio:"))

envioGratuito = input("Indica si el envio es gratuito (True/False):")

if (envioGratuito == "True"):
    envioGratuito==True
elif (envioGratuito==False):#es para validar dos casos ahorrando if else
    envioGratuito==False
else:
    envioGratuito = "Valor incorrecto, ingrese (True/False)"

print("nombre:", nombre)
print("ID:", id)
print("Precio: ", precio)
print("Envio gratuito?:", envioGratuito)

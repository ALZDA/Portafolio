dolares= input("¿Cuántos dólares tienes?:")
dolares = float(dolares)
valor_peso = 0.054
peso = dolares / valor_peso
peso = round(peso, 2)
peso = str(peso)
print("Tienes $" + peso + " MXN")
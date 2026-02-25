#a partire da una lista di temperature, creare una nuova lista con le temperature superiori a 20.

temperature = [18,22,30,12,15,32,27,19,28,20]
#creare collection, non modificare, operatore di confronto, utilizzare append
temperature_sopra_20 = []

for temperatura in temperature:
    if temperatura > 20:
        temperature_sopra_20.append(temperatura)
print(temperature_sopra_20)
#questa è operazione di filtraggio
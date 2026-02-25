numeri = [3,6,9,12,15,18,21,24,27,30]
#creare un dizionario
#chiave deve essere il numero
# valore --> il numero diviso 3
nuova = {n : n/ 3 for n in numeri}
print(nuova)

nomi = ['Anna,' 'Ciccio', 'Francesca', 'Annibale']
#creare un dizionario
# chiave --> nome
#valore --> 'Lungo' se la lunghezze è maggiore di 5, altrimenti 'Corto'
nuova_nomi ={nome: 'Lungo' if len(nome) > 5 else 'Corto' for nome in nomi}
print(nuova_nomi)

"""
#scrivere una pipeline (4 funzioni) che
- riceve una lista di stringhe numeriche (numeri come stringa)
- li converte in interi gestendo gli errori 
- restituisce solo i > 10
- calcolo la somma (sum(list))
quando usiam except dentro il for mettiamo pass
"""

#conversione da stringhe a numeri
def converti(lista):
    numeri = []
    for n in lista:
        try:
            numeri.append(int(n))
        except ValueError:
            pass
    return numeri

def filtra(lista):
    return [n for n in lista if n > 10]

def somma(lista):
    return sum(lista)

def main():
    dati = ['4', '12', '31', '1', '3', '21', 'trenta']

    numeri = converti(dati)
    filtrati = filtra(numeri)
    risultato = somma(filtrati)

    print("Somma:", risultato)

main()


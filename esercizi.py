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


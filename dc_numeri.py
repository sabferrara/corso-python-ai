studente = {
    'name':'Anna',
    'age':22,
    'corso': 'Python'
}

"""
se la lista è una sequenza di oggetti, la dict è un armadio con i nostri cassetti 
"""
num = [10,20,30]  #qua abbiamo numeri
#num_d = {         #qua chiavi
#    'a':10,
#    'b':20,
#    'c':30,
#}

#se ho la mia lista, e voglio creare un dizionario con il doppio.

quadrati =[]

for n in num:
    quadrati [n] = n * n  #uso il valore n come chiave
print(quadrati)
#facciamo la comprehension
quadrati_c = {n: n * n for n in num}
print(quadrati_c)

"""
{chiave: valore for elemento in sequenza} #per pgni iterazione di questo ciclo for avremo la coppia chiave in 
questo caso chiave n e valore n*n
"""


numeri = [1,2,3,4]

#voglio moltiplicare tutto per 2

#nuovi = []

#for n in numeri:
 #   numeri.append(n)
  #  pass

#senno anche con list comprehension

# nuovi =[n * 2 for n in numeri]

#introdurre numpy
import numpy as np
#trasformiamo i numeri in un array
array = np.array(numeri)
nuovi = array * 2
numeri_random =np.random.randint(1,101,10)
print(np.mean(numeri_random))


print(nuovi)

""""
numeri_random =np.random.randint(1,101,10)
np.mean --> media
np..max --> 
"""

"""
ESERCIZIO: array numerico casuale tra 1 e 100
calcolare la media, massimi, moltiplicare tutto per 3 e filtrare i numeri maggiori di 50
"""

numeri_random= np.random.randint(1,101,10)

np.mean(numeri_random)
np.max(numeri_random)

print(numeri_random * 3)

print(numeri_random[numeri_random > 50])  #per filtrare


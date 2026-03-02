import numpy as np

x = 5 #singolo numero, nessuna dimensione

v= np.array([1,2,3,4,5]) #vettore monodimensionale
print(v.shape)

m = np.array([   #array bidimensionale
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(m.shape)

t = np.array([   #TENSORE 3D: array tridimensiona,e con 2 blocchi, ogni blocco ha 2 righe e 2 colonne
    [
        [1,2],
        [3,4],
    ],
    [
        [5,6],
        [7,8],
    ]
])
print(t.shape)

#ogni dimensione aggiunge un contesto

a= np.array([1,2,3,4,5])
b = 10 #è uno scalare

print(a+b) #lo adatta alla dimensione dell'array

"""
[1,2,3] + [10,10,10] 
vede che b è uno scalare che non ha dimensione. adotta B alla dimensione di A, ma andando ad effetturare
questa operazione senza mantenerla in memoria [10,10,10] --> broadcasting
"""

c = np.array(    #bidimensionale
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

media = np.mean(c, axis=0)
norm = c - media
print(norm)
d = np.array( [10,20,30])
#crea array virtuali andando a leggere in broadcasting la somma di 1+10, 2+20, 3+30, finisce l'array e ricominica
print(c+d)

f = np.array( [1,2,3,4,5,6])
#per lavorare meglio questo set di dati, lo trasformo in una matrice:
e = np.array([
    [1,2,3],
    [4,5,6],
])
#se ho 6 elementi posso fare una matrice 2x3 o 3x2 6x1 o 1x6, l'importante è rimanere con lo stesso numero di elementi
g = f.reshape(2,3)
print(g)

h = np.array( [1,2,3,4,5,6,5,6,4,3,2,4,5,6,7,5,4,2,1,3,5])
i = h.reshape(3,-1)   # - 1 ci calcola in automatico la dimensione mancante
print(i)

l = np.array( [1,2,3,4,5,6,5,6,4,3,2,4,5,6,7,5,4,2,1,3,5])
n = l[0:2]
n[0] = 99
print(n)
print(l)  #ho modificato l'array principale perchè n non è una copia, è una vista di l.
# per poter creare una copia sulla quale lavorare, utilizziamo copy
o = l[0:2].copy()
print(o)
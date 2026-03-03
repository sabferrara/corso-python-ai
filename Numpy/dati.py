import numpy as np

dati = np.array([
    [34,167,70],
    [37,185,92],
    [22,173,65]
])
#rappresentano eta, altezza, peso

print(dati.shape)
print(dati[:0]) #se voglio prendere tutte le righe delle colonna zero

media= np.mean(dati, axis = 0) #creo una media per colonna
print(media)    #se mettessi axis=1 mi da la media per riga che non mi interessa

eta = dati[:,0] #prendo tutte le eta

import numpy as np

dataset = np.random.uniform(0,100,(5,4))
print (dataset)  #ogni riga rappresenta una persona, ogni colonna l'eta, l'altezza, peso, punteggio

"""
#obiettivo, normalizzare le ultime 3 colonne
#aggiungere nuova colonna con le feature
#copia del dataset e verificare che non venga alterata
"""

#creiamo una copia di sicurezza
dataset_originale = dataset.copy()

#normalizziamo ultime 3 colonne, quindi quelle con indice 1 2 3
features = dataset [:, 1:]
print(features)

minimo =np.min(features, axis=0)
massimo = np.max(features, axis=0)
features_norm = features - minimo/ (massimo-minimo)   #broadcasting

print(features_norm)

#sostituire l'output, quindi normalizzate, al dataset iniziale. lo faccio dicendogli di prendere le posizione del dataset
#sostituendole con queste altre cose

dataset[:,1:] = features_norm

print(dataset)

#voglio calcolare la media delle feature per ogni riga
media_feature = np.mean(dataset[: ,1:], axis =1)
media_feature =  media_feature.reshape(-1,1) #voglio aggiungere questa colonna al dataset

dataset_con_media = np.hstack((dataset, media_feature)) #vuol dire che aggiungi la media delle feature al dataset
print(dataset)


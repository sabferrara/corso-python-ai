import numpy as np

punteggi = np.array([23,46,78,56,98,34,65,32,67,45,20])

#se in py avessi una lista del genere e volessi calcolare gli studenti sopra la media,
#prima calcolo la media e poi filtrare tutti gli steudenti sopra. Poi dovrei normalizzare
#i punteggi tra 0 e 1.

media = np.mean(punteggi)   #mean è una funzione aggregatrice che mi da 1 solo numero
print(type(punteggi))
print(type(media)) #è un float gestito da numpy, quindi ha un comportamento diverso.

sopra_media = punteggi >  media  #maschera booleana, quindi prima stampiamo il tipo di punteggi
print(sopra_media) #ottengo una maschera booleana che tramite delle operazioni vettoriali
# mi fa il confronto elemento per elemento
#per contare quanti sono i voti sopra la media mi basta andare a contare quanti sono i ture nell'array
numero_sopra_media = np.sum(sopra_media)
print(numero_sopra_media)
pc = (numero_sopra_media / len(punteggi)) * 100 #percentuale
print(pc)  #45% degli studenti ha il puntegio sopra la media


minimo = np.min(punteggi)
massimo = np.max(punteggi)

normalizzati =(punteggi - minimo)/(massimo - minimo)
print(normalizzati)


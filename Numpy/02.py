import numpy as np

#matrice
studenti =np.array([
    [80,79,90],
    [60,75,90],
    [88,93,90],
    [55,60,70]
])

"""
ogni riga è uno studente,
ogni colonna è una materia

Calcola:
media per studente
media per materia
studenti con media > 75
normalizzare il dataset
"""
media_studente = np.mean(studenti,axis=1)
media_materia = np.mean(studenti,axis=0)

media_alta = media_studente > 75  #maschera booleana
studenti_sopra_media = studenti[media_alta]

minimo = np.min(studenti)
massimo = np.max(studenti)

normalizzati =(studenti - minimo)/(massimo - minimo)

print(media_studente)
print(media_materia)
print(media_alta)
print(studenti_sopra_media)
print(normalizzati)
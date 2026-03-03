import pandas as pd

dati = {
    "nome": ['Ciccio', 'anna', ' Marcelolo', 'Francesca', 'PAOLO'],
    "email": ['ciccio@email.it', 'anna@email.com', 'marcello@redyard.com', 'francesca@gmail.com', 'paolo@paolo.it'],
    "eta": [25,22,38, 20, 21],
    "stipendio": [1200,1800, 1900, 2100, 1750],
    'citta': ['Roma','Milano', 'Firenze', 'Roma', 'Roma'],
    'categoria': ['A','A','B','A', 'B'],
    'vendite': [240,250,190,310,370]
}

df = pd.DataFrame(dati)

#raggruppare vendite per città
print(df.groupby('citta')['vendite'].sum())  #raggruppo per una serie, vedo quale voglio controllare e sommo

#vogli vedere la categoria che ha venduto di piu
print(df.groupby('categoria')['vendite'].sum())
print(df)

print(df.groupby('categoria', 'citta')['vendite'].sum())

#tramite la EDA vediamo come sono formati questi dati, cosa ci dicono in modo da arricchire il nostro bias cognitivo quando creiamo un modello
#da dare al machine learning, dovremmo gia sapere quello che vogliamo ottenere

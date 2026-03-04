"""
trasformare feature per ogni parola per vedere quante volte appare.
nel conteggio delle parole quelle rarissime contano di piu, quelle piu comuni meno.
Sommo i punteggi delle sngole parole, se il punteggio è alto sono simili.
embedding --> modello che trasforma in vettori semantici, con risultati migliori, ma servono tante librerie e modelli
"""
from sklearn.metrics.pairwise import cosine_similarity

#il testo viene tokenizzato: cioe spezzato in parti piu piccole, la ricerca si concentrerà sui token
#delle stringhe, quindi non possiamo trattarli come stringhe numeriche.
#elastic riesce a trovare dei testi simili con un forte grado di accuratezza

"""
andare a creare una colonna (soup) che mi vada a concatenare director + cast + genere + description
per garantire in base alle 4 features quali sono i titoli consigliati
soup (tutta in una stessa stringa sullo stesso rigo):
modello TF IDF
'spiegami come posso fare un modello di predizione con soup e modello ft/idf ...'

"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('NetFlix.csv')

pd.options.display.max_columns = 20
print('Film totali:',len(df))

#per pulire i dati tutto in minuscolo e senza spazi
features = [
    'director',
    'cast',
    'genres'
]

for feature in features:
    df[feature] = df[feature].fillna("").astype(str).str.lower().str.replace(' ', '')

# Per la descrizione: solo minuscolo, ma MANTENIAMO gli spazi
df['description'] = df['description'].fillna("").astype(str).str.lower()

def soup(x):
    return x['director'] + ' ' + x['cast'] + ' ' + x['genres'] + ' ' + x['description']

df['soup'] = df.apply(soup, axis=1)

print("--- Anteprima della colonna SOUP ---")
print(df['soup'].head())

# 3. MODELLO TF-IDF (facendo diventare il testo un vettore di numeri (una coordinata nello spazio)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['soup'])

model = NearestNeighbors(n_neighbors=11, metric='cosine')
model.fit(tfidf_matrix)


# 4. CALCOLO SIMILARITÀ
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Indice inverso per trovare i film dal titolo
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# 5. FUNZIONE RACCOMA
def recommend_by_title(
        title:str,
        k: int = 10
) -> pd.DataFrame:
    idx = indices[title]

    # Prendiamo il vettore TF-IDF del film scelto
    seed_vector = tfidf_matrix[idx]

    #prendiamo i film piu vicini nello spazio
    distances, neighbor_indices = model.kneighbors(seed_vector)

    # Recuperiamo le righe dal dataset originale (escludendo il primo che è se stesso)
    recs = df.iloc[neighbor_indices[0]].copy()
    recs = recs[recs['title'] != title]

    columns = ['title', 'director', 'cast', 'genres']

    return recs[columns].head(k)

test =  ('Robin Hood: The Rebellion')
print(f"Film di riferimento: {test}\n")

risultati = recommend_by_title(test, k=10)
print("Ecco i 10 titoli consigliati per te:")
print(risultati)



"""
dobbiamo creare un algoritmo che ci dia una top 10 di canzoni che potrebbero piacerci
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors  #va a cercare le 10 canzoni piu vicine a quella che passiamo


pd.options.display.max_columns = 20

df = pd.read_csv('dataset.csv')

#print(df)
#print(len(df))

print('Righe totali:',len(df))
print('Tracce Uniche:',df["track_id"].nunique())

#vediamo quanto è sporco il dataset. Capire i missing value,
missing = df.isna().sum().sort_values(ascending=False)  #isna controlla le cose che sono Nan
print(missing)

#valori che mancano
missing_values = df.isnull().sum()
print(missing_values)

#vediamo le feature che utilizzeremo
features_num = [
    "energy",
    "tempo",
    "valence",
    "acousticness"
]
print(df[features_num].describe())

genre_ohe = pd.get_dummies(df["track_genre"], prefix = 'genre') #ONE HOT ENCODING
print(genre_ohe.shape)

#rimuoviamo i duplicati
df = df.sort_values('popularity', ascending = False)
df = df.drop_duplicates(subset = ['track_id'], keep = 'first')

genre_ohe = pd.get_dummies(df["track_genre"], prefix = 'genre') #ONE HOT ENCODING
print(genre_ohe.shape)

X_num = df[features_num]  #features numeriche
X = pd.concat([X_num, genre_ohe], axis =1)  #mi vai a concatenare due serie,
# aggiungendo alla matrice features_num anche il genere
print(X.shape)

#normalizziamo
scaler = StandardScaler()  #ogni colonna è una dimensione, in questo caso ne abbiamo prese 4
# e abbiamo 4 dmensioni

X_num_scaled = scaler.fit_transform(X_num)  #serve solo per X_num,

X_final = np.hstack((X_num_scaled, genre_ohe.values))


model = NearestNeighbors(
    n_neighbors=10 + 1,
    metric = 'euclidean'
)

model.fit(X_num_scaled)  #fit indicizza, memorizza i punti nello spazio e definisce una struttura
# per cercare le canzoni vicine (che hanno coordinate piu vicina) piu velocemente

#dopo aver fatto il modello, andiamo a trovare la traccia di raccomandazione

#vediamo quanti generi abbiamo facendo ONE HOT ENCODING
print(df["track_genre"].nunique())

#funzione di raccomandazione, noi passiamo il tack id e lui ci trova le canzoni piu simili

def reccomend_by_track_id(
        track_id : str,
        k: int =10,
        same_genre: bool = False  #se vogliamo ottenere canzoni dello stesso genere
) -> pd.DataFrame:

    seed = df[df["track_id"] == track_id]
    if seed.empty:
        raise ValueError("Track ID desn't exist")

    seed_row=seed.iloc[0]#prende tutta la riga della canzone in base all'id che andiamo a passare

    seed_num= seed[features_num] #facciamo passare le features numeriche
    seed_num_scaled = scaler.transform(seed_num) #e poi le scaliamo (le features) che usiamo come punto di riferimento

    seed_genre = seed_row["track_genre"]
    seed_genre_ohe = np.zeros((1, genre_ohe.shape[1]))

    genre_col_nome = f"genre_{seed_genre}"

    if genre_col_nome in genre_ohe.columns:
        idx = list(genre_ohe.columns).index(genre_col_nome)
        seed_genre_ohe[0,idx] = 1

    #mi creo il vettore finale della seed
    seed_vec = np.hstack([seed_num_scaled, seed_genre_ohe])

    distances, idices = model.kneighbors(seed_vec) #va a cercare le canzoni con distanza meno alta (le piu vicine)

    #recuperiamo le righe da dataset originale raccomandazione
    recs = df.iloc[idices[0]].copy()

    recs = recs[recs["track_id"] != track_id] #eliminiamo da recs la traccia seed

    if same_genre:
        recs = recs[recs["track_genre"] == seed_genre["track_genre"]]

    recs = recs.head(k)

    cols = [
         'track_id',
         'track_name',
         'artists',
         'track_genre',
         'popularity',
    ]

    return recs[cols]

test_id = ""

print("Traccia seed: \n")
print(df[df["track_id"] == test_id][['track_name', 'artists']])

print('Tracce consigliate: \n')
print(reccomend_by_track_id(test_id, k=10, same_genre=False))


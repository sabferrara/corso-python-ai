import pandas as pd

dati = {
    "nome": ['Ciccio', 'Anna', 'Marcelolo', 'Francesca', 'Paolo'],
    "eta": [None,22,38, None, 21],
    "stipendio": [1200,1800, None, 2100, None]
}

df = pd.DataFrame(dati)
print(df.isnull())#per vedere quali dati vanno bene,
print(df.isnull().sum())

df.info()
print(df.dropna()) #rimuove righe con 1 NaN

#usiamo mean per replace di Nanìn
media_eta = df['eta'].mean()
df ['eta'] = df['eta'].fillna(media_eta) #posso dire di andare a sostituire tutte le eta mancanti con un valore standard

media_stipendio = df['stipendio'].mean()
df['stipendio'] = df['stipendio'].fillna(media_stipendio)
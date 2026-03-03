import pandas as pd

dati = {
    "nome": ['Ciccio', 'anna', ' Marcelolo', 'Francesca', 'PAOLO'],
    "email": ['ciccio@email.it', 'anna@email.com', 'marcello@redyard.com', 'francesca.com', None],
    "eta": [None,22,38, None, 21],
    "stipendio": [1200,1800, None, 2100, None]
}

df = pd.DataFrame(dati)
df['nome'] =df['nome'].str.strip().str.title()
df['email'] =df['email'].str.strip().str.lower()

df['eta'] = df['eta'].fillna(df['eta'].mean())
df['stipendio'] = df['stipendio'].fillna(df['stipendio'].mean())
df =df.dropna(subset=['email'])
df= df[df['email'].str.contains('@')]

df['eta'] = df['eta'].astype(int) #eta convertita in intero
print(df.info())

dati_2 = {
    "nome": ['Ciccio', 'anna', ' Marcelolo', 'Francesca', 'PAOLO'],
    "email": ['ciccio@email.it', 'anna@email.com', 'marcello@redyard.com', 'francesca.com', None],
    "eta": [None,'22',38, 'venti', 21],
    "stipendio": [1200,1800, None, 2100, None]
}

df1 = pd.DataFrame(dati_2)

#pulizia nome
df1['nome'] =df1['nome'].str.strip().str.title()
#pulizia email
df1['email'] =df1['email'].str.strip().str.lower()
df1 =df1.dropna(subset=['email'])  #elimin mil nane
df1= df1[df1['email'].str.contains('@')]  #elimina mail che non contengono@

#pulizia e popolamento dell'età con la media
df1['eta'] = pd.to_numeric(df1['eta'], errors='coerce')  #converte età in valore numerico con coerce me li trasforma direttanemtne in NaN
df1['eta'] = df1['eta'].fillna(df1['eta'].mean())
df1['eta'] = df1['eta'].astype(int)

##pulizia e popolamento dello stipendio con la media
df1['stipendio'] = df1['stipendio'].fillna(df['stipendio'].mean())



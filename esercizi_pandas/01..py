import pandas as pd

dati = {
    "nome": ['Ciccio', 'Anna', 'Marcelolo', 'Francesca', 'Paolo'],
    "eta": [None,22,38, None, 21],
    "citta": ['Roma', 'Milano', 'Firenze']
}

#definiamo in base ai dati che abbiamo un dataframe
df = pd.DataFrame(dati)
print(df)

df_filtrato = df[df['eta'] <30]
print(df_filtrazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzto)

df_2 = df[df['nome'] == 'Ciccio']
print(df_2)


'stipendio' : [1200,1800, None, 2100, None]
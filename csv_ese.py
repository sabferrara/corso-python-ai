import csv

with open('dati.csv',newline='') as f_input:  #prendere i dati, dall'input

    reader = csv.DictReader(f_input)#creo un reader
    utenti_modificati = [] #creo una lista di appoggio

    for row in reader: #itero su ogni riga del mio csv
        eta = int(row['eta']) # poi indico che l'eta deve essere un intero e poi applico la regola

        if eta >= 27:
            categoria = 'Senior'
        else:
            categoria = 'Junior'

        row['categoria'] = categoria
        utenti_modificati.append(row)

#ora apriamo modalità scrittura
with open('dati.nuovi.csv','w', newline='') as f_output:

    colonne =['nome', 'eta', 'citta', 'categoria']

    writer = csv.DictWriter(f_output, fieldnames = colonne)

    writer.writeheader()
    writer.writerows(utenti_modificati)








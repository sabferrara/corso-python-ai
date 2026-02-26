import csv
import json

utenti_validi = []
utenti_non_validi =[]

with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nome = row['nome'].strip()
        eta = row['eta'].strip()
        citta = row['citta'].strip()


#controllo i campi vuoti
        if not nome or not citta:
            utenti_non_validi.append(row)
        continue
#controllo eta numerica
    try:
        eta = int(eta)
    except ValueError:
        utenti_non_validi.append(row)
        pass

    if eta > 27:
            categoria = 'Senior'
    elif eta > 25:
            categoria = 'Mid'
    else:
            categoria = 'Junior'

    row['eta'] = eta
    row['categoria'] = categoria
    utenti_validi.append(row)

with open('utenti_validi.csv','w', newline = '') as f_out:
    colonne =['nome', 'eta', 'citta', 'categoria']
    writer = csv.DictWriter(f_out,fieldnames=colonne)

    writer.writeheader()
    writer.writerows(utenti_validi)

with open('utenti_non_validi.csv','w', newline = '') as f_out:
    colonne =['nome', 'eta', 'citta']
    writer = csv.DictWriter(f_out,fieldnames=colonne)

    writer.writeheader()
    writer.writerows(utenti_non_validi)

with open('user.json','w') as f_out:
    json.dump(utenti_validi,f_out)






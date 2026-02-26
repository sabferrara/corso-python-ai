import csv
import json

#funzione di validazione
def validate_row(row):
    #controllo che ci siano tutti gli elementi della riga
    try:
        if not row['nome'].strip():
            return False, 'Nome mancante'
        if not row['citta'].strip():
            return False, 'Citta mancante'

        eta = int(row['eta'])
        if eta < 0:
            return False, 'Eta mancante'
        return True, None

    except KeyError as e:   #ci potrebbe eessere un errore nella chiave
        return False, e
    except ValueError as e:
        return False, e
    except Exception as e:#prendo tutte le eccezioni possibili che possono esserci
        return False, e

#calcolo la categoria
def calculate_category(age):
    if age < 26:
        return 'Junior'
    elif age < 30:
        return 'Mid'
    else:
        return 'Senior'


#gestire la pipeline e creare òista di vaid users

valid_users = []
try:
    with open('users.csv', newline='') as f_input,\  #file lettura
         open('valid_users.csv','w',newline='') as f_valid_users,\    #file scrittura
         open('invalid_users.csv','w',newline='') as f_invalid_users:    #file scrittura
         #apro il reader
         reader =csv.DictReader(f_input)

         #aggiungo la categoria solo ai validi
         valid_fieldnames = reader.fieldnames + ['categoria']
         invalid_fieldnames = reader.fieldnames + ['errore']

         valid_writer = csv.DictWriter(f_valid_users, fieldnames=valid_fieldnames)
         invalid_writer = csv.DictWriter(f_invalid_users, fieldnames=invalid_fieldnames)

         valid_writer.writeheader()
         invalid_writer.writeheader()

         for row in reader:

             is_valid, error = validate_row(row) #is valid corrisponde al false o true, mentre error corrisponde all'errore che sto passand tipo nome o citta mancante, nel caso in cui lerrore non ce è None, quindi va avanti

             if is_valid: #se la riga è valida procedi
                 eta = int(row['eta'])
                 category = calculate_category(eta)
                 row['categoria'] = category

                 #scrivo le righe del valido,
                 valid_writer.writerow(row)

                valid_users.append({
                     'nome': row['nome'],
                     'citta': row['citta'],
                     'eta': eta,
                     'categoria': category,
                )}

             else:
                 row['errore'] = error  #segno errore nella colonna
                 invalid_writer.writerow(row)

except FileNotFoundError:
    print('File non esistente')
except Exception as e:
    print(e)

    #salvataggio file json
try:
    with open('valid_users.json', 'w') as f_valid_users_json:
        json.dump(f_valid_users, f_valid_users_json, index = 4)

except Exception as e:
    print(e)

print(Done)

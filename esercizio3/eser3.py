import csv
import json

users_validi = []

with open("requests.csv", newline='') as file_input:
    reader = csv.DictReader(file_input)

    # funzione di validazione
    for row in reader:
        id = row['id'].strip()
        nome = row['nome'].strip()
        email = row['email'].strip()
        eta = row['eta'].strip()
        servizio = row['servizio'].strip()

        try:
            eta = int(eta)
        except ValueError:
            continue

        if '@' not in email or eta < 18 or nome == '':
            continue
        users_validi.append(row)

    richiesta_pulite =[]
    for row in users_validi:
        id = row['id']
        nome = row['nome'].strip().title()
        email = row['email'].strip().lower()
        eta = int(row['eta'].strip())
        servizio = row['servizio'].strip()

        if 18 <= eta <= 25:
           categoria_eta = 'Junior'
        elif 26 <= eta <= 40:
           categoria_eta = 'Adult'
        else:
           categoria_eta = 'Senior'

        richiesta = {
                 'id': id,
                 'nome': nome,
                 'email': email,
                 'eta': eta,
                 'servizio': servizio,
                 'categoria_eta': categoria_eta,
        }
        richiesta_pulite.append(richiesta)

    servizi_unici = set()
    conteggio_servizi = {}
    for richiesta in richiesta_pulite:
        servizio = richiesta ['servizio']

        servizi_unici.add(servizio)

        if servizio in conteggio_servizi:
            conteggio_servizi[servizio] += 1
        else:
            conteggio_servizi[servizio] = 1

    print('richiesta_pulite:', richiesta_pulite)
    print('servizi unici:', servizi_unici)
    print('conteggio servizi:', conteggio_servizi)

class Richiesta:
    def __init__(self, id, nome, email, eta, servizio, categoria_eta):
        self.id = id
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio
        self.categoria_eta = categoria_eta

    def to_dict(self,):
        return {'id':self.id,
                'nome':self.nome,
                'email':self.email,
                'eta':self.eta,
                'servizio':self.servizio,
                'categoria_eta':self.categoria_eta
        }
class Validator:
    def validate(nome,email,eta):
        if nome == '':
            return False

        if '@' not in email:
            return False

        if eta < 18:
            return False

        return True

class Pipeline:
    def __init__(self, input_csv,output_json):
        self.input_csv = input_csv
        self.output_json = output_json

        self.richiesta_pulite = []
        self.servizi_unici = set()
        self.conteggio_servizi = {}

    def sanification(self, nome, email, servizio):
        nome = nome.strip().title()
        email = email.strip().lower()
        servizio = servizio.strip().title()
        return nome, email, servizio

    def categoria_eta(self,eta):
        if 18 <= eta <= 25:
           return 'Junior'
        elif 26 <= eta <= 40:
           return 'Adult'
        else:
           return 'Senior'

    def run(self):
        with open(self.input_csv, 'r', newline='') as f_in:
            reader = csv.DictReader(f_in)
            for row in reader:
                id = row['id']
                nome = row['nome']
                email = row['email']
                servizio = row['servizio']

                try:
                    eta = int(row['eta'])
                except ValueError:
                    continue

                if nome == '' or '@' not in email or eta < 18:
                    continue

                nome, email, servizio = self.sanification(nome, email, servizio)
                categgoria = self.categoria_eta(eta)

                richiesta = {
                    'id': id,
                    'nome': nome,
                    'email': email,
                    'eta': eta,
                    'servizio': servizio,
                    'categoria_eta': categgoria
                }

                self.richieste.append(richiesta)
                self.servizi_unici.add(servizio)

                if servizio in self.conteggio_servizi:
                    self.conteggio_servizi[servizio] += 1
                else:
                    self.conteggio_servizi[servizio] = 1

output ={
    'totale_richieste': len(richiesta_pulite),
    'servizi_unici': list(servizi_unici),
    'conteggi_servizi': conteggio_servizi,
    'richieste': richiesta_pulite
}

with open('output.json', 'w', newline='') as f_out:
    json.dump(output, f_out, indent = 4)









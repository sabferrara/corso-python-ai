import json

with open('utenti.json','r') as f_in:
    utenti = json.load(f_in)
#essendo una lista possiamo iterare
for u in utenti:

    eta = u['eta']

    if eta > 27:
        u['categoria'] = 'Senior'
    else:
        u['categoria'] = 'junior'

with open('utenti_classificati.json','w') as f_out:
    json.dump(utenti,f_out)

print(utenti)


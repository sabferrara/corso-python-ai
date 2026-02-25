nomi =['anna', 'luca', 'ciccio']

#trasforma questi nomi in maiuscolo
maiuscolo =[]
for nome in nomi:
    nome_maiusculo = nome.upper()
    maiuscolo.append(nome_maiusculo)
print(maiuscolo)

maiuscolo.append(nome.title())
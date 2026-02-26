import json

prompt= f"""
genera la descrizione di questo utente:
Si chiama anna e ha 22 anni
"""

with open('utente.json', 'r') as file:
    u = json.load(file)

def vincenzo_gpt(prompt, context):
    risposta = 'Ciao, ecco la tua descrizione'
    descrizione = f"L'utente si ciama {context["nome"]} e ha {context['eta']} anni"

    return risposta + descrizione
print(vincenzo_gpt(prompt,u))

"""
6 passaggi importanti:
- validazione
- preparazione del contesto (u=json.load(file)
- chiamata al modello 
- elaborazione della risposta
- output del risultato

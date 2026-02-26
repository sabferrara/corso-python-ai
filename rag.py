documenti =[
    'il sistema accetta pagamenti con carta',
    "Il sistema permette il login con spid ",
    "Il servizio è attivo 24 su 24"
]
#faccio embedding
def embedding_testuale(testo):   #trasformo domanda e documenti
    return len(testo)

def ricerca_similarita(domanda, documenti):

     valore_domanda = embedding_testuale(domanda)

     migliore = None
     distanza_minima = float('inf')

     for doc in documenti:
         distanza = abs(valore_domanda - embedding_testuale(doc))

         if distanza < distanza_minima:
             distanza_minima = distanza

#mi da la frase con il numero di caratteri piu simile alla domanda che gli sto facendo.

domanda ='Posso pagare con la carta, per favore?'

#mett un contesto vhr r la ricerca similarità

contesto = ricerca_similarita(domanda,documenti)
print(domanda)
print(contesto)
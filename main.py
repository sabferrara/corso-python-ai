lista = ['giallo', 'verde', 'blu']
for colore in lista:
    print(colore)

numeri =[10,20,30]
nuovi_numeri =[]
#operazione di trasformazione
for numero in numeri:
    nuovo = numero + 2  #qua trasformiamo la collection origiale (numeri)
    nuovi_numeri.append(nuovo)
print(nuovi_numeri)

for i in range (len(numeri)):
    numeri[i] = numeri [i] + 2 #cosi sto modificando la lista iniziale, non va bene
print(nuovi_numeri)

#operazione di filtro (es. voglio filtrare solo numeri pari)

numeri =[1,2,3,4,5,6,7,8,9,10] #creo nuova colezone
nuovi_numeri = []
pari =[]
for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)
print(pari)

#aggiungere numero sia vfiltrato che modificato
risultato = []

for numero in numeri:
    if numero % 2 == 0:
        risultato.append(numero * 10)
print(risultato)0


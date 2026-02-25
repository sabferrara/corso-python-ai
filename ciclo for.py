numeri =[1,2,3,4]
quadrati = []

#for numero in numeri:
 #   quadrati.append(numero ** 2)


#voglio mettere il numero elevato al quadrato dentro la mia lista nuova
quadrati = [numero **2 for numero in numeri]
#utilizziamo [trasformazione for elemento in elementi]
print(quadrati)

#è una list comprension. mettiamo il risultato che vogliamo ottenere e poi la dichiarazione del ciclo for

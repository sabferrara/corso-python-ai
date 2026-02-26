import csv

with open("dati.csv", newline= '') as csvfile:
    reader = csv.reader(csvfile)

    for riga in reader:
        print(riga)


with open("dati.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for riga in reader:
        print(riga)

dataset = []
with open("dati.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(csvfile)

    writer.writerow(["nome","eta", "citta"])
    writer.writerow(["Ciccio","19","Ancona"])

#posso utilizzare i dizionari per creare csv
#creo una variabile contenente i nomi delle colonne(i campi
    with open("dati.csv", "w") as csvfile:

        colonne = ["nome","eta", "citta"]

        writer = csv.DictWriter(csvfile, fieldsname = colonne)

        writer.writeheader()

        writer.writerom({
            "nome":"Mimmo",
            "eta": 22,
            "citta": "Roma"
        })

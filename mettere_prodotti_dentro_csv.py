prodotti = [
    {'id': 1, 'nome': 'PC', 'prezzo': 999.00},
    {'id': 2, 'nome': 'Monitor', 'prezzo': 699.00},
    {'id': 3, 'nome': 'Mouse', 'prezzo': 99.00},
    {'id': 4, 'nome': 'Tastiera', 'prezzo': 129.00},
]
import csv
with open ("dati.csv", "w") as csvfile:
    colonne = ["id", "nome", "prezzo"]

    writer = csv.DictWriter(csvfile, fieldnames = colonne)

    writer.writeheader()

    for p in prodotti:
        writer.writerow(p)
class Libro:
    def __init__(self, titolo, pagine):
        self.titolo = titolo
        self.pagine = pagine

    def lettura(self):
        print(f"Il libro di {self.titolo} ha un totale di {self.pagine} pagine")


libro1 = Libro('Anatomia',560)
libro2 = Libro('Geografia', 80)
libro3 = Libro('Matematica', 300)

libro1.lettura()
libro2.lettura()
libro3.lettura()

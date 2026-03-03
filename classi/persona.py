class Persona:
    # I metodi devono essere indentati all'interno della classe
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        # rimosso parentesi di troppo e aggiunto spazio prima di "anni"
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni"

# Ora puoi creare le istanze passando i parametri richiesti
p1 = Persona("Mario", 30)
p2 = Persona("Elena", 25)
p3 = Persona("Luca", 40)

print(p1.saluta())

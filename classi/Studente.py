#è una persona, riprendo la classe persona
from classi.persona import Persona

class Studente(Persona):
    
#aggiungo le propietà
    def __init__(self, nome, eta, corso): #nome ed eta mi derivano dalla classe persona(uso super)
        super().__init__(nome,eta)
        self.corso = corso

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni, e studio {self.corso}"

ciccio = Studente('Ciccio', 25, 'Python AI')   #tra parentesi mi chiede nome e eta perchè lo studente estende Persona
print(ciccio.saluta())

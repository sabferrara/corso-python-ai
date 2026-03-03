from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod   #decoratore
    def area(self):    #io non so come calcolare l'area, e dico che tutte le classi che ne estendono devono implementare il calcolo dell'area siccome non lo so fare io.
        pass

class Quadrato(Forma):

    def __init__(self,lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2

class Cerchio(Forma):    #cerchoo fa parte di forma, ha implemenatto il metodo area,

    def __init__(self,raggio):
        self.raggio = raggio

    def area(self):
        return self.raggio ** 2 * 3,14

    #ereditarietà: sia quadrato che cerchio ereditano area, che è un concetto astratto
    #entrambi sia quadrato e cerchio usano area in modo diversa


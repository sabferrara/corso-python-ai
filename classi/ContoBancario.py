class ContoBancario:

    def __init__(self, saldo):
        self.saldo = saldo

conto_di_ciccio =ContoBancario(10000)

conto_di_ciccio.saldo = conto_di_ciccio.saldo -10000

print(conto_di_ciccio.saldo)


#voglio creare un metodo che aumenti il mio saldo.
#Abbiamo reso saldo protetta per non potervi accedere direttamente
class ContoBancario:

    def __init__(self, saldo):
        self._saldo = saldo

    def deposita(self, importo):  #metodo che aumenta il saldo
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):    #metodo che diminuisce il saldo
        if 0 < importo < self._saldo:
            self._saldo -= importo

    def mostra_saldo(self):    #questo metodo lo fa vedere
        return self._saldo

conto_di_ciccio =ContoBancario(10000)

conto_di_ciccio.deposita(100)
conto_di_ciccio.preleva(1000)

print(conto_di_ciccio.mostra_saldo())

#utilizzare un singolo underscore è una convenzione, proviamo ad utilizzarli 2
class ContoBancario:

    def __init__(self, saldo):
        self.__saldo = saldo

    def deposita(self, importo):  #metodo che aumenta il saldo
        if importo > 0:
            self.__saldo += importo

    def preleva(self, importo):    #metodo che diminuisce il saldo
        if 0 < importo < self.__saldo:
            self.__saldo -= importo

    def mostra_saldo(self):    #questo metodo lo fa vedere
        return self.__saldo

conto_di_ciccio =ContoBancario(10000)

conto_di_ciccio.deposita(100)
conto_di_ciccio.preleva(1000)

print(conto_di_ciccio.mostra_saldo())


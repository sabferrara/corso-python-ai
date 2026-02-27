#LLM deve rispondermi

import abc import ABC, abstractmethod   #importo l'astratto

class LLMModel(ABC):

    @abstractmethod
    def genera(self,prompt):
        pass


    #ttte le classe che vann0 ad estendere questa classe devono generarmi qualcosa, ogni LLM deve avere genera
from abc import ABC, abstractmethod

class EmbeddingModel(ABC):

    @abstractmethod
    def genera_embedding(selfself,testo):   #testo che passero al LLM per avere delle risposte
        pass
#creiamo una classe che riceve un llm da una parte, embedding dall'altra. devo gestirli entrambi e li inserisco nel costruttore.

class PipelineAI:

    def __init__(self, llm_model, embedding_model):
        self._llm_model = llm_model
        self._embedding_model = embedding_model  #trova il metodo embedding con gli altri file

    #voglio nascondere all'esterno, le rendo protette aggiungendo underscore prima del nome delle variabili

    #costruiamo un metodo che fara partire la pipeline
    def esegui(self, testo):   #testo è un attributo che defineremo dall'esterno, che da valore ai contributi dall'esterno
        embedding = self._embedding_model.genera_embedding(testo)
        risposta = self._llm_model.genera(embedding)

        return {
            'embedding': embedding,
            'risposta': risposta
        }
#llm_model e embedding_model sono incapsulati, non li toccheremo mai dallesterno

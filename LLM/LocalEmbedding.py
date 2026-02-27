from LLM.EmbeddingModel import EmbeddingModel


class LocalEmbadding(EmbeddingModel):

    def genera_embedding(self,testo):
        return [0.9, 0.1, 0.8]

#genera embedding fanno cose diverse ma usano lo stesso (POLIFUNZIONISMO)
#In 5 file abbiamo fatto esempi di ereditarieta, astrazione,
# polimofrismo (local embedding e openai hanno lo stesso metodo ma fanno cose diverse)
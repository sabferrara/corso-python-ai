from LLM.LLMMODEL import LLMModel


class GPTModel(LLMModel):  #dobbiamo dire che deve estendere genera

    def genera(self, prompt):
        return f"Risposta locale per {prompt}"

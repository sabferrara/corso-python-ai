from LLM.GPTModel import GPTModel
from LLM.PipelineAI import PipelineAI

pipeline_1 = PipelineAI(GPTModel(), OpenAIEmbedding())
pipeline_2 = PipelineAI(GPTModel(), LocalEmbedding())

result_1 = pipeline_1.esegui("Cos'è il ML?")#esegui metodo che esiste dentro PipelineAi
result_2 = pipeline_1.esegui("Cos'è il ML?")

print(result_1)
print(result_2)

#polimorfismo: openAIEmbedding e LocalEmbedding sono usati in modo diverso
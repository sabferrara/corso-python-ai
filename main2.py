with open("pulizia.txt", "r") as f:
    nomi = f.readlines()

nomi_puliti =[]
print(nomi_puliti)

for n in nomi:
    nome = n.strip()
    nome= nome.title()
    nomi_puliti.append(nome)

print(nomi_puliti)

with open("pulizia.txt","w") as f:
    for nome in nomi_puliti:
        f.write(n +" \n")

#CON UNA COMPREHENSION
with open("pulizia.txt", "r") as f:
    nomi = f.readlines()

nomi_puliti =[r.strip().title(). replace("\n", "") for r in f.readlines()]

print(nomi_puliti)


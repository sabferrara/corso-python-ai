"""
Possiamo prevedere chi sopravvive? Si
"""

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt

pd.options.display.max_rows = 100
pd.options.display.max_columns = 8
df = pd.read_csv('Titanic-Dataset.csv')

df['IsMaleChild'] = 0
df.loc[df['Name'].str.contains('Master'), 'IsMaleChild'] = 1


"""
#prima di ripulire i dati, lo conosciamo
#print(df.head())
#print(df.info())
"""

#dall'output possiamo dire che abbiamo 177 righe Null, calcoliamo l'eta mancante con la media
#poi vediam che la cabina abbiamo 204 record, e avremo meno di 1/4 del nostro dataset, quindi lo eliminimo, sempre osservando l'outlet
#e tenendo a mente cje il nostro obiettivo è capire chi sopravvie.
#survived, pclass, sex e age, (forse fare) sono le piu importanti da tenere in considerazione

"""
print(df.describe())  #per vedere le statistiche generali

#vediamo i sopravvissuti
survived = df['Survived'].value_counts()
print(survived)
"""

"""
#cerchiamo la sopravvivenza per sesso
survived_by_sex = df.groupby('Sex')['Servived'].mean()
print(survived_by_sex)

survived_class = df.groupby('Pclass')['Survived'].mean()
print(survived_class)

avg_age_survived = df[df['Survived'] == 1]['Age'].mean()
print(avg_age_survived)
"""

"""
#esploriamo per l'eta'
survived_by_age = df.groupby('Age')['Survived'].mean()
print(survived_by_age)
"""

"""
#prezzo medio per classe
print(df.groupby('Pclass')['Fare'].mean())
#prezzo max per classe
print(df.groupby('Pclass')['Fare'].max())
"""

#abbiamo visto che se eri un uomo sulla 30ina in terza classe succedeva un patratrac
#quelli piu importanti sono classe e sesso

#PULIZIA
#un modell ML vuole solo numeri

"""
facciamo info per avere la panoramica sulle colonne,
tutte le stringhe le andrei a eliminare
print(df.info())
"""
#con queste tre successive, ci stiamo iniziando a creare la pipeline
df = df.drop(['PassengerId','Name','Cabin', 'Ticket'], axis = 1)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0]) #se porto di imbarco è nullo, mettere quello piu frequente
#creo una nuova features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 #1 sono io
df['isAlone'] = 0
df.loc[df['FamilySize']==1, 'isAlone'] =1 #vuol dire che se la prima cose è vera, la seconda diventa 1
df = df.drop(['SibSp', 'Parch'], axis = 1)

df['Age0015'] = 0  #creiamo feature da 0 a 15 anni
df['Age1540'] = 0  #FEATURE da 15 a 40 anni
df['Age4080'] = 0
df.loc[(df['Age'] > 0) & (df['Age'] <= 15), 'Age0015'] =1
df.loc[(df['Age'] > 15) & (df['Age'] <= 40), 'Age1540'] =1
df.loc[df['Age'] > 40, 'Age4080'] =1
df = df.drop(['Age'], axis = 1)

df = pd.get_dummies(df,columns=['Sex','Embarked'], drop_first=True)
print(df)
#i modelli di ML si basano sulla moda, tendenza, per questo tocca normalizzare

X = df.drop('Survived', axis = 1) # Xmi stampa solo le features
Y = df['Survived'] #Y stampa i dati in base alla sopravvivenza

#separazione nei 4 set, dividiamo in train per imparare e test per provare che mi resttuisce una tupla di 4 valori
X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size = 0.2,
    random_state = 42   #con 42 rendiamo lo shuffle riproducibile, altrimenti ogni volts avremmo un train diverso
)

print(X_train)   #matrice di addestramento delle feature
print(y_train)
#il modello non andrà a vedere i test,

#titanic ha un target: survived(1 o 0) ed è un problema di classificazione binaria

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

model.fit(X_train, y_train)
#la logisticregression prende le features e le combina con dei pesi, creando una probabilità tra o e 1
#se la probabilità supera 0,5 lo considera come classe 1 altrimenti zero
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print('Accuracy===>', accuracy)
print("\n")

#confused matrix (TN,TP,FN,FP)
cm = confusion_matrix(y_test,y_pred)
print("==== Confusion Matrix === >\n ", cm)

cr = classification_report(y_test,y_pred)
print( "====Classification Report ====>\n", cr)
print("\n======== \n")

y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train,y_train_pred)
test_accuracy = accuracy_score(y_test,y_pred)
print('Train Accuracy===>', train_accuracy)
print('Test Accuracy===>', test_accuracy)

#per vedere i pesi
for feature,coef in zip(X.columns,model.coef_[0]):
    print(feature,coef)
    #age negativo: piu aumenta eta piu aumenta la possibilità di morire
    #piu aumenta SibSp piu schiatti

#aggiungiamo passeggeri
jack = {
    'Pclass':3,
    'isMaleChild':0,
    'FamilySize': 1, #era da solo
    'isAlone': 1,
    'Sex_male':1,
    'Age0015':0,
    'Age1540':1,
    'Age4080':0,
    'Embarked_Q':0,
    'Embarked_S':1,
}

rose = {
    'Pclass':1,
    'isMaleChild':0,
    'FamilySize': 2, #non da sola
    'isAlone': 0,
    'Sex_male':0,
    'Age0015':0,
    'Age1540':1,
    'Age4080':0,
    'Embarked_Q':0,
    'Embarked_S':1
}

vince = {
    'Pclass':2,
    'isMaleChild':0,
    'FamilySize': 4,
    'isAlone': 0,
    'Sex_male':1,
    'Age0015':0,
    'Age1540':1,
    'Age4080':0,
    'Embarked_Q':0,
    'Embarked_S':0
}

char_titanic_movie = pd.DataFrame([jack,rose, vince], index = ['Jack','Rose', 'Vince'])
char_titanic_movie = char_titanic_movie.reindex(columns = X.columns, fill_value=0)

pred_class = model.predict(char_titanic_movie)
pred_proba = model.predict_proba(char_titanic_movie)[:,1]

results = pd.DataFrame(
    {
        "Predict Sorvived": pred_class,
        "Predict Probability": pred_proba,
    }, index = char_titanic_movie.index
)

print(results)

survived_by_sex = df.groupby('Sex_male')['Survived'].mean()

plt.figure()
plt.bar(['Femmine','Maschi'],survived_by_sex) #grafico a barre
plt.title('Sopravvivenza per sesso')
plt.ylabel('Percentuale Sopravvivenza')
plt.show()
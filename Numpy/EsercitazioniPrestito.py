#carichiamo i dati grezzi
#puliamo i campi
#rimuovere quelli irrecuperabili

from __future__ import annotations
import re
from dataclasses import dataclass #ci consente di creare classi come fossero entità, per gestre oggetti
from typing import Any, Dict,List, Optional, Tuple #sono dei tipi che utilizziamo per tipizzare gli oggetti

import numpy as np

#importiamo il nostro dataset
RAW_RECORDS: List[Dict[str,Any]] = [                   #è una costante, ci sono i due punti perchè specifichiamo che deve essere una lista di dizionario, con le chiavi le stringhe e valore qualsiasi

        {"age": " 25", "income": "€30.000", "debts": "2",   "credit_score": "650", "approved": "yes"},
        {"age": "45",  "income": "80000",   "debts": "1",   "credit_score": "720", "approved": "1"},
        {"age": "N/A", "income": "€50.000", "debts": "5",   "credit_score": "580", "approved": "no"},
        {"age": "23",  "income": " 25k ",   "debts": "3",   "credit_score": "600", "approved": "0"},
        {"age": "52",  "income": "120000",  "debts": "0",   "credit_score": "800", "approved": "yes"},
        {"age": "40",  "income": "70k",     "debts": "4",   "credit_score": "610", "approved": "no"},
        {"age": "??",  "income": "40000",   "debts": "",    "credit_score": None,  "approved": "yes"},
        {"age": "31",  "income": "€-1000",  "debts": "2",   "credit_score": "690", "approved": "no"},
        {"age": "34 ", "income": "45000",   "debts": "two", "credit_score": "710", "approved": "yes"},
        {"age": "29",  "income": " 60000 ", "debts": "1",   "credit_score": "680", "approved": "YES"},
]

#creiamo un modello di dati, quindi inseriamo un @
@dataclass      #crea un modello dati, dice che questi dati grezzi devono seguire le istruzione successive. Ti evita di mettere i costruttori
class CleanRecord:
    age: int    #gli diciamo come il record pulito e tipizzato deve essere formato. Abbiamo l'eta che vogliamo sia un intero.
    income: float  #income deve essere un float
    debts: int #devono essere interi
    credit_score: int
    approved: int

#classe per parsing/sanificazione
class FieldParser:   #convertire i campi grezzi in numeri, gestendo i formati strani. Non sarà il panser a decidere se è valio o meno, si limita solo a convertire e se non riesce ci restituisce None

    def parse_int(self, value:Any) -> Optiona[int]:#controlliamo se il valore è intero, se non lo è si converte. Con ->Optional[int] indica il tipo che deve restituire è un intero, altrimento restituisce None
        if value is None:
            return None

        if isinstance(value,str): #se e una string, dobbiamo pulirla
            txt = value.strip() #tolgo gli spazi superflui
            if txt == "" or txt.lower() in {'n/a', 'na', '??'}: #se il testo è vuoto, o una volta converito in minuscolo è uguale a quello tra {}, allora mi restituisci None
                return None

            txt = re.sub(r"[^\d\-]", "", txt) #tramite la regex sto dicendo di tenersi solo le cifre ed eventualmente il segno meno, se non è cosi tutti gli altri segni me li togli (converti in stringa vuota) #puliamo eventuali simboli che devono essere puliti
            if txt == "" or txt == "-": #se il testo rimane vuoto o con il trattino, è nond e vado a fare la conversione
                return None

            try:
                return int(txt)
            except ValueError:
                return None

        if isinstance(value,(int, np.integer)):
            return int(value)
        return None  #se è qualsiasi altro tipo di valore(lista,booleano)

    #abbiamo prima esvluso che sia un none, poi escluso che sia vuoto o con caratteri strani,
    #poi abbiamo assunto che fosse un intero o intero numpy, negli altri casi non mi interessa.
    """
    se io ho '€30.000' --> 30000.00
    25k --> 25000.00
    """
    def parse_income(self,value: Any) -> Optiona[float]:
        if value is None:
            return None

        if isinstance(value,(int, float, np.integer, np.floating)):
            income = float(value)
            return income

        if not isinstance(value, str):
            return None

        txt = value.strip().lower()
        if txt in {'n/a', 'na', ''}:
            return None

        txt = value.strip().lower()
        #sanifichiamolo
        k_match = re.fullmatch(r"([-+]?\d+)\s*k", txt) #se questa cosa mi restituisce true (prendi tutta la stirnga tranne k)
        if k_match:
            return float(k_match.group(1)) * 1000.0

        txt = txt.replace('€', ""). replace ("", " ").replace(".", "")

        try:
            return float(txt)
        except ValueError:
            return None

    def parse_approved(self,value:Any) -> Optional[int]:
        if value is None:
            return None

        if isinstance(value,(int, np.integer)):
            if int(value) in (0,1):
                return int(value)
            return None

        txt = value.strip().lower()

        if txt in {'1', 'yes', 'y', 'si', 't', 'true'}: #prendiamo tutte le possibile variabili per considerare sia vero
            return 1

        if txt in {'0', 'no', 'n', 'f', 'false'}:
            return 0

        return None

#validatore
class RecordValidator:

    #creiamo dei metodi. Dobbiamo dire alla classe di decidere se il metodo è accettabile per il training
    def is_valid(self, rec:CleanRecord) -> bool: #qualsiasi elemento, funzione etc che inizia con is è un booleano

        if rec.age < 18 or rec.age > 99:
            return False

        if rec.income <= 0:
            return False

        if rec.debts < 0 or rec.debts > 50:
            return False

        if rec.credit_score < 300 or rec.credit_score > 850:
            return False

        if rec.approved not in (0,1):
            return False

        return True

#dobbiamo ritrasformarlo in una matrice
class PreprocessingPipeline:

    def __init__(self,parser:FieldParser, validator:RecordValidator):
        self.parser = parser
        self.validator = validator
        self.dropped_records: int = 0
        self.kept_records: int = 0 #vado sempre a tipizzare

    def clean_records(self, raw_records: List[Dict[str,Any]]) -> List[CleanRecord]:
        #creiamo lista nuova con record puliti e validi, senza toccare la lista originale grezza
        cleaned: List[CleanRecord] = []

        for raw in raw_records:
            age = self.parser.parse_int(raw.get('age'))  #fieldparser
            income = self.parser.parse_income(raw.get('income'))
            debts = self.parser.parse_int(raw.get('debts'))
            credit_score = self.parser.parse_int(raw.get('credit_score'))
            approved = self.parser.parse_approved(raw.get('approved'))

            if None in (age, income, debts, credit_score, approved):   #se uno di questi tra parentesi è none..
                self.dropped_records += 1
                continue
            rec = CleanRecord(    #se nessuno di qeusti e none
                age= int(age),
                income= float(income),
                debts= int(debts),
                credit_score= int(credit_score),
                approved= int(approved)
            )

            #una volta che i dati esistono e sono puliti, li filtriamo e dobbiamo passare il test di qualità

            if not self.validator.is_valid(rec):
                self.dropped_records += 1
                continue

            cleaned.append(rec)
            self.kept_records += 1
            #una volta completato ci restituiamo la lista dei valori puliti
        return cleaned

    #convertiamo i record puliti in una matrice x(sono le features) e un vettore y(sarà il nostro target). E in base al
    #target ottenere il nostro modello

    def build_xy (self, cleaned:List[CleanRecord]) -> Tuple[np.ndarray,np.ndarray]:
        #convertiamo i record puliti in matrice x e vettore y
        X = np.array(
            [[r.age, r.income, r.debts, r.credit_score] for r in cleaned],
                dtype = float   #serve per ottenere qualcosa di coerente
        )

        Y = np.array(
            [r.approved for r in cleaned],
            dtype = int
        )

        return X, Y

    #aiutiamo il modello a capire quello che bisogna fare

    def add_feature_engineering(self, X: np.ndarray) -> np.ndarray:
        income = X[:,1]
        debts = X[:,2]

        debt_to_income = debts/ income #nuova colonna, che dobbiamo invertire per attaccarla alla matrice perchè cosi esce una riga

        debt_to_income = debt_to_income.reshape(-1,1) #inverte la forma della matrice

        X_enhanced = np.hstack((X,debt_to_income))

        return X_enhanced

    def minmax_normalize(selfself, X:np.ndarray) -> np.ndarray:   #normalizzazione
        min_col = np.min(X, axis=0)  #min e max per ogni colonne
        max_col = np.max(X, axis=0)

        #calcoliamo il denominatore perchè se una colonna è costante(il max uguale al minimo, il denominatore = 0.
        denom = (max_col - min_col)

        denom[denom == 0] = 1.0
        #applichiamo la normalizzazione
        X_norm = (X-min_col)/denom
        return X_norm

    def train_test_split(
            self,
            X:np.ndarray,
            Y:np.ndarray,
            train_ratio: float = 0.8,   #indica quanto deve essere train e quanto test
            seed : int =42
    )-> Tuple[np.ndarray,np.ndarray, np.ndarray,np.ndarray]:
        idx =np.arange(len(X))  #creiamo un array di indici

        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

        train_size = int(len(idx) * train_ratio)

        train_idx = idx[:train_size]
        test_idx = idx[train_size:]

        X_train = X[train_idx]
        X_test = X[test_idx]

        Y_train = Y[train_idx]
        Y_test = Y[test_idx]

        return X_train, Y_train, X_test, Y_test


def somma(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("somma, ,b,must be int")
    return a + b

def differenza(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("differenza, ,b,must be int")
    return a-b

def moltiplicazione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("moltiplicazione, ,b,must be int")
    return a * b

def divisione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("divisione, ,b,must be int")
    if b == 0:
        raise ZeroDivisionError('String must be greater than 0')
    return a / b


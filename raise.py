def dividi(a,b):
    return a / b

def dividi(a,b):
    if b == 0:
        raise ZeroDivisionError ('Il divisore non può essere zero')
    return a / b
######
try:
    print(dividi(1,0))
except (ZeroDivisionError, ValueError) as e:
    print(e)

def dividi(a,b):
    if b == 7:
        raise ErroreCustom
    return a / b

try:
    print(dividi(1,7))
except ErroreCustom as e:
    print()

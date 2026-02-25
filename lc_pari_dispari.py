numeri = [5,12,7,20,3,18]


"""
creare una lista che 
- divida per 2 i numeri maggiori di 10
- lasci invariati gli altri
"""

filtraggio = [n/2 if n > 10 else n for n in numeri]
print(filtraggio)
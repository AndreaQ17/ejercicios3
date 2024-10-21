
# EJERCICIO 3: Python string formatting (formato de cadenas en python)
def print_formatted(n):
    width = len(bin(n)) - 2
    for i in range(1, n + 1):
        print(f"{i:{width}d} {oct(i)[2:]:{width}} {hex(i)[2:].upper():{width}} {bin(i)[2:]:{width}}")
n = 17
print_formatted(n)


#EJERCICIO 1: ALFABETO RANGOLI
def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 97 + size)]
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4 * size - 3, '-'))
    print('\n'.join(lines[::-1] + lines[1:]))
n = 18
print_rangoli(n) 


#EJERCICIO 2: CONTADOR DE COLECCIONES 
from collections import Counter
myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
contador = Counter(myList)
print(contador) 
print(contador.items())  
print(contador.keys())  
print(contador.values()) 






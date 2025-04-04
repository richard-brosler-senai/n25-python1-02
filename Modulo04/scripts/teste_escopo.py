"""
Código para demonstrar escopo de variáveis no python
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear
# Definindo uma função
def calculo():
    a = 5
    b = a + c
    # c = 30 # Se descomentado dá erro porque a variável c passa a ser local
    return b
# Programa principal
clear()
c = 10
print(calculo())
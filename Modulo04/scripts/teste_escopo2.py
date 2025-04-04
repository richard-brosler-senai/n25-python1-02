"""
Programa de teste de escopo de variáveis - 2
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear
def calculo():
    global c, d
    a = 5
    b = a + c
    c = 30
    d = 50
    return b
# programa principal
c = 10
print(calculo())
print("Valor de c=",c,"Valor de D=",d)
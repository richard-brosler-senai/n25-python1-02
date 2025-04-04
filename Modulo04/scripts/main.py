"""
Programa principal
Author: Richard Brosler
Version: 2025-04-03
"""
import funcoes
from click import clear # importando somente a função clear
clear() # Limpa o console
funcoes.cabecalho("Bem vindo!",colunas=50)
funcoes.cabecalho("Olá turma, boa noite!",30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("Fatorial de 5=",funcoes.fatorial(1000))
print("Fatorial de 5=",funcoes.fatorial_rec(5))
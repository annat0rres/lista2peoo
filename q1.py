# 1. Escreva um programa que verifica se um número fornecido pelo usuário é par ou ímpar.

n = int(input('digite um n° inteiro: '))

if n % 2 == 0:
    print(n, 'é par!')
else:
    print(n, 'é impar')
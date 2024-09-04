# 5. Crie um programa que gera os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário.

n = int(input('digite um n°: '))
if n <= 0:
    print('digite um n° inteiro positivo: ')
else:
    a, b = 0, 1
    print(a, end = ' ')
    print(b, end = ' ')
    for i in range(n - 2):
        proximo = a + b
        print(proximo, end = ' ')
        a = b
        b = proximo

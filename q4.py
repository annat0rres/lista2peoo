# 4. Escreva um programa que calcula o fatorial de um número fornecido pelo usuário.
# n! = n × (n-1) ×  ... ×  2 ×  1

n = int(input('digite o número que deseja ver o fatorial: '))
fatorial = 1

while n > 0: 
    fatorial *= n
    n -= 1

print('o fatorial é:', fatorial)
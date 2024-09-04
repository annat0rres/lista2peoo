#2. Crie um programa que converte a temperatura de Celsius para Fahrenheit e vice-versa, com base na escolha do usuário.
# F= 59​ × C+32

temp = float(input('digite a temperatura: '))

perg = str(input('digite c se deseja transformar F para C ou digite f se deseja transformar C para F: '))

if perg == 'c':
    ce = (temp - 32) /  (5/9)
    print(f'a temperatura em Celsius é: {ce}')
if perg == 'f':
    fh = (5/9) * temp + 32
    print(f'a temperatura em Fahrenheit é: {fh}')
else:
    print('digite c OU f!')

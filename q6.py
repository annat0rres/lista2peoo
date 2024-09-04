#6. Crie um programa que recebe os coeficientes (a,b,c) de uma equação quadrática  ax2 + bx +c =0 e calcula suas raízes reais, se existirem.

a = float(input('digite o A da raiz quadrada: '))
b = float(input('digite o B da raiz quadrada: '))
c = float(input('digite o C da raiz quadrada: '))
delta = b**2 - 4 * a * c
print('este é seu delta: ', delta) 
if delta >= 0:
    raizd = delta **(1/2)
    x = ((b*-1) + raizd) / (2*a)
    x2 = ((b*-1) - raizd) / (2*a)
    print('esse é seu x1:', x)
    print('esse é seu x2:', x2)
else:
    print('o delta é negativo! não existe raizes reais')
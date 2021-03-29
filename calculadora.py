n0 = str(input('Qual é o seu nome ? '))
print('Olá',n0,'!')
n1 = int(input('Digite um valor: '))
n2 = int(input('Agora digite outro valor: '))
S = n1 + n2
SB = n1 - n2
M = n1 * n2
D = n1 / n2
D2 = n1 // n2
P = n1 ** n2
M2 = (n1 + n2)/2
R1 = float(n1) ** 0.5
R2 = float(n2) ** 0.5
if (n1%2) == 0:
  N1='par'
else:
  N1='impar'
if (n2%2) == 0:
  N2='par'
else:
  N2='impar'
print(f'A soma é {S},a subtração é {SB}')
print(f'A multiplicação é {M},e a divisão é {D}')
print(f'O resto da divisão é {D2},e a potência é {P} ')
print(f'A média entre os dois números é {M2} ')
print(f'A raiz de {n1} é {R1} e a raiz de {n2} é {R2}')
print(f'O número {n1} é {N1} e o o número {n2} é {N2}')
print('Até mais',n0,'punheteiro XD ')

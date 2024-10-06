from operadores import soma,sub, divisao, multi

x = 1
y = 1

print(f'A soma é: {soma(x,y)}')
print(f'A subtração é: {sub(x,y)}')
print(f'A divisão é: {divisao(x,y)}')
print(f'A multiplicação é: {multi(x,y)}')

from operadores.avançados import quadrado,cubo
print(f'O resultado ao quadrado é: {quadrado(x,y)}')
print(f'O resultado ao cubo é: {cubo(x,y)}')


'''
from meu_pacote.subpacote import modulo3


print(modulo3.funcao3())
'''
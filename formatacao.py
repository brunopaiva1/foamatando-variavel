#formatação de variáveis em python
a = 100
b = 175
c = 204

soma = a + b + c
subtracao = a - b - c
divisao = c / b
multiplicacao = a * b * c
resto = a % b & b % c

#o "format" serve para que seja possivel a concatenação de uma string com qualquer outro tipo
print('Soma: {}'.format(soma))
print('Subtração: {}'.format(subtracao))
print('Divisão: {}'.format(divisao))
print('Multiplicação: {}'.format(multiplicacao))
print('Resto: {}'.format(resto))

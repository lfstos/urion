'''
Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e
informe-o expresso no formato horas:minutos:segundos.
Entrada

O arquivo de entrada contém um valor inteiro N.
Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos,
conforme exemplo fornecido.

Exemplo Entrada     Exemplo Saída
556                 0:9:16
1                   0:0:1
140153              38:55:53
'''

n = int(input())
h = n // 60**2
n = n - h * 60**2

m = n // 60
n = n - m * 60

s = n

print('{}:{}:{}'.format(h, m, s))
# print(f'{h}:{m}:{s}')
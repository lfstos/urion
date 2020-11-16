'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode
ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a
relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada      Exemplo de Saída
576                     576
                        5 nota(s) de R$ 100,00
                        1 nota(s) de R$ 50,00
                        1 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        1 nota(s) de R$ 5,00
                        0 nota(s) de R$ 2,00
                        1 nota(s) de R$ 1,00

11257                   11257
                        112 nota(s) de R$ 100,00
                        1 nota(s) de R$ 50,00
                        0 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        1 nota(s) de R$ 5,00
                        1 nota(s) de R$ 2,00
                        0 nota(s) de R$ 1,00

503                     503
                        5 nota(s) de R$ 100,00
                        0 nota(s) de R$ 50,00
                        0 nota(s) de R$ 20,00
                        0 nota(s) de R$ 10,00
                        0 nota(s) de R$ 5,00
                        1 nota(s) de R$ 2,00
                        1 nota(s) de R$ 1,00
'''


n = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(n)
for nota in notas:
    quantidade_notas = int(round(n, 2) / nota)
    n -= quantidade_notas * nota
    print('{} nota(s) de R$ {:.2f}'.format(quantidade_notas, nota))


'''n = int(input())
n1 = n
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
if n >= 100:
    while n >= 100:
        cem += 1
        n -= 100
if n >= 50:
    while n >= 50:
        cinquenta += 1
        n -= 50
if n >= 20:
    while n >= 20:
        vinte += 1
        n -= 20
if n >= 10:
    while n >= 10:
        dez += 1
        n -= 10
if n >= 5:
    while n >= 5:
        cinco += 1
        n -= 5
if n >= 2:
    while n >= 2:
        dois += 1
        n -= 2
if n >= 1:
    while n >= 1:
        um += 1
        n -= 1
print(n1)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
'''
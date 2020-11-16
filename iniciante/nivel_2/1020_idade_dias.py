'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada      Exemplo de Saída
400                     1 ano(s)
                        1 mes(es)
                        5 dia(s)

800                     2 ano(s)
                        2 mes(es)
                        10 dia(s)

30                      0 ano(s)
                        1 mes(es)
                        0 dia(s)
'''

n = int(input())
ano = n // 365
n = n - ano * 365
mes = n // 30
n = n - mes * 30

print(f'{ano} ano(s)')
print(f'{mes} mes(s)')
print(f'{n} dia(s)')




'''
n = int(input())

ano, mes, dia = 0, 0, 0

if n >= 365:
    while n >= 365:
        n -= 365
        ano += 1
if n >= 30:
    while n >= 30:
        n -= 30
        mes += 1
dia = n
print(f'{ano} ano(s)')
print(f'{mes} mes(s)')
print(f'{dia} dia(s)')
'''
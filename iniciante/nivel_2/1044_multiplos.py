'''
1044

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

Exemplo Entrada     Exemplo Saída
6 24                Sao Multiplos
6 25                Nao sao multiplos
'''

a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
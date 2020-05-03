"""
Execício 1013


Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem
“eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é
necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

"""

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorABS = int ((a+b+abs(a - b)) / 2)

if maiorABS > c:
    print("{} eh o maior".format(maiorABS))
else:
    print("{} eh o maior".format(c))
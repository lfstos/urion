'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada      Exemplo de Saída
7 21 -14                -14
                        7
                        21

                        7
                        21
                        -14

-14 21 7                -14
                        7
                        21

                        -14
                        21
                        7
'''

a, b, c = [int(x) for x in input().split()]
menor = a, b, c
for x in sorted(menor):
    print(x)
print()
for x in menor:
    print(x)
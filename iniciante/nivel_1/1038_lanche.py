'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

CODIGO      ESPECIFICAÇÃO       PREÇO
1           Cachorro Quente     R$ 4.00
2           X-Salada            R$ 4.50
3           X-Bacon             R$ 5.00
4           Torrada Simples     R$ 2.00
5           Refrigerante        R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um
item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago,
com 2 casas após o ponto decimal.

Exemplo de Entrada      Exemplo de Saída
3 2                     Total: R$ 10.00
4 3                     Total: R$ 6.00
2 3                     Total: R$ 13.50
'''

codigo, quantidade = [int(x) for x in input().split()]

cod_preco = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

for key, value in cod_preco.items():
   if codigo == key:
       print('Total: R$ {:.2f}'.format(quantidade * value))

"""
Exercício 1010

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o
valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois
inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após
os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

"""

cod_peca_1, num_pecas_1, valor_unit_1 = input().split(' ')

cod_peca_1 = int(cod_peca_1)
num_pecas_1 = int(num_pecas_1)
valor_unit_1 = float(valor_unit_1)

cod_peca_2, num_pecas_2, valor_unit_2 = input().split(' ')
cod_peca_2 = int(cod_peca_2)
num_pecas_2 = int(num_pecas_2)
valor_unit_2 = float(valor_unit_2)
resultado = (num_pecas_1 * valor_unit_1) + (num_pecas_2 * valor_unit_2)

print('VALOR A PAGAR: R$ {:.2f}'.format(resultado))

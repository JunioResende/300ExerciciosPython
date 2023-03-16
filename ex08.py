"""Peca para que o usuario digite um numero, em seguida converta esse numero para float
exibindo em tela tanto o numero em si quanto seu tipo de dado
"""

num = int(input("Digite um numero inteiro: "))
num = float(num)

print(f"O numero digitado e {num} e seu tipo e {type(num)}")

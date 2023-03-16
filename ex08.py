"""Peca para que o usuario digite um numero, em seguida converta esse numero para float
exibindo em tela tanto o numero em si quanto seu tipo de dado
"""

# Variavel que ira captar um numero inteiro
num = int(input("Digite um numero inteiro: "))
num_conv = float(num)  # Variavel que ira fazer a conversao

# Mostra em tela o numero digitado pelo usuario e seu tipo de dado
print(
    f"O numero digitado e {num} e Seu tipo de dado e {type(num)},\n apos a conversao para float temos {num_conv:.2f} e seu tipo e {type(num_conv)}")

"""
    Escreva um programa que pede que o o usuario de entrada de dois valores,
    em seguida exiba o resultado em tela da soma, subtracao, multiplicacao,
    e divisao desses numeros.
"""
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
restoDivisao = num1 % num2
potenciacao = num1 ** num2

print(f"+A soma dos dois valores e: {soma}\n-A subtracao dos dois valores e: {subtracao}\n*A multiplicacao dos dois valores e: {multiplicacao}\n/A divisao resulta em: {divisao: .2f}\n%O resto da divisao resulta em: {restoDivisao: .2f}\n**A potenciacao resulta em: {potenciacao}")

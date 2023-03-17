contador = 0
soma = 0

for i in range(1, 101):
    if i % 3 == 0:
        soma += i
        contador += 1
print(
    f"Foram encontrados {contador} numeros impares!\nA soma desses valores e = {soma}")

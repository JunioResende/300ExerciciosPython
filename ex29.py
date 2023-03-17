inicio = int(input("Digite o numero que da inicio a contagem: "))
fim = int(input("Digite o numero que da fim a contagem: "))

# Sempre que temos variaveis que declaram inicio e fim podemos usar o metodo range.
for i in range(inicio, fim + 1):
    print(i)

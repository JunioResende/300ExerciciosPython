termo = int(input("Digite o primero termo: "))
razao = int(input("Digite a razao: "))
pa = termo + (20 - 1) * razao

for i in range(termo, pa + razao, razao):
    print(i)

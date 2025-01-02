linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
simbolo = input("Insira o símbolo: ")

for x in range(linhas):
    for y in range(colunas):
        print(simbolo, end="")
    print()
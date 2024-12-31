"""
nome = input("Digite seu nome: ")

while nome == "":
    print("Este campo deve ser preenchido.")
    nome = input("Digite seu nome: ")

print(f"Olá, {nome}.")
"""

"""
num = int(input("Insira um número de 1 a 10: "))

while num < 1 or num > 10:
    print(f"{num} não é um número válido.")
    num = int(input("Insira um número de 1 a 10: "))

print(f"Você escolheu o número {num}.")
"""

comida = input("Insira uma comida que você gosta (Pressione s para sair): ")

while not comida == 's':
    print(f"Você gosta de {comida}!")
    comida = input("Insira uma comida que você gosta: (Pressione s para sair): ")
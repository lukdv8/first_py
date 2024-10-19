"""
nome = input("Digite seu nome completo: ")

# retorna o comprimento da string
print(len(nome))

# retorna a primeira ocorrência de um determinado caractere
print(nome.find("L"))

# transforma o primeiro caractere de uma string em maiúscula
print(nome.capitalize())

# transforma todos os caracteres de uma string em maiúscula
print(nome.upper())

# transforma todos os caracteres de uma string em minúsculo
print(nome.lower())

# substitui qualquer ocorrência de um determinado caractere por outro
print(nome.replace(" ", ""))

# método booleano, só retornará verdadeiro se a string conter APENAS caracteres alfabéticos
print(nome.isalpha())

# método booleano, só retornará verdadeiro se a string conter APENAS dígitos numéricos
print(nome.isdigit())

# retorna a última ocorrência de um determinado caractere (não difere de minúscula e maiúscula)
print(nome.rfind("a"))

# retorna quantos caracteres iguais estão dentro de uma string
print(nome.count("a"))

# retorna uma lista de todos os métodos string disponíveis
print(help(str))
"""

# exercicio de validacao da entrada do usuario
# nao pode conter mais que 12 caracteres
# nao pode conter espaços
# nao pode conter digitos numericos

print("Seu nome não deve conter espaços, digitos numéricos e mais que 12 caracteres")
nome = input("Digite seu nome: ")

if len(nome) > 12:
    print("Seu nome não pode ultrapassar 12 caracteres.")

elif not nome.find(" ") == -1:
    print("Seu nome não pode conter espaços.")

elif not nome.isalpha():
    print("Seu nome não pode conter digitos numéricos.")

else:
    print(f"Olá, {nome}!")
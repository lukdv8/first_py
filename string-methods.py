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
"""
# este é o meu primeiro programa em python!

#imprimir
print("Eu gosto de cogumelos!")
print("São muito bons!")

#criando variáveis String
first_name = "Lucas"
food = "cogumelos"
email = "abcd@fake.com"

# concatenando strings
print(f"Olá {first_name}!")
print(f"Você gosta de {food}")
print(f"Seu e-mail é {email}")

# integer
idade = 27
print(f"Você tem {idade} anos")

# float
valor = 59.90
print(f"O freio custa {valor}")

# Boolean
e_um_estudante = True
print(f"Você é um estudante?: {e_um_estudante}")

# conversão de tipo implícita
nome = "Alfreu"
visitas_mcdonalds = 5
peso = 107.9
e_sedentario = True

# string pra boolean
nome = bool(nome)
print(nome)

# int pra float
visitas_mcdonalds = float(visitas_mcdonalds)
print(visitas_mcdonalds)

#float pra int
peso = int(peso)
print (peso)

# boolean pra string
e_sedentario = str(e_sedentario)
print (e_sedentario)

# conversão de tipo explícita
#int pra float
x = 5
y = 3.5
x = x / y
print(x)

#entrada do usuário
hobby = input("Qual seu hobby?: ")
# entrada do usuario conventendo o tipo
saldo = float(input("Digite seu saldo: "))
saldo = saldo + 300
print(f"Seu hobby é {hobby}")
print(f"Seu saldo é {saldo}")

# calculando a área do triangulo
comprimento = float(input("Digite o comprimento da base: "))
altura = float(input("Digite a altura do triângulo: "))

area = comprimento * altura / 2

print(f"A base do seu triângulo tem {comprimento} cm de comprimento")
print(f"E {altura} cm de altura")
print(f"Resultando em uma área de {round(area, 5)} cm^2")

# carrinho de compras
item = input("Digite qual item quer comprar: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o valor:"))

total = preco * quantidade

print(f"Você comprou {quantidade} {item}/s")
print(f"Totalizando {total} reais")
"""

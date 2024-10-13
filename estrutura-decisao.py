"""
#estrutura de decisão composta
idade = int(input("Digite a sua idade: "))

if idade>=18 :
    print("Você é maior de idade.")
else :
    print("Você é menor de idade.")
"""

#elif
idade = int(input("Digite a sua idade: "))

if idade>=18 :
    print("Você é maior de idade.")
elif idade >=16:
    print("Você é um infanto-juvenil.")
else :
    print("Você é menor de idade.")
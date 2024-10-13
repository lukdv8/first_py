nota1 = float(input("Digite a nota da Avaliação 1: "))
nota2 = float(input("Digite a nota da Avaliação 2: "))
nota3 = float(input("Digite a nota da Avaliação 3: "))

media = (nota1 + nota2 + nota3) / 3

print("\nNota da Avaliação 1: ", nota1)
print("Nota da Avaliação 2: ", nota2)
print("Nota da Avaliação 3: ", nota3)
print("\nMédia das notas: ", media)

#resultado
if media>7.0 :
    print("Você está aprovado.")
else :
    print("Você está reprovado.")
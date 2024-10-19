#and = confere se duas ou mais condicoes sao verdadeiras

#or = confere se ao menos uma condicao e verdadeira

#not = inverte o resultado da condicao. verdadeiro é falso e vice-versa

temp_forno = 179

if temp_forno > 200 or temp_forno < 180:
    print("Temperatura incorreta.")

else:
    print("A pizza assou e está no ponto.")

tem_combustivel = True
tem_faisca = True
tem_compressao = False

if tem_combustivel == True and tem_faisca == True and tem_compressao == True:
    print("O motor funciona.")

else:
    print("O motor não funciona.")

agua_quente = False

if not agua_quente:
    print("Você não vai conseguir coar o café!")

else:
    print("Café coado com sucesso!")
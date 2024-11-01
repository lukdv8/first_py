email = input("Digite seu email: ")
print()

# index = email.index("@")

# nome = email[:index]
# dominio = email[index + 1:]
nome = email[:email.index("@")]
dominio = email[email.index("@") + 1:]

print(f"O nome é {nome} e o domínio é {dominio}")
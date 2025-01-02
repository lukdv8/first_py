value1 = 3.14159
value2 = 23.06
value3 = -706.11
value4 = 5000.4567

# arredonda casas decimais
print(f"O primeiro valor é ${value1:.2f}")
print()

# aloca espaços
print(f"O segundo valor é ${value2:30}")
print()

# aloca zeros
print(f"O terceiro valor é ${value3:030}")
print()

# centralizar
print(f"O segundo valor é ${value2:^30}")
print()

# direita
print(f"O segundo valor é ${value2:>30}")
print()

# esquerda
print(f"O primeiro valor é ${value1:<30}")
print()

# preceder com sinal aritmético
print(f"O primeiro valor é ${value1:+}")
print()

# separar milhas por vírgula
print(f"O quarto valor é ${value4:,}")
print()
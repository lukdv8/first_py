#solicita entrada do usuário
medida = input("Insira a medida: C para Celsius ou F para Fahrenheit: ")
temperatura = float(input("Insira a temperatura: "))

if medida == 'C':
    #converte celsius em fahrenheit
    temperatura = round((9 * temperatura) / 5 + 32, 1)
    print(f"{temperatura}°F")
    
elif medida == 'F':
    #converte fahrenheit em celsius
    temperatura = round((temperatura - 32) * 5 / 9, 1)
    print(f"{temperatura}°C")
    
#trata uma entrada incorreta
else :
    print(f"{medida} não é uma medida válida.")
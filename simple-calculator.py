operador = input("Digite um dos operadores + - * /: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    result = num1 + num2
    print(result)

elif operador == "-":
    result = num1 - num2
    print(result)

elif operador == "*":
    result = num1 * num2
    print(result)

elif operador == "/":
    result = num1 / num2
    print(result)
    
else:
    print(f"{operador} não é um operador válido.")
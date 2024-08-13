#Este é um projeto simples, apenas para usar as funcionalidades do GitHub, o usuário deve informar 2 números e selecionar uma operação de matemática básica e o programa deve retornar o resultado

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        print("Divisão por zero não é permitida")
    else:
        return num1 / num2

num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))

op=int(input("\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\nSelecione uma operação: "))

if op == 1:
    resultado = soma(num1, num2)
elif op == 2:
    resultado = sub(num1, num2)
elif op == 3:
    resultado = multi(num1, num2)
elif op == 4:
    resultado = div(num1, num2) 

else:
    print("Opção inválida")

print(f"Resultado = {resultado}")


#Este é um projeto simples, apenas para usar as funcionalidades do GitHub, o usuário deve informar uma string que deseja repetir e o número de repetições.

print("Bem vindo ao repetidor de textos!")
texto = input("Digite o texto que desejar:")
num = int(input("Quantas vezes deseja repetir?"))

for _ in range(num):
    print(texto)
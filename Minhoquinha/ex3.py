def calcular_media(lista):
    return sum(lista) / len(lista)

print("Escolha uma opção:")
print("1. Usar uma lista predefinida")
print("2. Inserir números manualmente")

opcao = int(input("Digite 1 ou 2: "))

if opcao == 1:
    lista_numeros = [10, 20, 30, 40, 50]
    print("Lista predefinida:", lista_numeros)

elif opcao == 2:
    lista_numeros = []
    print("Insira os números um de cada vez. Digite 0 para terminar.")

    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        lista_numeros.append(numero)

if lista_numeros:
    media = calcular_media(lista_numeros)
    print(f"A média dos valores na lista é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")

numbers = []

while True:
    number = int(input("Digite um número (0 para parar): "))
    
    if number == 0:
        break
    
    numbers.append(number)

print("Lista de números inseridos:", numbers)

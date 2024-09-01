def calcular_consumo_medio(lista_viagens):
    """
    Calcula o consumo médio de combustível para cada viagem e o consumo total médio

    Args:
    lista_viagens (list) Uma lista de tuplas onde cada tupla contém a distância percorrida e a quantidade de combustível consumido

    Return:
    tuple - Consumo médio por viagem e consumo total médio
    """
    consumos_por_viagem = []
    distancia_total = 0
    combustivel_total = 0

    for viagem in lista_viagens:
        distancia = viagem[0]
        combustivel = viagem[1]
        if combustivel > 0: 
            consumo = distancia / combustivel
            consumos_por_viagem.append(consumo)
        else:
            consumos_por_viagem.append(0) 
        distancia_total += distancia
        combustivel_total += combustivel

    if combustivel_total > 0:
        consumo_medio_total = distancia_total / combustivel_total
    else:
        consumo_medio_total = 0

    return consumos_por_viagem, consumo_medio_total

lista_viagens = []

while True:
    distancia = input("Digite a distância percorrida (km) ou '0' para finalizar: ")
    if distancia == '0':
        break
    combustivel = input("Digite a quantidade de combustível consumido (litros): ")
    
    # criando um try para o programa nao morrer se tentarem fazer algo com valor negativo (é impossível fazer com valor negativo)
    try:
        distancia = float(distancia)
        combustivel = float(combustivel)
        if distancia >= 0 and combustivel >= 0: 
            lista_viagens.append((distancia, combustivel))
        else:
            print("Por favor, insira valores não-negativos.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

consumos_por_viagem, consumo_medio_total = calcular_consumo_medio(lista_viagens)

print("\nConsumo de combustível por viagem (km/l):")
for i, consumo in enumerate(consumos_por_viagem, start=1):
    print(f"Viagem {i}: {consumo:.2f} km/l")

print(f"\nConsumo médio total (km/l): {consumo_medio_total:.2f}")
def validar_hora(hora):
    """
    Valida se a hora está no intervalo de 0 a 23
    
    Args:
    hora (int) Hora a ser validada
    
    Return:
    bool- True se a hora for válida, False caso contrário
    """
    return 0 <= hora <= 23

def validar_temperatura(temperatura):
    """
    Valida se a temperatura está no intervalo de -15°C a 60°C
    
    Args:
    temperatura (float) Temperatura a ser validada
    
    Return:
    bool - True se a temperatura for válida, False caso contrário
    """
    return -15 <= temperatura <= 60

def calcular_media_ponderada(horarios, temperaturas):
    """
    Calcula a média ponderada das temperaturas baseando-se nos intervalos de tempo entre os registros
    
    Args:
    horarios (list) Lista com os horários dos registros
    temperaturas (list) Lista com as temperaturas registradas
    
    Return:
    float - Média ponderada das temperaturas
    """
    if len(horarios) < 2:
        return 0.0
    
    soma_temperaturas = 0
    soma_pesos = 0
    
    for i in range(len(horarios) - 1):
        intervalo = horarios[i+1] - horarios[i]
        temperatura = temperaturas[i]
        soma_temperaturas += temperatura * intervalo
        soma_pesos += intervalo
    
    intervalo_final = 24 - horarios[-1]
    soma_temperaturas += temperaturas[-1] * intervalo_final
    soma_pesos += intervalo_final
    
    return soma_temperaturas / soma_pesos if soma_pesos != 0 else 0.0

def exibir_dados(horarios, temperaturas):
    """
    Exibe as informações de temperatura, incluindo a média ponderada, o horário e a temperatura mais baixa e mais alta
    
    Args:
    horarios (list) Lista com os horários dos registros
    temperaturas (list) Lista com as temperaturas registradas
    """
    if not horarios or not temperaturas:
        print("Nenhum dado disponível para exibição.")
        return
    
    media_ponderada = calcular_media_ponderada(horarios, temperaturas)
    
    temperatura_min = min(temperaturas)
    temperatura_max = max(temperaturas)
    hora_min = horarios[temperaturas.index(temperatura_min)]
    hora_max = horarios[temperaturas.index(temperatura_max)]
    
    print(f"\nMédia ponderada das temperaturas: {media_ponderada:.2f}°C")
    if 20 <= media_ponderada <= 30:
        print("A média está dentro do intervalo de segurança (20°C a 30°C).")
    else:
        print("A média está fora do intervalo de segurança (20°C a 30°C).")
    
    print(f"\nTemperatura mais baixa do dia: {temperatura_min:.2f}°C às {hora_min}:00")
    print(f"Temperatura mais alta do dia: {temperatura_max:.2f}°C às {hora_max}:00")

horarios = []
temperaturas = []

while True:
    entrada = input("Digite a hora (0-23) e a temperatura (°C), separados por espaço, ou 'Fim' para finalizar: ")
    if entrada.lower() == 'fim': #lembrando de colocar lower para nao dar erro se o usuario colocar FIM
        break
    
    try:
        hora_str, temperatura_str = entrada.split()
        hora = int(hora_str)
        temperatura = float(temperatura_str)
        
        if validar_hora(hora) and validar_temperatura(temperatura):
            horarios.append(hora)
            temperaturas.append(temperatura)
        else:
            print("Hora ou temperatura inválidos. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira os valores corretamente.")

exibir_dados(horarios, temperaturas)

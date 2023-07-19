# Função para calcular a diferença entre duas horas e minutos
def calcular_diferenca(hora1, minuto1, hora2, minuto2):
    # Converter as horas e minutos para minutos
    total_minutos1 = hora1 * 60 + minuto1
    total_minutos2 = hora2 * 60 + minuto2

    # Calcular a diferença em minutos
    diferenca_minutos = abs(total_minutos1 - total_minutos2)

    # Calcular a diferença em horas e minutos
    diferenca_horas = diferenca_minutos // 60
    diferenca_minutos = diferenca_minutos % 60

    # Retornar a diferença
    return diferenca_horas, diferenca_minutos

# Função para exibir o resultado em uma moldura
def exibir_resultado_moldura(texto, cor):
    tamanho = len(texto)
    print("\033[1;35m", "*" * (tamanho + 4), "\033[0m")
    print("\033[1;35m", "*", texto, "*", "\033[0m")
    print("\033[1;35m", "*" * (tamanho + 4), "\033[0m")

# Loop principal
while True:
    # Exibir a moldura inicial
    exibir_resultado_moldura("Diferença de Horas", "\033[1;35m")

    # Solicitar as horas e minutos do primeiro momento
    hora1 = int(input("Digite a primeira hora: "))
    minuto1 = int(input("Digite o primeiro minuto: "))

    # Solicitar as horas e minutos do segundo momento
    hora2 = int(input("Digite a segunda hora: "))
    minuto2 = int(input("Digite o segundo minuto: "))

    # Calcular a diferença
    diferenca_horas, diferenca_minutos = calcular_diferenca(hora1, minuto1, hora2, minuto2)

    # Criar o texto do resultado
    resultado_texto = "A diferença é de {} horas e {} minutos.".format(diferenca_horas, diferenca_minutos)

    # Exibir o resultado dentro da moldura verde
    exibir_resultado_moldura(resultado_texto, "\033[1;32m")

    # Perguntar ao usuário se deseja calcular outro valor
    resposta = input("Deseja calcular outra diferença de horas? (S/N): ")

    # Verificar a resposta do usuário
    if resposta.lower() != 's':
        break

    print()  # Pular uma linha antes de recomeçar o loop
9
# Calcuar valor de locadora de carro

def pegar_dias_de_locacao():
    dias = int(input('Quantos dias você deseja ficar com o carro? '))
    return dias

def calcular_valor_do_aluguel(dias):
    valor_diario = 100
    valorTotal = valor_diario * dias
    return valorTotal

def main():
    dias = pegar_dias_de_locacao()
    valorTotal = calcular_valor_do_aluguel(dias)
    print(f'O valor total do aluguel é R${valorTotal:.2f}')

main()
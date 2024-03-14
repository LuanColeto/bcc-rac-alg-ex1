# Calcular a idade de alguém

def pegar_ano_de_nascimento():
    ano = int(input('Em que ano você nasceu? '))
    return ano

def calcular_idade(anoNascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - anoNascimento
    return idade

def mostrar_idade(idade):
    print(f'Você tem {idade} anos.')

def main():
    anoNascimento = pegar_ano_de_nascimento()
    idade = calcular_idade(anoNascimento)
    mostrar_idade(idade)

main()
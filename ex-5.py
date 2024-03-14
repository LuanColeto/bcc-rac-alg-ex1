# Calcular idade em meses

def pegar_ano_de_nascimento():
  ano = int(input('Em que ano você nasceu? '))

  return ano


def pegar_mes_de_nascimento():
  mes = int(input('Em que mês você nasceu? (ex: 2) '))

  return mes


def calcular_idade_em_meses(anoNascimento, mesNascimento):
  from datetime import date
  ano_atual = date.today().year
  mes_atual = date.today().month
  idade = (ano_atual - anoNascimento)
  idadeEmMeses = idade  * 12 + mes_atual - mesNascimento

  return idadeEmMeses

def main():
  anoNascimento = pegar_ano_de_nascimento()
  mesNascimento = pegar_mes_de_nascimento()
  idadeEmMeses = calcular_idade_em_meses(anoNascimento, mesNascimento)
  print(f'Você tem {str(idadeEmMeses)} meses de idade.')


main()
# Calcular o preço de um produto por quilo

def pegar_valor_do_quilo():
    valor = float(input('Digite o valor do quilo do produto (em kg): '))
    return valor

def pegar_peso_do_produto():
  peso = float(input('Digite o peso do produto (em gramas):'))
  pesoEmQuilo = peso / 1000
  return pesoEmQuilo

def calcular_peso(valor, peso):
  total = valor * peso
  return total

def main():
  valorQuilo = pegar_valor_do_quilo()
  pesoDoProduto = pegar_peso_do_produto()
  totalASerPago = calcular_peso(valorQuilo, pesoDoProduto)

  print(f'O total a ser pago é  R${totalASerPago:.2f} ')

main()
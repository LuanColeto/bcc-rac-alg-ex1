# Calcular média de 4 notas

def pegar_notas():
  nota1 = float(input('Digite a primeira nota: '))
  nota2 = float(input('Digite a segunda nota: '))
  nota3 = float(input('Digite a terceira nota: '))
  nota4 = float(input('Digite a quarta nota: '))

  total = nota1 + nota2 + nota3 + nota4
  
  return total


def main():
  total = pegar_notas()
  media = total / 4
  print(f'A média das notas é {media:.2f}')

main()
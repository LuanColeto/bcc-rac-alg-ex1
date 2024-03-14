# Converter Celsius para Farenheit

def celsius_para_farenheit(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

def main():
    celsius = float(input('Digite a temperatura em Celsius: '))
    farenheit = celsius_para_farenheit(celsius)
    print(f'{celsius}°C = {farenheit}°F')

main()
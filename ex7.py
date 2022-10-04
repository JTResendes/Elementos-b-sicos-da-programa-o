"""Lê o número de horas de um empregado
"""



def salario(num1, num2):
    total = 0
    if num1 <= 40:
        salario = num1 * num2
        extra = 0
        total = salario + extra
    if num1 > 40:
        salario = (num1 * num2) - ((num1 - 40) * num2)
        extra = (num1 - 40) * (num2 * 2)
        total = salario + extra
    return total


while __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira as horas: '))
        num2 = int(input('Insira os preço/hora: '))
        print(f'O salário de {num1} horas é {salario(num1, num2)}')
        continuar = input('Quer continuar? [s, n] ')
    print('Adeus!')


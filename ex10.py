"""def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


impar = 0
num = int(input("Escreva um inteiro"))
print(str(format(num)))

print("Numeros pares e impares", )
"""


def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        numero_ls = []
        numero = input('Insira o numero: ')

        for letter in numero:
            numero_ls.append(letter)

        numero_lista = [int(item) for item in numero_ls]

        pares = par(numero_lista)

        print(pares)
        print(numero_lista)
        print(numero_ls)

        continuar = input('Quer continuar? [S, N]')
        if continuar == 'N':
            break
            #erro

primeiro = int(input("Digite o primeiro numero"))
segundo = int(input("Digite o segundo numero"))
terceiro = int(input("Digite o terceiro numero"))

maior = primeiro

if segundo > maior:
    maior = segundo
    if terceiro > maior:
        maior = terceiro

    print('Maior: ', maior)

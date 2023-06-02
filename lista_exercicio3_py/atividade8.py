atual = float(input("Digite a quantidade atual do estoque: "))
quantidade_maxima = float(input("Digite a quantidade máxima: "))
quantidade_minima = float(input("Digite a quantidade mínima: "))

quantidade_media = (quantidade_maxima + quantidade_minima) /2

if quantidade_media >= atual:
    print("Não efetuar compra.")
else:
    print("Efetuar Compra.")
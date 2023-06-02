qtd = float(input("Quantas maçâs você vai comprar? "))

if qtd >= 12:
    total = qtd * 1
    print("O valor de sua compra é: R$ %.2f" % total)
else:
    total = qtd * 1.30
    print("O valor de sua compra é: R$ %.2f" % total)
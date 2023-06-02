saldo = float(input("Digite seu saldo: "))
debito = float(input("Digite seu debito: "))
credito = float(input("Digite seu credito: "))

saldo_atual = saldo - debito + credito

print("Seu saldo atual é: %.2f" % saldo_atual)

if saldo_atual < 0:
    print("Seu saldo é negativo.")
else:
    print("Seu saldo é positivo.")
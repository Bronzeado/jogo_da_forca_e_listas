def calcula_peso(altura, sexo):
    if sexo == "M":
        peso = (72.7 *altura) - 58
    elif sexo == "F":
        peso = (62.1 * altura) - 44.7
    else:
        return "Resposta Inválida"    

    return peso

altura = float(input("Digite sua altura: "))
print("Considere M para Masculino e F para Feminino")
sexo = input("Sexo Masculino ou Feminino? ")

peso = calcula_peso(altura, sexo)
if isinstance(peso, str):
    print(peso)
else:
    print("O peso ideal é: %.2f" % peso, "kg")

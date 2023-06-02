a1 = float(input("Sua primeira nota: "))
a2 = float(input("Sua segunda nota: "))

media = (a1 + a2) / 2

if media >= 9 and media <= 10:
    print("Aprovado! Sua nota é: A")
elif media >= 7.5 and media < 9:
    print("Aprovado! Sua nota é: B")
elif media >= 6 and media < 7.5:
    print("Aprovado! Sua nota é: C")
elif media >= 4 and media < 6:
    print("Reprovado! Sua nota é: D")
else:
    print("Reprovado! Sua nota é: E")
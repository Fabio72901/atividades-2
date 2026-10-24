nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")

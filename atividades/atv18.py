dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if ano > 0 and ano <= 2026:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print("Data valida")
        else:
            print("Data inválida")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print("Data valida")
        else:
            print("Data invalida")
    elif mes == 2:
        if dia >= 1 and dia <= 28:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        print("Data invalida")
else:
    print("Data invalida")

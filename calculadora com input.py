def calculadora():
    while True:
        operador = input("digite uma operaçao(0=sair, 1=soma, 2=subtraçao, 3=multiplicaçao, 4=divisao)")
                
        if operador == '0':
            print("Encerrando. ")
            break
        elif operador not in['0', '1', '2', '3', '4']:
            print("Operador inválido. ")

        try:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))

            if operador == '1':
                calculo = num1 + num2
                print(calculo)

            elif operador == '2':
                calculo = num1 - num2
                print(calculo)

            elif operador == '3':
                calculo = num1 * num2
                print(calculo)

            elif operador == '4':
                try:
                    calculo = num1 / num2
                    print(calculo)
                except ZeroDivisionError:
                    print("Não é possivel dividir por zero! ")
        except ValueError:
            print("Apenas numeros")                                            

calculadora()
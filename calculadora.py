def calculadora(num1, num2, operador):
    if operador == 1:
        calculo = num1 + num2
        print(calculo)
        
    
    elif operador == 2:
        calculo = num1 - num2
        print(calculo)
    
    elif operador == 3:
        calculo = num1 * num2
        print(calculo)
    
    elif operador == 4:
        calculo = num1 / num2
        print(calculo)
    
    else:
        print(0)

calculadora(12, 20, 3)        
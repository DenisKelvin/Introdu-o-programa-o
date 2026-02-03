def Calculador_d_imc():
    Altura = float(input("Qual sua altura? "))
    Peso = float(input("Qual o seu peso? "))
    calculo_imc =  Peso / (Altura * Altura) 
    
    if calculo_imc <= 18.5:
        print("Abaixo do peso. ")
    
    elif calculo_imc > 18.5 and calculo_imc <= 24.9:
        print("Peso Normal. ")

    elif calculo_imc >= 25.0 and calculo_imc <= 29.9:
        print("Sobrepeso. ")

    elif calculo_imc >= 30.0 and calculo_imc <= 34.9:
        print("Obesidade Grau 1. ")

    elif calculo_imc >= 35.0 and calculo_imc <= 39.9:
        print("Obesidade Grau 2. ")

    elif calculo_imc > 39.9:
        print("Obesidade Grau 3(grave). ")                              

Calculador_d_imc()
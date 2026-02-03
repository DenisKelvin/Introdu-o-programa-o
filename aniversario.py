def aniversario():
    while True:
           try:
              nome_completo = input("Digite seu nome completo:")
              ano_atual = 2026
              ano_nascimento = int(input("Digite o ano que voçê nasceu: "))
              if ano_nascimento < 1926 or ano_nascimento > 2025:
                 print("Digite um ano entre 1926 e 2025. ")
              else:
                 idade_atual = ano_atual - ano_nascimento
                 print(nome_completo)
                 print(ano_nascimento)
                 print(f"Voce completou ou completara {idade_atual} anos neste ano. ")
                 break
           except ValueError:
              print("Digite apenas numeros. ")
           
aniversario()             
def num_pares():
    while True:
       pergunte = input("Digite 1 para inserir um numero ou 2 para sair: ")
       if pergunte == '2':
            print("Encerrando")
            break
       elif pergunte not in['1', '2']:
           print("Entrada invalida. digite 1 ou 2! ") 
        
       elif pergunte == '1':
           try:
              numero = int(input("Digite um numero par: "))
              if numero % 2 == 0:
                 print("Corretamente, o numero digitado é par. ")
              else:
                  print("O numero digitado é impar. digite um numero par. ")
                  
           except ValueError:
              print("letras nao sao validas. ")
           
           

num_pares()               


           
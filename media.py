nome = input("Digite o nome do aluno: ").lower()
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a primeira nota do aluno: "))

print(f"nome: {nome}")
print(f"primeira nota: {nota1}")
print(f"segunda nota: {nota2}")

media = (nota1 + nota2) / 2
print(f"media: {media}")

if media < 4:
    print ("Situação: reprovado")

elif media < 7:
    print("Situação: em recuperação")

elif media > 7:
    print("Situação: aprovado")    
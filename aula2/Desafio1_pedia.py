Nota1 = float(input("Insira a primeira nota do aluno "))
Nota2 = float(input("Insira a segunda nota do aluno "))
Media = ((Nota1*4)+(Nota2*6))/10

if (Media < 7):
    print(f"A media do aluno é {Media}, e está reprovado!")

elif (Media < 10):
    print(f"A media do aluno é {Media}, e está aprovado!")

else:
    print(f"A media do aluno é {Media}, e está aprovado com distinção!")

print("------AVALIAÇÃO DO ALUNO------")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Agora digite o total de faltas do aluno: "))

media = (nota1 + nota2)/2

if not nota1 < 10 or not nota2 < 10:
    print(f"Alguma das notas digitadas, {nota1} ou {nota2}, não existe. Favor repita toda a operação novamente")

elif media <= 3 or faltas >= 10:
    print(f"Aluno possui média {media} e teve {faltas} faltas")
    print("Aluno reprovado!!")

elif media >=6 and faltas == 0:
    print(f"Aluno possui média {media} e teve {faltas} faltas")
    print("Aluno aprovado!!")

elif media >= 7 and faltas < 10:
    print(f"Aluno possui média {media} e teve {faltas} faltas")
    print("Aluno aprovado!!")
else:
    print(f"Aluno possui média {media} e teve {faltas} faltas")
    print("Aluno em recuperação!!")






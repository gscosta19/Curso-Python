import random

numero_secreto = random.randint(1, 100)
raizq_num = numero_secreto ** 0.5
metade_terço = numero_secreto/2/2
num_potencia = numero_secreto ** 2 

print("Vocè terá 3 dicas para acertar o número")

for i in range(4):
    if i == 1:
        print(f"A raiz quadrada do número secreto é {raizq_num:.2f}.")
        num = int(input("Digite o número: "))

        if num < 1 or num > 100:
            print('Você digitou um número não solicitado. Digite outro: ')
            num = int(input("Digite o número correto: "))
        
        elif num == numero_secreto:
            print('Parabens, você GANHOU!!')
            break
        
        else:
            print('Você perdeu sua primeira chance. Vamos para 2ª dica: ')
        
    if i == 2:
        print(f"a metade da metade do número secreto é {metade_terço:.2f}.")
        num = int(input("Digite o novo número: "))

        if num < 1 or num > 100:
            print('Você digitou um número não solicitado. Digite outro: ')
            num = int(input("Digite o número correto: "))
        
        elif num == numero_secreto:
            print('Parabens,na segunda tentativa você GANHOU!!')
            break
        
        else:
            print('Você perdeu sua segunda chance. Vamos para 3ª dica: ')

    if i == 3:
        print(f"O quadrado do número secreto é {num_potencia:.2f}.")
        num = int(input("Digite o novo número: "))

        if num < 1 or num > 100:
            print('Você digitou um número não solicitado. Digite outro: ')
            num = int(input("Eita!! Tenha atenção. Digite o número dentro do intervalo: "))
        
        elif num == numero_secreto:
            print('Parabéns,na última tentativa você GANHOU!!')
            break
        
        else:
            print('Você perdeu sua última chance. Precisa melhorar muuuuuito!!')
                  
print('FIM')

        




    

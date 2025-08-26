n = 0

while n < 5:

    digitar = int(input("Digite um número de 1 a 3: "))

    if digitar == 1:
        print ("bom dia!")

    elif digitar == 2:
        print ("boa tarde!")

    elif digitar == 3:
        print ("boa noite!")    

    else:
        print ("digitação Incorreta. Favor digitar um número de 1 a 3. Tente novamente!")

    n = n +1 

    if n < 5:
        print(n)
    else:
        print("você já executou as {} tentativas disponíveis".format(n))




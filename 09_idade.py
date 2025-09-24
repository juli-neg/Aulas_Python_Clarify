executar = True

while executar:
    nome = input("Qual o seu nome?\n")
    anoNasc = int(input("Em que ano voce nasceu?\n"))
    anoAtual = int(input('Em que ano estamos?:\n'))

    idade = anoAtual - anoNasc
    print (f"Olá, {nome}. Você tem {idade} anos!")
    opcao = input("\nDeseja testar de novo? \nSim ou Não\n")
    if opcao == "Não" or opcao == "Nao" or opcao == "não" or opcao == "nao" or opcao == "n":
    
        executar = False


tipoEscola = input("Estuda em colegio: \n [1]Publico\n[2]Particular\n")
nomeAluno = input("Qual o nome do aluno?\n")
mediaAluno = int(input("Qual e media do aluno " + nomeAluno + "?\n"))
freqAluno = int(input("Qual a frequencia do aluno " + nomeAluno + "?\n"))

if tipoEscola == "2":
    print("---------- Escola Particular ----------")
    if mediaAluno >= 7 and freqAluno >= 70:
        status = "Aprovado"
    else:
        status = "Reprovado"

if tipoEscola == "1":
    print("---------- Escola Publica ----------")
    if mediaAluno >= 6 or freqAluno >= 70:
        status = "Aprovado"
    else:
        status = "Reprovado"

print(f"O Aluno {nomeAluno} foi {status} com media {mediaAluno}")
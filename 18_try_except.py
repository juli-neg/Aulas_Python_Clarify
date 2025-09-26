def divisao(a, b):

    try:
         # tente fazer isso
         resultado = a / b
         print(f"O resultado da divisão de {a} e {b} é: {resultado}")

    except ZeroDivisionError:
          # erro de divisão por zero
          print("Erro: Tentou dividir por 0? Tá errado, rapaz.")

    except TypeError:
         # erro de tipo
         print("Erro: Não dá pra dividir textos.")

    except Exception as descricao:
         #captura qualquer erro que nao pensamos
         print(f"É um erro inesperado: {descricao}")

    else:
         # só se tudo deu certo
         print("Divisão realizada com sucesso!")

    finally:
        # Sempre é executado com erro
        print("Processo de divisão concluido!")



divisao(10,2)
divisao(10,0)
divisao(10,"dois")
divisao("10",2)
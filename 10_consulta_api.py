import json, requests


nome = input("Qual o seu nome?\n")
resposta = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")

json_dados = json.loads(resposta.text)

print (json_dados[0]['res'][2])
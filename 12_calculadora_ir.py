def calculadora_ir(salario_bruto):
    tabela_ir = [
        {'faixa':(0,1903),             'aliquota':0,    'deducao':0},
        {'faixa':(1904,2826),          'aliquota':7.5,  'deducao':142},
        {'faixa':(2827,3751),          'aliquota':15,   'deducao':354},
        {'faixa':(3752,4664),          'aliquota':22.5, 'deducao':636},
        {'faixa':(4664,float("inf")),  'aliquota':27.5, 'deducao':869}
    ]
    imposto = 0
    for nivel in tabela_ir: 
        if salario_bruto > nivel["faixa"][0] and salario_bruto <= nivel["faixa"][1]:
            imposto = (salario_bruto * nivel ['aliquota']) / 100 - nivel["deducao"]
            break 
    return imposto 

    
salario_bruto = float(input("informe seu salario bruto:\n"))
imposto = calculadora_ir(salario_bruto)
liquido = salario_bruto - imposto
print(f"O Imposto de renda devido é de R$ {imposto}")
print(f"Você receberá miseros: {liquido}")
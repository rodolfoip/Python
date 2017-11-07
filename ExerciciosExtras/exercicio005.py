# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valorHora = float(input('Digite o valor da sua hora de trabalho: '))
qtdHora = float(input('Digite a quantidade de horas trabalhadas: '))

salarioBruto = valorHora * qtdHora
salarioLiquido = 0

descontoSindicato = salarioBruto * 0.03
FGTS = salarioBruto * 0.11
descontoINSS = salarioBruto * 0.1
if 900 >= salarioBruto <= 1500:
    descontoIr = salarioBruto * 0.05
elif salarioBruto <= 2500:
    descontoIr = salarioBruto * 0.1
else:
    descontoIr = salarioBruto * 0.2
totalDescontos = (descontoIr + descontoINSS + descontoSindicato)
salarioLiquido = salarioBruto - totalDescontos
print('-=' * 15)
print("""Folha de pagamento
Salário Bruto:      {}
(-) INSS:           {}
(-) IR:             {}
FGTS:               {}
(-) Sindicato:      {}
Total de descontos: {}
Salário liquido:    {}""".format(salarioBruto, descontoINSS, descontoIr, FGTS, descontoSindicato, totalDescontos, salarioLiquido))
print('-=' * 15)

#1 - FAZER UMA ESTRUTURA DE IF/ELIF/ELSE QUE
#VERIFIQUE SE O DIA É DIA DE SEMANA OU NÃO

diaS = str(input("Digite o dia da semana: ")).lower().strip()

if diaS == "segunda" or diaS == "terça" or diaS == "quarta" or diaS == "quinta" or diaS == "sexta":
    print("É dia de semana")
else:
    print("Não é dia de semana")

#2 - FAZER UMA ESTRUTURA DE IF/ELIF/ELSE QUE
#VERIFIQUE SE UMA PESSOA PODE DIRIGIR OU NÃO,
#LEVANDO EM CONSIDERAÇÃO AS VARIÁVEIS
#TEM_CARTEIRA E IDADE

while True:
    temCarteira = str(input("Você possui carteira de motorista? (Sim/Não): ")).lower().strip()
    if temCarteira == "sim":
        temCarteira = True
        break
    elif temCarteira == "nao" or temCarteira == "não":
        temCarteira = False
        break
    else:
        print("Entrada inválida para temCarteira. Por favor, digite 'Sim' ou 'Não'.")

idade = int(input("Digite a sua idade: "))

if temCarteira and idade >= 18:
    print("A pessoa pode dirigir")
else:
    print("A pessoa não pode dirigir")

#3 - FAZER UMA ESTRUTURA DE IF/ELSE/ELIF QUE
#VERIFIQUE A ALTURA DE UMA PESSOA, DIZENDO SE
#ELE TEM NANISMO, SE É BAIXO, MÉDIO, ALTO, OU TEM
#GIGANTISMO

altura = float(input("Digite a altura da pessoa (em metros): "))

if altura < 1.40:
    print("A pessoa tem nanismo")
elif 1.40 <= altura < 1.60:
    print("A pessoa é baixa")
elif 1.60 <= altura < 1.80:
    print("A pessoa é de altura média")
elif 1.80 <= altura < 2.00:
    print("A pessoa é alta")
else:
    print("A pessoa tem gigantismo")
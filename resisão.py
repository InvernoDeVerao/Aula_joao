#REVISAO


"""if = executa uma condição verdadeira 
 elif= se nao, ou seja se if nao for verdadeiro, o elif sera acionado, elif serve para criar condicoes, voce pode adicionar varias.
 em caso de mais elifs 
 elif 1 falso
 elif 2 verdadeiro
 elif 3 ignorado
 caso algum elif seja verdadeiro os outros serao ignorados
 else = se nem if e nem elif nao for verdadeiro, else sera acionado

"""

"""if idade > 18 or autorizacao
if autorizacao and responsavel """

"""tempo_limpo = True 
tempo_sujo = False
dia_da_semana= True

if dia_da_semana and tempo_limpo:
    print("vou de bike")
elif dia_da_semana and tempo_sujo:
    print("vou de carro")
else:
    print("n vou pra escola")"""


"""voce pode fazer um codigo somente com if
exp
if email_valido:
    print ('enviar email')# nesse caso, se for verdadeiro ira aparecer "email enviado" caso nao seja, nao é necessario retornar nada, 
    é possivel usar o return dentro de uma função, como por exemplo o def, colocando para retornar "email nao enviado"""
"""exp
email_valido = True

def enviar_email(email):
    if email:
        return "Enviar email"
    return "Email inválido"

print(enviar_email(email_valido))"""


tempo_limpo = True
Tempo_sujo = False
dia_da_semana = False

if dia_da_semana and tempo_limpo:
    print('Ir de bike para a escola')
elif dia_da_semana and Tempo_sujo:
    print('Ir de carro para a escola')
else:
    print('Não é necessário ir para a escola')

email_valido = True

def enviar_email(email):
    if email:
        return "Enviar email"
    return "Email inválido"

print(enviar_email(email_valido))



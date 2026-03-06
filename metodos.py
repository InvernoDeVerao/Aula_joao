"""
Métodos são blocos de codigo que realizam tarefas especificas, e podem ser reutilizadas em diferentes partes do programa
eles são definidos usando a palavra-chave "def", seguida pelo nome do metodo, e entre parenteses, os parametros que o metodo recebe
os parametros são variaveis que são passadas para o metodo quando ele pe camdo e podem ser usadas dentro do metodo para realizar a 
tarefa especifica.!
"""
'''
cadastro = [
    {
        "username": "erick123",
        "password": "erickizinho",
    },
    {
        "username": "vinizão",
        "password": "soygay",
    },
    {
        "username": "tiaga",
        "password": "LiviaVolta",
    }
    ]
'''
'''
def saudacao (nome):
    print (f"ola, {nome}! ")

saudacao('maria')
saudacao('juakin')
saudacao('lunierle')
'''
'''
def formatacao_username(username):
    return username.replace(' ','').lower()

def cadastrar(valid_username, password):
    valid_username = formatacao_username(valid_username)
    print(valid_username)
    for cadastros in cadastro:
        if cadastros["username"] == valid_username:
            print ('Usuario já cadastrado')
            return
    cadastro.append({
        "username": valid_username,
        "password": password,
    })
    return'Usuario cadastrado com exito'

def soma(x,y):
    resultado = x+y
    return resultado



print (cadastrar("murile sadia", "murila123321"))
print (cadastrar("je qu ei ra", "jocaira"))
print (cadastrar("viDa", "23321"))
print (cadastrar("buraca", "fad"))

print (soma (10,20))

def atualizar_senha(lista, username, new_password):
    valid_username = formatacao_username(username)
    for user in lista:
        if user ['username'] == valid_username:
            user['password'] = new_password
            return 'Senha alterada com sucesso'
    return 'Usuario não encontrada'

print (atualizar_senha(cadastro, 'erick123', 'piupiucabelo'))
'''
usuario = [
    {
        "id": 1,
        "username": "erick",
        "password": "erick1",
    },
    {
        "id": 2,
        "username": "vini",
        "password": "vini1",
    },
    {
        "id": 3,
        "username": "tiaga",
        "passw,ord": "tiaga1",
    },
    {
        "id": 4,
        "username": "jurema",
        "password": "jurema1",
    },
    {
        "id": 5,
        "username": "natan",
        "password": "natan1",
    },
    ]

def mudar_user(id_busca, new_user, new_password):
    for user in usuario:
        if user["id"] == id_busca:
            user["username"] = new_user
            user["password"] = new_password
            return "deu certo"
    return "n deu"

resultado = mudar_user(4, "juma", "erick123")
print(resultado)
print(usuario[4])
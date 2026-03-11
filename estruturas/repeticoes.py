"""pessoas = [
    {
    "nome": "joao", 
    "idade": 30},
    {#pessoa 1, INDEX 0
    "nome": "erick", 
    "idade": 17},
    {#pessoa 2, INDEX 1
    "nome": "isaque", 
     "idade": 123}"""
#pessoa 3, INDEX 2

#nomes = []#cria lista vazia para armazenar os nomes e idades

#nomes.append(pessoas[0]["nome"])#add o valor do atributo "nome" da pessoa 1 na lista nomes
#nomes.append(pessoas[1]["nome"])#add o valor do atributo "nome" da pessoa 2 na lista nomes
#nomes.append(pessoas[2]["nome"])#add o valor do atributo "nome" da pessoa 3 na lista nomes
#print(f'{nomes}')
      

"""for pessoa in pessoas:#automatica o treco de cima, ele percore a lista pessoas pegando os atributos desejados (nome e idade).
    nomes = pessoa['nome']
    idades = pessoa['idade']
    print(f'{nomes}, {idades}')"""

"""
nome = []
idade = []
for pessoa in pessoas:
    nome.append(pessoa["nome"])
    idade.append(pessoa["idade"])
print(f'{nome}, {idade}')

nome.append(input("digite o nome: " ))
idade.append(int(input("digite sua idade: ")))
print(f'{nome}, {idade}')"""

#list comprehensioin
"""nomes = [pessoa["nome"] for pessoa in pessoas]
idades = [pessoa["idade"] for pessoa in pessoas]
print (f'{nomes}, {idades}')"""
"""
users = [
    {"id": 1, "name": "joao", "active": True},
    {"id": 2, "name": "marta", "active": False},
    {"id": 3, "name": "pedro", "active": True},
    {"id": 4, "name": "adolf", "active": True},
    {"id": 5, "name": "mirabel", "active": False},
    {"id": 6, "name": "epstein", "active": True},
    {"id": 7, "name":  "frank", "active": True},
    {"id": 8, "name": "P.diddy", "active": False},
    {"id": 9, "name": "Justin", "active": True},
    {"id": 10, "name": "stalin", "active": True},
    {"id": 11, "name": "mussolini", "active": False},
    {"id": 12, "name": "robinho", "active": True}

]
active_users = [(user["id"], user["name"]) for user in users if user ["active"]] #["name"] captura só o nomee ["id"] só o ID
print(f"active_users: \n{active_users}\n")
inative_users = [(user["id"], user["name"]) for user in users if not user ["active"]]
print(f"inative_users: \n{inative_users}\n")

number = 12.123123123532423123

resultado = (number)
print(f"{resultado:.3f}")


ids_user = [user["id"] for user in users]
print (ids_user)

ids_active = [user["id"] for user in users if ["active"]]
print (ids_active)

ids_desable = [user["id"] for user in users if not user ["active"]]
print (ids_desable)

preco = [100.0, 250.0, 80.0, 150.0]
desconto10 = [item * 0.9 for item in preco]
desconto20= [item * 0.8 for item in preco]
desconto30= [item * 0.7 for item in preco]
desconto40= [item * 0.6 for item in preco]
desconto50= [item * 0.5 for item in preco]

print ("Preço reau: ", preco)
print ("desconto de 10 reau: ", desconto10)
print ("desconto de 20 reau: ", desconto20)
print ("desconto de 30 reau: ", desconto30)
print ("desconto de 40 reau: ", desconto40)
print ("desconto de 50 reau: ", desconto50)





raw_emails = [
    "JOAO@email.com ",
    "thYago@email.com",
    "ERike@gmail.com",
    "GabrimARo@gmail.sem",
]
srtip remove os espaços brancos do inicio ao fim da string, nao remove espaço no meio  das frases
striped_emails = [email.strip() for email in raw_emails]

print(f'emails sem espaços : {striped_emails}')

lower() converte a string para letras minusculas


lower_emails = [email.lower () for email in raw_emails]
print(f' emails em minusculo: {lower_emails} ')


emails = [email.strip().lower() for email in raw_emails]
print('Emails limpos: {emails}\n\n\n')

emails = [
    "J O A O@email.com ",
    "tH  Y  agO@email.com",
    "E  r i ke@  gmail.com",
    "Ga br imA Ro@ gmail.sem",
]

emails_limpos = [
    email.lower()
    .replace(" ", "")
    for email in emails

]
print(emails_limpos)
"""

"""list comprenchion é uma forma concisa"""
# de criar listas a partir de interaveis,
# aplicando uma expressao a cada irem e opiconalmente filtrando os itens com uma condição. a sintaxe basica é 
# nova_lista = [expressao for item in iteravel if condicao]



"""for sem lista, ele repete por um numero especifico de vezes,ou seja, ele itera sobre um intervalo de numeros"""
"""
for i in range(5):
 print(f'iteração {i}')

for i in range (1,6):
  print(f'iteração {i}')

  
for i in range(0, 10, 2):
 print(f'iteração {i}')

 for i in range (10,0,-1):
  print(f'iteração {i}')


  for i in range (5):
    if i % 2 == 0:
     print(f'iteração {i} é par')
    else:
      print(f'iteração {i} é impar')
"""
#pq do I em for
#para cada elemento i do iterável, faça algo
#iteraveis:
#lista, tuplas, dicionario, conjunto, string

#lista [1,2,3]
#iteravel = i[0] = 1, i[1] = 2, i[2] = 3

usuario = [
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

def login(username, password):
    for unicornio in usuario:
        if unicornio["username"] == username and unicornio ["password"] == password:
            return "login com sucesso"
    return "login falho"

print (login ("erick123", "erickizinho"))
print (login ("vinizão", "soygay"))
print (login ("tiaga", "LiviaVolta"))

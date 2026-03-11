nome = 'Thyago' #string
idade = 17 #int
altura = 1.50 #float
casado = True #boolean

#print ('{} tem {} anos.'.format (nome, idade)) ANTIGO

if idade >= 60:
    print(f'{nome} é idoso.')
elif idade >= 18:
    print(f'{nome} é maior de idade.')

if altura >= 1.80:
        print(f'{nome} é alto')
elif altura >= 1.60:
     print(f'{nome} é de estatura média')
elif altura >= 1.40 and altura <1.60:
     print (f'{nome} tem altura baixa')

if casado:
     print(f'{nome} é casado.')
elif not casado:
     print(f'{nome} é não casado.')


nomes = ['Thyago', 'felicima', 'miago']

if nome in nomes:
    print(f'{nome} está na lista.')

idade1=17
autorizacao = False

if idade1 >= 18 or autorizacao:#um dos dois precisa estar verdadeira.
     print('pode entrar na festa.')
else:
     print('não pode entrar na festa.')

     class maconheiro:
          def __init__ (self, nome, idade, doenca, comprador,):
               self.nome = nome
               self.idade = idade
               self.doenca = doenca
               self.comprador = comprador
     
     user1 = maconheiro ("Kelwin", 16, "HIV", "Alan")

     print (f"o {user1.nome}, tem {user1.idade}, com a doenca {user1.doenca}, e compra drogas do {user1.comprador}")

     contador = 0

while True:
     print('escolha entre 1 e 2 e qualquer outra coisa pra sair:')
     contador = int(input())
     if contador == 1:
          print ('Caguei na roupa')
     elif contador == 2:
          print ('Não caguei na roupa')
     else:
          print('fechou!')
          break
#alterei na escola.


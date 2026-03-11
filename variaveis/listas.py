nomes = ['erick', 'Vini', 'joaozin', 'pedro']
"""
print (nomes[0])
print (nomes[1])
print (nomes[2])
print (nomes[3])
#por INDEX

print(nomes[-1])
print(nomes[-2])
print(nomes[-3])
print(nomes[-4])
#Pelo tamanho da lista -1=ultimo -2=penultimo...
"""
print (nomes)
nomes[0] = 'carlos'#altera por INDEX
nomes[1] = 'adolf'
nomes[2] = 'hitler'
nomes[3] = 'stalin'
print (nomes)

nomes.append('Kelwin')#coloca no final da lista
print (nomes)

nomes.remove('Kelwin')#remove pelo nome/valor
print (nomes)

del nomes[0]#remove pelo INDEX
print (nomes)

nomes.insert(0, 'carla')#



contador = 0
nome = ''
while True:
     print('escolha 1 para adicionar um nome e 2 para sair')
     contador = int(input())
     if contador == 1:
        nome = input('Digite o nome: ')
        nomes.append(nome) 
        print(nomes)
     elif contador == 2:
          break
     

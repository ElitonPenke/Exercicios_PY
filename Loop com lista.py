'''1 - Crie um programa para elaborar uma lista de convidados de uma festa,
o programa irá perguntar o nome do convidado, você digitará o nome e ao
terminar a lista, o programa irá exibir a lista em ordem alfabética. Insira até 10 nomes.'''

CONVIDADOS=[]

while True:
    convidado=input('Digite um nome:')
    convidado= convidado.upper()
    if convidado =='FIM':
        break
    else:
        CONVIDADOS.append(convidado.title())
CONVIDADOS.sort()
i=0
for convidado in CONVIDADOS:
    i=i+1
    print(f'{i}°{convidado}')

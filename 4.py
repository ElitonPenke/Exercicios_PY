import random
nome_jogador1: str = ''
nome_jogador2: str = ''
escolha_jogador1: str = ''
escolha_jogador2: str = ''
num_jogador1: int = 0
num_jogador2: int = 0
resultado: str = ''

while True:
    continuar=input('Quer jogar???S/N:  ').lower()
    if continuar=='s': 
        print("\n----------------------------------------------------------------------------------------------------------\n")
        nome_jogador1=input('Diga o nome do 1° jogador:  ')
        nome_jogador2=input('Diga o nome do 2° jogador:  ')    

        print("\n----------------------------------------------------------------------------------------------------------\n")
        primeiro_aescolher= random.choice([nome_jogador1,nome_jogador2])

        if primeiro_aescolher == nome_jogador1:
            segundo_jogador = nome_jogador2
        else:
            segundo_jogador = nome_jogador1

        while True:
            try:
                escolha_jogador1=input(f'Jogador {primeiro_aescolher}. Qual quer: PAR ou ÍMPAR\n').lower()
                print("\n----------------------------------------------------------------------------------------------------------\n")

                break
            except:
                print('ERRO. Digite novamente um numero:')

        if escolha_jogador1 == 'par':
            escolha_jogador2 ='impar'
        else:
            escolha_jogador2 ='par'
        while True:
            try:
                num_jogador1=int(input(f'Jogador {nome_jogador1}. Digite algum número:\n'))
                num_jogador2=int(input(f'Jogador {nome_jogador2}. Digite algum número\n'))
                break
            except:
                print('ERRO. Digite novamente um numero:')

        soma_dos_numeros=num_jogador2+num_jogador1

        if soma_dos_numeros % 2 == 0:
            resultado= 'par'
        else:
            resultado ='impar'
            
        if resultado == escolha_jogador1:
            print(f'{nome_jogador1} Você ganhou!!!')
        else:
            print(f'{nome_jogador2} Você ganhou!!!')
    else:
        print("\n-----------------------------PROGRAMA ENCERRADO-----------------------------------------\n")

        break
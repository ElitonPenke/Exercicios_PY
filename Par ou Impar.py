import random

while True:
    continuar = input('Quer jogar??? S/N: ').lower()
    if continuar != 's':
        print("\n----------------------------- PROGRAMA ENCERRADO -----------------------------------------\n")
        break

    print("\n----------------------------------------------------------------------------------------------------------\n")
    nome_jogador1 = input('Diga o nome do 1° jogador: ')
    nome_jogador2 = input('Diga o nome do 2° jogador: ')

    print("\n----------------------------------------------------------------------------------------------------------\n")
    primeiro_aescolher = random.choice([nome_jogador1, nome_jogador2])

    # Determina o segundo jogador
    if primeiro_aescolher == nome_jogador1:
        segundo_jogador = nome_jogador2
    else:
        segundo_jogador = nome_jogador1

    # Escolha par ou ímpar pelo primeiro
    while True:
        escolha_primeiro = input(f'Jogador {primeiro_aescolher}, escolha: PAR ou ÍMPAR\n').strip().lower()
        if escolha_primeiro in ['par', 'impar']:
            break
        print('ERRO. Digite apenas "par" ou "impar".')

    # Define a escolha do segundo automaticamente
    if escolha_primeiro == 'par':
        escolha_segundo = 'impar'
    else:
        escolha_segundo = 'par'

    # Entrada dos números
    while True:
        try:
            num_primeiro = int(input(f'Jogador {primeiro_aescolher}, digite um número: '))
            num_segundo = int(input(f'Jogador {segundo_jogador}, digite um número: '))
            break
        except ValueError:
            print('ERRO. Digite novamente um número válido.')

    # Soma e resultado
    soma = num_primeiro + num_segundo
    resultado = 'par' if soma % 2 == 0 else 'impar'

    print(f"\nSoma: {soma} → Resultado: {resultado.upper()}")

    # Determina vencedor corretamente
    if resultado == escolha_primeiro:
        print(f"{primeiro_aescolher}, você ganhou!!!")
    else:
        print(f"{segundo_jogador}, você ganhou!!!")

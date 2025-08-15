print("\n ------------------------------Algoritmo da Amizade------------------------------ \n")
while True:
    ligação = input('Você ligou para a pessoa, ele/ela atendeu? ')
    ligação = ligação.lower()
    
    if ligação == 'sim':
        Conviterefeicao = input('Ele/ela atendeu. Você convidou para uma refeição. Ele/ela aceitou? ')
        Conviterefeicao = Conviterefeicao.lower()
        
        if Conviterefeicao == 'sim':
            print('Amizade feita')
            break
        else:
            convitebebida = input('Ele/ela não aceitou a refeição, porém você convidou para uma bebida. Ele/ela aceitou? ')
            convitebebida = convitebebida.lower()
            
            if convitebebida == 'sim':
                print('Oferece essas bebidas:\n Café\n Chá\n Chocolate')
                bebidaescolhida = input('Qual bebida ele/ela escolheu? ')
                print(f'Então está marcado. Vamos beber {bebidaescolhida}. Amizade feita')
                break
            else:
                for i in range(3):
                    sugestao = input('Você perguntou se ele tem algum interesse que gostaria de fazer juntos. O que ele disse? ')
                    repostasua = input('Você, particularmente, aceitou a ideia? ')
                    
                    if repostasua == 'não':
                        continue
                    else:
                        print(f'Vamos fazer {sugestao} amanhã\nAmizade feita!!!')   
                        break
    else:
        continue

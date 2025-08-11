import operacoes #ou chamar 'import from print  operacoes *'

operacao=''
while True:
    operacao=input("\n Deseja calcular qual operação?\n-1 para soma\n-2 para subtração\n-3 para divisão\n-4 para multiplicação\n")
    if operacao == '1':
        num1=int(input('digite um numero: '))          #pede os numeros
        num2=int(input('me diga outro numero: '))      #pede os numeros
        print(operacoes.soma(num1,num2))    #chama o outro modulo, ai chama a def soma passando os parametros num1 e 2 dentro das ()

    elif operacao == '2':
        num1=int(input('digite um numero: '))          #pede os numeros
        num2=int(input('me diga outro numero: '))      #pede os numeros
        print(operacoes.sub(num1, num2))
    
    elif operacao=='3':
        num1=int(input('digite um numero: '))          #pede os numeros
        num2=int(input('me diga outro numero: '))      #pede os numeros
        print(operacoes.div(num1,num2))

    elif operacao=='4':
        num1=int(input('digite um numero: '))          #pede os numeros
        num2=int(input('me diga outro numero: '))      #pede os numeros
        print(operacoes.mult(num1,num2))
    
    else: 
        print('Não existe essa operação')

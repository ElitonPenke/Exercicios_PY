#Metodo para ver o tipo de uma variavel type()
var_x = 10
print(type(var_x))

'''da para usar varios estilos de programação 

Paradigma funcional: uma função que dobra um número'''
def dobro(x):
    return x * 2

#cria uma lista
numeros = [1, 2, 3, 4]

# Usando map (funcional) para aplicar a função 'dobro' a cada número da lista
resultado = list(map(dobro, numeros))

# Paradigma orientado a objetos: criando uma classe Calculadora
class Calculadora:
    def __init__(self, valores):
        self.valores = valores
    def somar(self):
        return sum(self.valores)
    
# Criando um objeto 'calc' da classe Calculadora (OO)
calc = Calculadora(resultado)

# Usando o método somar do objeto 'calc' e imprimindo o resultado (estruturado)
print("Soma final:", calc.somar())

'''Nesse código, usamos uma função dobro (estilo funcional), criamos uma class
Calculadora e um objeto calc (estilo orientado a objetos), e no final, imprimimos o'''

#Em python,teoricamente, tudo é um objeto

minha_variavel='ABC'
print(dir(minha_variavel)) #MOSTRA TODOS OS ATRIBUTOS E METODOS

#Operadores(int and float)------------------------------------------------------------------------

2 + 2
4 # Resultado inteiro, pois ambos os operandos são inteiros(int)

(50 - 5 * 6) / 4
5.0 # Resultado float, pois a divisão (/) sempre retorna um float

7 // 3 # Divisão inteira: retorna apenas a parte inteira do resultado
2

7 / 3.0 # Divisão real: um dos operandos é float, então o resultado é float
2.3333333333333335


#Listas(mutaveis)--------------------------------------------------------------------------------------
minha_lista=[1,2,3,4,5,6,'uma frase','uma palavra']
print(minha_lista)

minha_lista[3]=4444 #mudando o elemento 4 para o n 4444
print(minha_lista)

minha_lista.append('mais uma palavra acrescentada ') #acrescentar mais uma variavel denrto da lista
print(minha_lista)

minha_lista.remove(2) #removendo um elemnto qualquer 
print(minha_lista)

#Dicionarios(chave:valor)--------------------------------------------------------------------------
meu_dici={'palavra':'significado','violão':'instrumento','caixa':'conteudo para quardar coisas'}
print(meu_dici)

print(meu_dici['palavra'])  

meu_dici['sintaxe']='termo em desuso' #adicionando um novo chave:valor em meu dicionario
print(meu_dici)

#Tuplas---------------------------------------------------------------------------------------------
# (imutaveis)(tipo uma lista, porem tem mais desempenho)

minha_tupla=(10,2,3,4,5,'uma palavra','uma frase')
print(minha_tupla)
print(minha_tupla[3])

tupla1=(1,2,3)
tupla2=(4,5,6)

tupla3=tupla1+tupla2 # posso concatenar para criar uma nova, mas nunca modificar 
print(tupla3)

#   Conjuntos --------------------------------------------------------------------------------------
# {} ou a função SET(), POREM É UNICO, N DEIXANDO REPETIÇÃO
meu_conjunto=set([1,2,3,4,5,6,7,7,7,8,8,8,8])
print(meu_conjunto)# so vai imprimir {1, 2, 3, 4, 5, 6, 7, 8}
#OU
meu_conjunto2={1,2,3,7,5,5,5,4,5}
print(meu_conjunto2) #vai imprimir so {1, 2, 3, 4, 5, 7}

"""Para os conjuntos conceitos de union, intersection, difference são aplicaveis a esse tipo de dados"""

#Operadores Relacionais-------------------------------------------------------
''' 
== Igual a
!= Diferente de
> Maior que
< Menor que
>= Maior ou igual a
<= Menor ou igual a
'''
#EX
idade=18

if idade < 18:
    print('menos de idade')
else:
    print('maior de idade')

#para retornar o booleano(false ou true)
print(idade>18) #false
print(idade==18)#true

#Operadores Lógicos----------------------------------------------------------------
'''
and   E: Retorna True se ambas as condições forem verdadeiras
or    OU: Retorna True se pelo menos uma das condições for verdadeira
not   NÃO: Inverte o resultado da condição (de True para False e vice-versa)
'''

a=10
b=5
print(a>10 and b>50) #false
print(a<40 or b>5) #true


#laços de repetição (for e while)-------------------------------------------------

count =1               #contador de começa com 1
while count <= 10:     #o loop continua enquanto o contador for menor ou igual que 10
    print(count)       #mostra o contador
    count+=1           #a cada loop ele adiicona mais um no contador

print('acabou')        #quando o loop acabar ele mostra 'acabou'


#OU

soma=0
while True:
    algum_numero=int(input('diga um numero: '))  #sempre pede um numero

    if algum_numero == 1:                        #compara o numero se é um 1, se for, para o loop
        break
    else:
        soma=soma+algum_numero                   #mas se n, ele soma o numero antigo com o novo e diz ele
        print(soma)

print('acabou')


#podemos usar o 'continue' em algum momentos para que o loop, apenas continue e n pare, assim pulando para a prox. linha

nomes={'eliton','gustavo','gruztmann','penke','joao'}

for nome in nomes:  #para cada nome dentro da lista nomes
    print(nome)     #diga o nome dentro, um por vez

#ou usar o 'range' para loop com quantidades que sabemos 

for i in range(1,20):   #vai mostrar tds os numero entre 1 e 20
    print(i)

#também da para fazer em letras(strings)

for letra in 'ELITON':  #diz cada letra por letra
    print(letra)

#------------------------------------------------------------------------------------------------------------------------
#exemplos

def calculadora():
    print("------------------------------------------- Calculadora Simples -------------------------------------------")

    # Recebe os números do usuário
    num1 = float(input("Digite o primeiro número: ")) #define os tipos em 'quebrados'
    num2 = float(input("Digite o segundo número: "))

    # Recebe a operação desejada
    operacao = input("Escolha a operação (+, -, *, /): ")

    # Realiza a operação com base na escolha do usuário
    if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é {resultado}")

    elif operacao == '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é {resultado}")

    elif operacao == '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é {resultado}")
        
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é {resultado}")
    else:
        print("Operação inválida!")

    # Chama a função para executar a calculadora
calculadora()
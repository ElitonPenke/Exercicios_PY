class Usuario():
    def __init__(self, primeiro_nome, segundo_nome, idade, sexo, cidade):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade

    def saudacao(self):
        print(f'\nSaudações {self.primeiro_nome} {self.segundo_nome}, seja bem-vindo ao nosso sistema!!!!')
       
    def descricao_usuario(self):
        print(f'O nome desse usuario é {self.primeiro_nome} {self.segundo_nome}.')
        print(f'O usuario tem {self.idade} anos.')
        print(f'O usuario {self.primeiro_nome} é {self.sexo}.')
        print(f'O usuario mora em {self.cidade}.')

def cadastro():
    primeiro_nome = input('Me diga seu 1° nome: ')
    segundo_nome = input('Me diga o seu 2° nome: ')
    idade = input('Me diga sua idade: ')
    sexo = input('Me diga seu sexo: ')
    cidade = input('Me diga a sua cidade: ')
    return Usuario(primeiro_nome, segundo_nome, idade, sexo, cidade)

usuarios = []

while True:
    continuar = input('\nDeseja cadastrar um usuário? (para sair, digite "não"): ')
    if continuar.lower() == 'não':
        print('----------------------------------------------------------- \n')        
        print('Esses são todos os usuario cadsatrados no sistema: \n')
        break
    else:
        usuario = cadastro()
        usuarios.append(usuario)

for usuario in usuarios:
    usuario.saudacao()
    usuario.descricao_usuario()

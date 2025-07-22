class Usuario():
    def __init__(self,primeiro_nome,segundo_nome,idade,sexo,cidade):
        self.primeiro_nome=primeiro_nome
        self.segundo_nome=segundo_nome
        self.idade=idade
        self.sexo=sexo
        self.cidade=cidade
   
    def descricao_usuario(self):
        print(f'O nome dele é {self.primeiro_nome} {self.segundo_nome}')
        print(f'Ele tem {self.idade}')
        print(f'o {self.primeiro_nome} é {self.sexo}')
        print(f'E ele é da {self.cidade}')
   
    def saudacao(self):
        print(f'\nSaudações {self.primeiro_nome} {self.segundo_nome}, seja bem vindo ao nosso sistema!!!!\n')

usuario1 = Usuario('Eliton', 'Penke', 19, 'masculino', 'Santa Rosa')
usuario2 = Usuario('Larissa', 'Müller', 22, 'feminino', 'Porto Alegre')
usuario3 = Usuario('Carlos', 'Silva', 25, 'masculino', 'Caxias do Sul')
usuario4 = Usuario('Juliana', 'Rocha', 18, 'feminino', 'Pelotas')
usuario5 = Usuario('Mateus', 'Oliveira', 21, 'masculino', 'Passo Fundo')
usuario6 = Usuario('Bianca', 'Schmidt', 20, 'feminino', 'Ijuí')

usuario1.saudacao()
usuario1.descricao_usuario()
usuario2.saudacao()
usuario2.descricao_usuario()
usuario3.saudacao()
usuario3.descricao_usuario()
usuario4.saudacao()
usuario4.descricao_usuario()
usuario5.saudacao()
usuario5.descricao_usuario()
usuario6.saudacao()
usuario6.descricao_usuario()
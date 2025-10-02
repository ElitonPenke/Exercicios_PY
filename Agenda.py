import json

ARQUIVO = 'contatos.json'

def carregar_contatos():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

contatos = carregar_contatos()  

class Agenda:
    def adicionar_contato():
        nome = input('NOME: ')
        telefone = input('TELEFONE: ')
        email = input('EMAIL: ')
        endereco = input('ENDEREÇO: ')
        aniversario = input('ANIVERSÁRIO: ')
        id = len(contatos) + 1
        novo = {
            'id': id,
            'nome': nome.title(),
            'telefone': telefone,
            'email': email.upper(),
            'endereco': endereco,
            'aniversario': aniversario
        }
        contatos.append(novo)
        salvar_contatos(contatos)
        print('\nCONTATO ADICIONADO COM SUCESSO!\n')

    def listar_contatos():
        for contato in contatos:
            print(f"\nID: {contato['id']}")
            print(f"NOME: {contato['nome']}")
            print(f"TELEFONE: {contato['telefone']}")
            print(f"EMAIL: {contato['email']}")
            print(f"ENDEREÇO: {contato['endereco']}")
            print(f"ANIVERSÁRIO: {contato['aniversario']}")
            print("=========================================")

    def atualizar_contato(self):
        pass
    def deletar_contato(self):
        pass


while True:
    print('\n|--------1-CADASTRAR NOVO CONTATO---------|')
    print('|--------2-LISTAR MEUS CONTATOS-----------|')
    print('|--------3-EDITAR CONTATO-----------------|')
    print('|--------4-SAIR-------------------------|\n')
    opcao=int(input('DIGITE A OPÇÃO DESEJADA: \n'))

    match opcao:
        case 1:
            Agenda.adicionar_contato()
        case 2:
            Agenda.listar_contatos()
        case 3:
            Agenda.atualizar_contato()
        case 4:
            print('SAINDO DO PROGRAMA...')
            break
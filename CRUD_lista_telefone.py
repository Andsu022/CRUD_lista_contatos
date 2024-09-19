agenda_contatos = {}

def adicionar_contato(nome, telefone):
    if nome in agenda_contatos:
        if agenda_contatos[nome] == telefone:
            print('Contato já adicionado !')
        else:
            opcao = input('O contato ja existe, gostaria de atualizar o telefone ? (s/n):')
            if opcao.lower() == 's':
                agenda_contatos[nome] = telefone
                print('Telefone atualizado !')
            else:
                print('Ok, contato não atualizado !')
    else: 
        agenda_contatos.update({nome : telefone})
        


def criar_agenda(nome, telefone):
    agenda_contatos[nome] = telefone
    print('Agenda criada com sucesso !!')



def verificar_agenda():
    if len(agenda_contatos) == 0:
        print('Agenda vazia !')
    else:
        for chave, valor in agenda_contatos.items():
            print(f'{chave} : {valor}')


def deletar_contato(nome):
    if len(agenda_contatos) == 0:
        print('Agenda vazia, nenhum contato removido !')

    else:
        if nome in agenda_contatos.keys():
            agenda_contatos.pop(nome)
            print('Contato removido com sucesso !!')
        else:
            print(f'Contato {nome} não encontrado!')

   

def main():
    
    while True:
        
        try:

            opc = int(input('\n|AGENDA DE CONTATOS\n|1 - Criar lista de contatos\n|2 - Adicionar contato\n|3 - Visualizar lista de contatos\n|4 - Deletar contato\n|5 - Sair\n|OPC ->'))

            match opc:

                case 1:
                    name = input('Digite o nome do contato: ')
                    phone = input('Digite o telefone(com DDD): ')
                    criar_agenda(nome = name, telefone = phone)
                    continue

                case 2:
                    nome_contato = input('Digite o nome do contato: ')
                    telefone_contato = input('Digite o telefone(com DDD): ')
                    adicionar_contato(nome_contato, telefone_contato)
                    continue

                case 3:
                    verificar_agenda()
                    continue
                
                case 4:
                    nome_contato = input('Digite o nome do contato: ')
                    deletar_contato(nome=nome_contato)
                    continue

                case 5:
                    print('Saindo...')
                    break

                case _:
                    print('Opção inválida !!!')
                    continue

        except:
            print('Erro')
            continue

main()
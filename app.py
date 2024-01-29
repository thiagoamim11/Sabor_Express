import os

restaurantes = [{'nome':'Luiz Lanches', 'categoria': 'Lanches', 'ativo': False},
                {'nome': 'Vicente Lanches', 'categoria': 'Lanches', 'ativo': True },  # Isso dentro das chaves é um dicionario em python
                {'nome': 'Pizzaria do Naco', 'categoria': 'Pizzaria', 'ativo': False}]


def exibir_nome_do_programa(): #funçao com o titulo
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")


def exibir_opcoes():  #funçao das opçoes
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")
    
    
def finalizar_app():   #funçao da mensagem de finalização do app
    exibir_subtitulo('''          
█▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀█   ▄▀█ █▀█ █▀█
█▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █░▀█ █▄▀ █▄█   █▄█   █▀█ █▀▀ █▀▀''')
    
    
    
    
def voltar_ao_menu_principal():  # funçao que faz o programa voltar a o menu principal
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()    

def opcao_invalida():  # funçao de opçoes invalidas
    print('Opção invalida\n')
    voltar_ao_menu_principal()
    
    
def exibir_subtitulo(texto): 
    os.system('cls')    
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():  # funçao para cadastrar restaurante
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante  {nome_do_restaurante} foi cadastrado com sucesso!")
    
    voltar_ao_menu_principal()

def listar_restaurantes(): # funçao para listar os restaurantes cadastrados
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()




    
def alternar_estado_restaurante():  # funçao para alterar o estado do restaurante , de False para True ou vice versa
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True    
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
            print('O restaurante nao foi encontrado')
    
    voltar_ao_menu_principal()
    


def escolher_opcao():   #funçao onde o usuario escolhe qual opçao deseja
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():  # funçao principal do app
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
    
if __name__ == '__main__':
    main()
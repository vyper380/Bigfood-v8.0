import datetime
import os

class Cliente:
    def __init__(self, id, nome, endereco, telefone, celular, data_cadastro):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.celular = celular
        self.data_cadastro = data_cadastro

class OrdemDeServico:
    def __init__(self, id, cliente, data_inicio, data_termino):
        self.id = id
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_termino = data_termino

class Checklist:
    def __init__(self, id, cliente, itens):
        self.id = id
        self.cliente = cliente
        self.itens = itens

clientes = []
ordens_de_servico = []
checklists = []

def adicionar_cliente():
    id = len(clientes) + 1
    nome = input("Nome do cliente: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    celular = input("Celular: ")
    data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cliente = Cliente(id, nome, endereco, telefone, celular, data_cadastro)
    clientes.append(cliente)
    salvar_dados()
    print("Cliente adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def listar_clientes():
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}, Celular: {cliente.celular}, Data de Cadastro: {cliente.data_cadastro}")
    input("Pressione Enter para continuar...")

def adicionar_ordem_de_servico():
    id = len(ordens_de_servico) + 1
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    if cliente:
        data_inicio = input("Data de início (YYYY-MM-DD): ")
        data_termino = input("Data de término (YYYY-MM-DD): ")
        ordem = OrdemDeServico(id, cliente, data_inicio, data_termino)
        ordens_de_servico.append(ordem)
        salvar_dados()
        print("Ordem de serviço adicionada com sucesso!")
    else:
        print("Cliente não encontrado!")
    input("Pressione Enter para continuar...")

def listar_ordens_de_servico():
    for ordem in ordens_de_servico:
        print(f"ID: {ordem.id}, Cliente: {ordem.cliente.nome}, Data de Início: {ordem.data_inicio}, Data de Término: {ordem.data_termino}")
        print("--------------------------------------------------")
    input("Pressione Enter para continuar...")

def adicionar_checklist():
    id = len(checklists) + 1
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    if cliente:
        itens = input("Itens do checklist (separados por vírgula): ").split(',')
        checklist = Checklist(id, cliente, itens)
        checklists.append(checklist)
        salvar_dados()
        print("Checklist adicionado com sucesso!")
    else:
        print("Cliente não encontrado!")
    input("Pressione Enter para continuar...")

def listar_checklists():
    for checklist in checklists:
        print(f"ID: {checklist.id}, Cliente: {checklist.cliente.nome}, Itens: {', '.join(checklist.itens)}")
        print("--------------------------------------------------")
    input("Pressione Enter para continuar...")

def agendar_suporte_tecnico():
    id = len(ordens_de_servico) + 1
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    if cliente:
        data_inicio = input("Data de agendamento (YYYY-MM-DD): ")
        ordem = OrdemDeServico(id, cliente, data_inicio, "Agendamento de Suporte Técnico Presencial")
        ordens_de_servico.append(ordem)
        salvar_dados()
        print("Suporte técnico agendado com sucesso!")
    else:
        print("Cliente não encontrado!")
    input("Pressione Enter para continuar...")

def imprimir_dados(dados):
    for dado in dados:
        print(dado)
    input("Pressione Enter para continuar...")

def imprimir_etiqueta():
    listar_ordens_de_servico()
    ordem_id = int(input("ID da ordem de serviço: "))
    ordem = next((o for o in ordens_de_servico if o.id == ordem_id), None)
    if ordem:
        print("--------------------------------------------------")
        print(f"Ordem de Serviço: {ordem.id}")
        print(f"Cliente: {ordem.cliente.nome}")
        print(f"Telefone: {ordem.cliente.telefone}")
        print("--------------------------------------------------")
    else:
        print("Ordem de serviço não encontrada!")
    input("Pressione Enter para continuar...")

def salvar_dados():
    with open('dados.txt', 'w') as file:
        for cliente in clientes:
            file.write(f"Cliente: {cliente.id}, {cliente.nome}, {cliente.endereco}, {cliente.telefone}, {cliente.celular}, {cliente.data_cadastro}\n")
        for ordem in ordens_de_servico:
            file.write(f"Ordem de Serviço: {ordem.id}, {ordem.cliente.nome}, {ordem.data_inicio}, {ordem.data_termino}\n")
        for checklist in checklists:
            file.write(f"Checklist: {checklist.id}, {checklist.cliente.nome}, {', '.join(checklist.itens)}\n")

def pesquisar_dados():
    termo = input("Digite o termo de pesquisa: ")
    with open('dados.txt', 'r') as file:
        for linha in file:
            if termo in linha:
                print(linha.strip())
    input("Pressione Enter para continuar...")

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------------------------------------------------")
        print("**SHAYRA INFORMATICA**")
        print("Telefone: 11-994780422 (WhatsApp)")
        print("Email: shayra.forfor.guarulhos@gmail.com")
        print("--------------------------------------------------")
        print("\nMenu:")
        print("1. Adicionar Cliente")
        print("2. Adicionar Ordem de Serviço")
        print("3. Listar Clientes")
        print("4. Listar Ordens de Serviço")
        print("5. Agendar Suporte Técnico Presencial")
        print("6. Adicionar Checklist")
        print("7. Listar Checklists")
        print("8. Imprimir Clientes")
        print("9. Imprimir Ordens de Serviço")
        print("10. Imprimir Checklists")
        print("11. Imprimir Etiqueta")
        print("12. Pesquisar Dados")
        print("13. Sair")
        print("--------------------------------------------------")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_cliente()
        elif opcao == 2:
            adicionar_ordem_de_servico()
        elif opcao == 3:
            listar_clientes()
        elif opcao == 4:
            listar_ordens_de_servico()
        elif opcao == 5:
            agendar_suporte_tecnico()
        elif opcao == 6:
            adicionar_checklist()
        elif opcao == 7:
            listar_checklists()
        elif opcao == 8:
            imprimir_dados(clientes)
        elif opcao == 9:
            imprimir_dados(ordens_de_servico)
        elif opcao == 10:
            imprimir_dados(checklists)
        elif opcao == 11:
            imprimir_etiqueta()
        elif opcao == 12:
            pesquisar_dados()
        elif opcao == 13:
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()

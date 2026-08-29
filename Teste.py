clientes = []
def encontrar_cliente(email):
    email = email.strip().lower()

    for cliente in clientes:
        if cliente["email"] == email:
            return cliente
    return None

def cadastrar_cliente():
    print("\n=== Cadastrar cliente ===")

    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip().lower()
    empresa = input("Empresa: ").strip()

    if not nome or not email or not empresa:
        print("Todos os campos são obrigatórios.")
        return
    if encontrar_cliente(email) is not None:
        print("Já existe um cliente com esse e-mail cadastrado.")
        return
    cliente = {
        "nome": nome,
        "email": email,
        "empresa": empresa,
        "status": "lead",
    }

    clientes.append(cliente)
    print(f"cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\n=== Lista de clientes ===")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for indice, cliente in enumerate(clientes, start=1):
        print(f"\ncliente #{indice}")
        print(f"Nome: {cliente['nome']}")
        print(f"E-mail: {cliente['email']}")
        print(f"Empresa: {cliente['empresa']}")
        print(f"Status: {cliente['status']}")

def buscar_cliente_por_email():
    print("\n=== Buscar cliente por e-mail ===")

    email_procurado = input("Digite o e-mail: ")
    cliente = encontrar_cliente(email_procurado)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print("\nCliente encontrado!")
    print(f"Nome: {cliente['nome']}")
    print(f"E-mail: {cliente['email']}")
    print(f"Empresa: {cliente['empresa']}")
    print(f"Status: {cliente['status']}")
    
def alterar_status():
    print("\n=== Alterar status ===")

    email_procurado = input("Digite o e-mail do cliente: ")
    cliente = encontrar_cliente(email_procurado)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print(f"Status atual: {cliente['status']}")

    novo_status = input(
        "Novo status (lead, ativo ou inativo): "
    ).strip().lower()

    status_validos = ["lead", "ativo", "inativo"]

    if novo_status not in status_validos:
        print("Status inválido.")
        return

    cliente["status"] = novo_status
    print("Status alterado com sucesso!")

def exibir_resumo():
    print("\n=== Resumo de clientes ===")

    resumo = {
        "lead": 0,
        "ativo": 0,
        "inativo": 0,
    }

    for cliente in clientes:
        status = cliente["status"]
        resumo[status] += 1

    print(f"Leads: {resumo['lead']}")
    print(f"Ativos: {resumo['ativo']}")
    print(f"Inativos: {resumo['inativo']}")
    print(f"Total: {len(clientes)}")
        
def executar_menu():
    while True:
        print("\n=== CRM Kodely ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar por e-mail")
        print("4. Alterar status")
        print("5. Exibir resumo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente_por_email()
        elif opcao == "4":
            alterar_status()
        elif opcao == "5":
            exibir_resumo()
        elif opcao == "0":
            print("CRM encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

executar_menu()
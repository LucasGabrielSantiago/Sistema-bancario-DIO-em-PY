import textwrap

#criando menu
def menu():
    menu = """\n
    ========================================

            [1]\tDepositar
            [2]\tSacar
            [3]\tExtrato
            [4]\tNova conta
            [5]\tListar contas
            [6]\tNovo usuário
            [0]\tSair

    ========================================
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Ovalor é invaido. @@@") 

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    #excedeu_saque = numero_saques >= LIMITE_SAQUES
    excedeu_saques = numero_saques >= limites_saques

    if excedeu_saldo:
        print("\n@@@ Não foi possivel realizar o saque.\nSaldo insuficiente @@@\nTente novamente")

    elif excedeu_limite:
        print("\n@@@ Não foi possivel realizar saque. @@@\nValor informado excedeu o limite")
        
    elif excedeu_saques:
        print("\n@@@ Não será possivel realizar saque.@@@\nVocê excedeu o seu limite de saques diarios\nTente novamente amanhã:")

    elif valor >0:
        saldo -= valor
        extrato += f"saque: R$ {valor:.2f}\n"
        print(f"\n=== Saque realizado com sucesso ===\nSeu saldo é: R${saldo:.2f}")
        numero_saques += 1

    else:
        print("Operção falhou.\nValor informado invalido")
    return saldo, extrato    
        
def exibir_extrato(saldo, /, *, extrato):
        print(16*"="+"Extrato"+"="*16)
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("="*40)

def  criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente númeto): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ já existe um usúario com esse CPF! @@@")
        return
    nome = input("\nInfome o nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
    endereco = input("Infome o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf =input("Infome o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuários não encontrado, fluxo de criação de conta encerrado! @@@")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor de deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Infome o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=exibir_extrato)

        elif opcao == "6":
            #criar_usuario(usuarios)
            criar_usuario(usuario)

        elif opcao == "4":
            numero_conta = len(contas) +1
            #conta = criar_conta(AGENCIA, numero_conta, usuarios)
            conta = criar_conta(AGENCIA, numero_conta, usuario)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            lista_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação invalida! Selecione a Opção desejada")

main()

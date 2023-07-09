"""
crie um sistema bancário com as operações:
sacar, depositar, e visualizar extrato
"""
"""
operação de deposito:
deve ter um contador com o numero de depositos realizados 
o valor e deposito não pode ser menor ou igual a zero
"""
"""
operação de saque :
o sistema deve permitir realizar 3 saques diarios 
maximo de R$1000,00 por saque. caso o usuario não tenha saldo 
na contonta não será possível sacar o dinheiro por falta de saldo,
Todos os saques devem ser armazenados em uma variavel e exibidos na operação extrato.
"""
"""
operação de extrato  
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim
da listagem deve ser exibido o saldo atual da conta 
os valores devem ser exibidos ultilizando o formato R$ xxx.xx,
exemplo:
1500.45 = R$1500.45
"""

#criando menu
menu = """
========================================

            [1] Depositar
            [2] Sacar
            [3] Extrato
            [0] Sair

========================================
=> """


saldo = 2500
limite = 3000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor= float(input("Operação selecionada foi Depósito:\nQual valor deseja depositar?"))
        if valor <= 0:
            print("O valor minimo de deposito deve ser superior a R$0.00\nTente novamente")
                    
        elif valor >0:
            saldo += valor 
            print(f"Deposito realizado com sucesso\nSeu saldo é: R${saldo:.2f}")

    elif opcao =="2":
        valor = float(input("Operação selecionada foi saque:\nInforme o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não foi possivel realizar o saque.\nSaldo insuficiente\nTente novamente")

        elif excedeu_limite:
            print("Não foi possivel realizar saque.\nValor informado excedeu o limite")
        
        elif excedeu_saque:
            print("Não será possivel realizar saque.\nVocê excedeu o seu limite de saques diarios\nTente novamente amanhã:")

        elif valor >0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            print(f"Saque realizado com sucesso\nSeu saldo é: R${saldo:.2f}")
            numero_saques += 1

        else:
            print("Operção falhou.\nValor informado invalido")
        


            
    elif opcao =="3":
        print(16*"="+"Extrato"+"="*16)
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("="*40)

    elif opcao =="0":
        print("***sair***")
        break

    else:
        print("Operação invalida\nTente novamente")
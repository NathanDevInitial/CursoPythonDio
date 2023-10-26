saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Lista para contas correntes
contas_correntes = []

#Numero inical para contas correntes
contador_numero_conta = 1

#Lista para usuários
usuarios = []

#Criação do usuário
def criar_usuario():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço (no formato LOGRADOURO, NRO - BAIRRO - CIDADE/ESTADO): ")

    #Conferindo se ja existe algum usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário com esse CPF.")
            return
        
    #ADD usuário criado a Lista de usuários...
    usuario.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

def criar_conta_corrente():
    usuario_cpf = input("CPF do titular da conta: ")

    #checando se o CPF informado existe.
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == usuario_cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Usuário com o CPF informado não encontrado.")
        return
    
    global contador_numero_conta 
    agencia = "0001"
    numero_conta = contador_numero_conta
    numero_conta += 1

    #Adicionando conta à lista de contas correntes
    contas_correntes.append({'agencia':agencia, 'numero_conta': numero_conta, 'usuario': usuario_encontrado})




def deposito(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido. ")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente. ")
    elif excedeu_limite:
        print("Operação falhou! O valor do saqque excedeu o limite. ")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido. ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido. ")
        return saldo, extrato 

def extrato(saldo, *, extrato):
    print("\n===================== EXTRATO =======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSando: R$ {saldo:.2f}")
    print("=======================================================")


def menu():
    return """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Abrir Conta
[q] Sair


===>>>"""

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES) 

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario()


    elif opcao == "a":
        criar_conta_corrente()

    elif opcao == "q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")





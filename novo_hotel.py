quartos = {
    'Single': {'preco': 50, 'vagas': 5, 'vagas_iniciais': 5},
    'Duplo': {'preco': 100, 'vagas': 4, 'vagas_iniciais': 4},
    'Triplo': {'preco': 150, 'vagas': 3, 'vagas_iniciais': 3},
    'Suite': {'preco': 300, 'vagas': 2, 'vagas_iniciais': 2}
}

def cadastrar_cliente():
    print("Cadastro:\n")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    print("--------------------------------------------------")
    print("Nome: ", nome, "\nTelefone: ", telefone, "\nEndereço: ", endereco)

def processar_single():
    tipo_quarto = 'Single'
    if quartos[tipo_quarto]['vagas'] > 0:
        print(quartos[tipo_quarto]['vagas'], " Vagas Disponíveis")
        cadastrar_cliente()
        dias = int(input("Dias de hospedagem: "))
        total = dias * quartos[tipo_quarto]['preco']
        print("Total à Pagar: R$", total, " Reais")
        confirmar_cadastro(quartos[tipo_quarto])
    else:
        print("Quartos Ocupados")

# Função para processar a opção Duplo
def processar_duplo():
    tipo_quarto = 'Duplo'
    if quartos[tipo_quarto]['vagas'] > 0:
        print(quartos[tipo_quarto]['vagas'], " Vagas Disponíveis")
        cadastrar_cliente()
        dias = int(input("Dias de hospedagem: "))
        total = dias * quartos[tipo_quarto]['preco']
        print("Total à Pagar: R$", total, " Reais")
        confirmar_cadastro(quartos[tipo_quarto])
    else:
        print("Quartos Ocupados")

# Função para processar a opção Triplo
def processar_triplo():
    tipo_quarto = 'Triplo'
    if quartos[tipo_quarto]['vagas'] > 0:
        print(quartos[tipo_quarto]['vagas'], " Vagas Disponíveis")
        cadastrar_cliente()
        dias = int(input("Dias de hospedagem: "))
        total = dias * quartos[tipo_quarto]['preco']
        print("Total à Pagar: R$", total, " Reais")
        confirmar_cadastro(quartos[tipo_quarto])
    else:
        print("Quartos Ocupados")

# Função para processar a opção Suite
def processar_suite():
    tipo_quarto = 'Suite'
    if quartos[tipo_quarto]['vagas'] > 0:
        print(quartos[tipo_quarto]['vagas'], " Vagas Disponíveis")
        cadastrar_cliente()
        dias = int(input("Dias de hospedagem: "))
        total = dias * quartos[tipo_quarto]['preco']
        print("Total à Pagar: R$", total, " Reais")
        confirmar_cadastro(quartos[tipo_quarto])
    else:
        print("Quartos Ocupados")

# Função para exibir os quartos disponíveis
def exibir_quartos_disponiveis():
    print("****************************************************************")
    print("********   Quartos Disponiveis:                         ********")
    print("********                                                ********")
    for tipo_quarto, info_quarto in quartos.items():
        vagas_disponiveis = info_quarto['vagas']
    print("********        {}               {}                ********".format(tipo_quarto, vagas_disponiveis))
    print("****************************************************************\n\n")

# Função para exibir o total de hóspedes
def exibir_total_hospedes():
    print("****************************************************************")
    print("********   Total de Hospedes        :                   ********")
    print("********                                                ********")
    total_hospedes = 0
    for tipo_quarto, info_quarto in quartos.items():
        vagas_ocupadas = info_quarto['vagas_iniciais'] - info_quarto['vagas']
        total_hospedes += vagas_ocupadas
    print("********        {}               {}                ********".format(tipo_quarto, vagas_ocupadas))
    print("********        Total                {}                ********".format(total_hospedes))
    print("****************************************************************\n\n")

# Função para confirmar o cadastro
def confirmar_cadastro(info_quarto):
    n = int(input("Deseja Comfirmar Cadastro? 1 - Sim  2 - Não "))
    if n == 1:
        print("Confirmado")
        info_quarto['vagas'] -= 1
    else:
        print("Cancelado")

# Função principal
def main():
    opcao = 0
    while opcao != 7:
        print("*************************** HOTEL JVR **************************")
        print("********                                                ********")
        print("********   Escolha a opção desejada:                    ********")
        print("********                                                ********")
        print("********       1 - Single              - R$ 50,00       ********")
        print("********       2 - Duplo               - R$ 100,00      ********")
        print("********       3 - Triplo              - R$ 150,00      ********")
        print("********       4 - Suíte Presidencial  - R$ 300,00      ********")
        print("********       5 - Quartos Dispoiveis                   ********")
        print("********       6 - Total de hospedes                    ********")
        print("********       7 - Processo encerrado                   ********")
        print("****************************************************************\n\n")

        opcao = int(input("Digite a opção para prosseguir: "))

        if opcao == 1:
            processar_single()
        elif opcao == 2:
            processar_duplo()
        elif opcao == 3:
            processar_triplo()
        elif opcao == 4:
            processar_suite()
        elif opcao == 5:
            exibir_quartos_disponiveis()
        elif opcao == 6:
            exibir_total_hospedes()
        elif opcao == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o programa
main()

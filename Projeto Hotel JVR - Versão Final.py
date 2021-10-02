s = 5
d = 4
t = 3
su = 2
def cadastro():

    print("Cadastro:\n ")
    nome = str(input("Nome: "))
    telefone = str(input("Telefone: "))
    endereco = str(input("Endereço: "))
    print("--------------------------------------------------")
    print("Nome: ",nome, "\nTelefone: ", telefone, "\nEndereço: ",endereco)

def single():
        print("--------------------------------------------------")
        dias = int(input("Dias de hospedagem: "))
        total = dias * 50
        print("Total à Pagar: R$",total, " Reais")
        n = int(input("Deseja Comfirmar Cadastro? 1 - Sim  2 - Não "))
        return n

def duplo():
    print("--------------------------------------------------")
    dias = int(input("Dias de hospedagem: "))
    total = dias * 100
    print("Total à Pagar: R$",total, " Reais")
    n = int(input("Deseja Comfirmar Cadastro? 1 - Sim  2 - Não "))
    return n

def triplo():
    print("--------------------------------------------------")
    dias = int(input("Dias de hospedagem: "))
    total = dias * 150
    print("Total à Pagar: R$",total, " Reais")
    n = int(input("Deseja Comfirmar Cadastro? 1 - Sim  2 - Não "))
    return n   
  
def suite():
    print("--------------------------------------------------")
    dias = int(input("Dias de hospedagem: "))
    total = dias * 300
    print("Total à Pagar: R$",total, " Reais")
    n = int(input("Deseja Confirmar Cadastro? 1 - Sim  2 - Não "))
    return n

opcao = 0
while(opcao != 7):

    print("*************************** HOTEL JVR **************************\n"
                  "********                                                ********\n"
                  "********   Escolha a opção desejada:                    ********\n"
                  "********                                                ********\n"
                  "********       1 - Single              - R$ 50,00       ********\n"
                  "********       2 - Duplo               - R$ 100,00      ********\n"
                  "********       3 - Triplo              - R$ 150,00      ********\n"
                  "********       4 - Suíte Presidencial  - R$ 300,00      ********\n"
                  "********       5 - Quartos Dispoiveis                   ********\n"
                  "********       6 - Total de hospedes                    ********\n"
                  "********       7 - Processo encerrado                   ********\n"
                  "****************************************************************\n\n")
    
 
    opcao = int(input("Digite a opção para prosseguir: "))
    
    if (opcao == 1):
        if(s > 0):
            print(s," Vagas Disponíveis")
            cadastro()
            n = single()
            if(n == 2):
                 print("Cancelado")
            else:
                print("Confirmado")
                s -= 1
        else:
            print("Quartos Ocupados")
       
    elif(opcao == 2):
         if(d > 0):
            print(d," Vagas Disponíveis")
            cadastro()
            n = duplo()
            if(n == 2):
                 print("Cancelado")
            else:
                print("Confirmado")
                d -= 1
         else:
            print("Quartos Ocupados")
       
    elif(opcao == 3):
        if(t > 0):
           print(t," Vagas Disponíveis")
           cadastro()
           n = triplo()
           if(n == 2):
               print("Cancelado")
           else:
               print("Confirmado")
               t -= 1
        else:
            print("Quartos Ocupados")

    elif(opcao == 4):
         if(su > 0):
           print(su," Vagas Disponíveis")
           cadastro()
           n = suite()
           if(n == 2):
               print("Cancelado")
           else:
               print("Confirmado")
               su -= 1
         else:
            print("Quartos Ocupados")
    elif(opcao == 5):
        print("****************************************************************\n"
                  "********   Quartos Disponiveis:                         ********\n"
                  "********                                                ********\n"
                  "********        Single               ",s,"                ********\n"
                  "********        Duplo                ",d,"                ********\n"
                  "********        Triplo               ",t,"                ********\n"
                  "********        Suite                ",su,"                ********\n"
                  "****************************************************************\n\n")



        
    elif(opcao == 6):
        print("****************************************************************\n"
                  "********   Total de Hospedes        :                   ********\n"
                  "********                                                ********\n"
                  "********        Single               ",5 - s,"                ********\n"
                  "********        Duplo                ",4 - d,"                ********\n"
                  "********        Triplo               ",3 - t,"                ********\n"
                  "********        Suite                ",2 - su,"                ********\n"
                  "********        Total                ",(5 - s)+(4 - d)+(3 - t)+(2 - su),"                ********\n"
                  "****************************************************************\n\n")
        

    else:
        print("Saindo...")
        break
        



        

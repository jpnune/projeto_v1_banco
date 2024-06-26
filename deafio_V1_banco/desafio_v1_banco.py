# ------------------> INICIO CODIGO <------------------------

# Variáveis Globais
saldo = 0
quantidade_de_operacoes = 0
extrato = f'id{" "*15} tipo de transação {" "*26} Valor\n\n'
quantidide_saque_diario_realizado = 0

# Constantes
QUANTIDADE_SAQUE_DIARIO_MAXIMO = 3
VALOR_MAXIMO_POR_SAQUE = 500


#looping do menu.
while True:
    # ----> Início bloco Menu <----
    
    # Verifica se é possivel fazer saque no dia, muda o layout do menu com ou sem opção de saque.
    if saldo ==0 or quantidide_saque_diario_realizado == QUANTIDADE_SAQUE_DIARIO_MAXIMO:

        # Menu sem opção de saque.
        print(f'{"\n"*1000}') #limpar a tela 
        print(f'{"#"*15}  MEMENU DE OPÇOES  {"#"*15}\n')
        print(f'{" "*10}Escolha uma opcão do menu abaixo\n')
        print(f'{" "*15}[ 1 ] Consultar saldo')
        print(f'{" "*15}[ 2 ] Depositar')
        print(f'{" "*15}[ 4 ] Extrato')
        print(f'{" "*15}[ 9 ] Sair')
        print()

        # Menssagem de saque diário atingido.
        if quantidide_saque_diario_realizado == QUANTIDADE_SAQUE_DIARIO_MAXIMO:
            print(f'{' '*7}Limite de saques diarios atingido!\n')
        opcao = int(input(f'{"#"*51}{"\n"*3}Digite aqui --> '))
        print(f'{"\n"*1000}') # Limpar a tela.
        if opcao == 3:
            continue
    else:
        # Menu com opção de saque.
        print(f'{"\n"*1000}') #Limpar a tela. 
        print(f'{"#"*15}  MEMENU DE OPÇOES  {"#"*15}\n')

        print(f'{" "*10}Escolha uma opcão do menu abaixo\n')
        print(f'{" "*15}[ 1 ] Consultar saldo')
        print(f'{" "*15}[ 2 ] Depositar')
        print(f'{" "*15}[ 3 ] Sacar')
        print(f'{" "*15}[ 4 ] Extrato')
        print(f'{" "*15}[ 9 ] Sair')
        print()
        opcao = int(input(f'{"#"*51}{"\n"*3}Digite aqui --> '))
        print(f'{"\n"*1000}') # Limpar a tela.
    # ----> FIM bloco Menu <----
        
    # ----> Início bloco Saldo <----
    # Refere-se a opção 1 do Menu.
    if opcao == 1: 
        print(f'Saldo disponivel: R${saldo:.2f}\n')

        # Verifica alguns possíveis erros do usuário forçando-o a escolher a opção correta.
        while True: 
            print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ') 
            voltar_menu = input('digite uma das opções acima: ') 
            print(f'{"\n"*1000}') #limpar a tela   

            # Sai do menu de opções caso seja digitado 0 ou 9.
            if voltar_menu == '0' or voltar_menu == '9':
                break
            else:
                print('Opção invalida!\nDigite: 0 para voltar ao menu principal ou 9 para encerrar o atendimento!\n')
    # ----Fim bloco Saldo <----

    # ----> Início bloco Depósito <----        
    # Refere-se a opção 2 do Menu.
    elif opcao == 2: 

        # Cria um submenu de depósito caso usuário queira continuar fazendo depósitos consecutivos.
        while True:
            deposito = input('digite o valor do depósito: ')
            print(f'{"\n"*1000}') # Limpar a tela. 
            
            # Formata a casa decimal do número inserido no input "deposito".
            if deposito ==".":
                deposito = "0.00"
            elif (len(deposito) - (str.find(deposito,'.')+1) < 2) or (str.find(deposito,'.') == -1): 
                deposito = f'{float(deposito)}0'
            else:
                deposito = deposito[:str.find(deposito,'.')+3]
            
            # Verifica se o depósito é um valor positivo (maior que 0).
            if float(deposito) > 0:
                saldo += float(deposito) # Adiciona o valor do deposito no saldo.
                quantidade_de_operacoes += 1 # Soma 1 ao contador "quantidade de operações" para ser usado no extrato.
                extrato += f'{quantidade_de_operacoes}{" "*(20 - len(str(quantidade_de_operacoes)))}  Depósito {" "*(34-len(deposito))} R${deposito}\n' # Formata e adiciona item no extrato.
                print(f'Depósito efetuado com sucesso! {"\n"*5}')
            else:
                print('O depósito tem que ser um valor maior que R$ 0.00\n')

            # Verifica alguns possíveis erros do usuário forçando-o a escolher a opção correta.
            while True:
                print('[ 0 ] Voltar ao menu principal\n[ 1 ] Fazer um novo depósito\n[ 9 ] Sair\n')
                voltar_menu = input( 'digite uma das opções acima: ')
                print(f'{"\n"*1000}') # Limpar a tela.      
                if voltar_menu == '0' or voltar_menu == '1' or voltar_menu == '9':
                    break
                else:
                    print('Opção incorreta, digite 0, 1 ou 9 conforme as opções apresentada!\n')
            if voltar_menu == '0' or voltar_menu == '9' :
                break
    # ----> Fim bloco Depósito <----

    # ----> Inicio bloco Saque <----     
    # Refere-se a opção 3 do Menu
    elif opcao == 3: 

        # Cria um submenu de saque caso usuário queira continuar fazendo saques consecutivos.
        while True:

            # Verifica o saldo para saber se é possível fazer saque.
            if saldo == 0:
                print(f'Saldo insuficiente!\n')
            else:
                print(f'Saldo: R${saldo :.2f}\n')
                saque = input('Digite o valor de saque desejado: ')

                # Formata a casa decimal do número inserido no input "saque".
                if saque ==".":
                    saque = "0.00"
                elif (len(saque) - (str.find(saque,'.')+1) < 2) or (str.find(saque,'.') == -1): 
                    saque = f'{float(saque)}0'
                else:
                    saque = saque[:str.find(saque,'.')+3]

                flt_saque = float(saque)
                print(f'{"\n"*1000}') # Limpar a tela.  

                # Verifica se o numero digitado é positivo.
                if flt_saque <= 0:
                    print('Valor de saque deve ser maior que R$ 0.00\n')
                else:

                    #  Verifica se o valor é menor que a restrição de valor máximo por dia.
                    if flt_saque <= VALOR_MAXIMO_POR_SAQUE:

                        # Verifica se valor do saldo é maior que valor do saque.
                        if flt_saque <= saldo:

                            # Confirmação e execução do valor do saque.
                            while True:
                                print(f'O valor de R$ {saque} será descontado da conta, confirma?\n[ 0 ] NÃO\n[ 1 ] SIM\n')
                                confirmacao = input('digite uma das opções acima: ')
                                print(f'{"\n"*1000}') # Limpar a tela. 
                                if confirmacao == '1':
                                    saldo -= flt_saque # Retira o valor do saldo.
                                    quantidade_de_operacoes += 1 # Soma 1 ao contador "quantidade de operações" para ser usado no extrato.
                                    extrato += f'{quantidade_de_operacoes}{" "*(20 - len(str(quantidade_de_operacoes)))}  Saque {" "*(37-len(saque))} R${saque}\n' # Formata e adiciona item no extrato.
                                    quantidide_saque_diario_realizado +=1 # Soma em 1 na contagem de saques diários.
                                    print(f'Saque de R$ {saque} efetuado com sucesso!\n')
                                    print(f'Saldo atual é de R${saldo}\n\n')
                                    break
                                elif confirmacao == '0':
                                    print('Saque CANCELADO!\n')
                                    break
                                else:
                                    print('Opção incorreta, digite 0 para cancelar o saque ou 1 para confirmar o saque.\n')
                        else:
                            print('Saldo insuficiente!\n')
                    else:
                        print(f'Valor superior ao limite por saque permitido!\n') 
            
            # Cria um looping do submenu de saque.   
            while True: 

                # Verifica se atingiu a quantidade de saque diário e retira a opção de saque quando atingido.
                if quantidide_saque_diario_realizado >= QUANTIDADE_SAQUE_DIARIO_MAXIMO:
                    print('Limite de saques diários atingido!\n')

                    # Verifica alguns possíveis erros do usuário forçando-o a escolher a opção correta .
                    while True:  
                        print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ')
                        voltar_menu = input('Digite uma das opções acima: ')
                        print(f'{"\n"*1000}') # Limpar a tela.     
                        if voltar_menu == '0' or voltar_menu == '9':
                            break
                        else:
                            print('Opção invalida!\nDigite: 0 para voltar ao menu principal ou 9 para encerrar o atendimento!\n')
                    if voltar_menu == '9' or voltar_menu == '0':
                        break 
                print('[ 0 ] Voltar ao menu principal\n[ 1 ] Escolher novo valor de saque\n[ 9 ] Sair\n ')
                voltar_menu = input('Digite uma das opções acima: ')
                print(f'{"\n"*1000}') # Limpar a tela.     
                if voltar_menu == '0' or voltar_menu == '1' or voltar_menu == '9':
                    break
                else:
                    print('Opção invalida!\nDigite: 0 - para voltar ao menu principal, 1 para escolher um novo valor ou 9 para encerrar o atendimento!\n')
            if voltar_menu == '9' or voltar_menu == '0':
                break
    # ----> Fim bloco Saque <----

    # ----> Inicio bloco Extrato <----            
    # Refere-se a opção 4 do Menu.
    elif opcao == 4:
        
        # Verifica alguns possíveis erros do usuário forçando-o a escolher a opção correta.
        while True:  
            if quantidade_de_operacoes == 0 :
                print('Não foram realizadas movimentações!\n')
            else:
                print(extrato)
            print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ')
            voltar_menu = input('Digite uma das opções acima: ')
            print(f'{"\n"*1000}') # Limpar a tela.     
            if voltar_menu == '0' or voltar_menu == '9':
                break
    # ----> Fim bloco Extrato <----
    
    # ----> Início bloco Sair <----
    # # Refere-se a opção 9 do Menu, finaliza o looping do menu e encerra o código. 
    if opcao == 9 or voltar_menu == '9':
        print(f'Obrigado pela preferência e volte sempre!{"\n"*5}')
        break
    # ----> Fim bloco Sair <----

# ------------------> FIM CÓDIGO <-------------------------------
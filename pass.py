# Criamos uma lista de listas chamada 'assentos' para representar as fileiras e assentos do avião.
# Cada posição na lista armazenará o status do assento (livre ou ocupado) e a classe do assento.

# Inicializando os assentos
assentos = []

# Primeira classe: fileiras 1 a 6
for fileira in range(1, 7):
    linha = []
    for letra in ['A', 'B', 'C', 'D', 'E', 'F']:
        linha.append([f"{fileira}{letra}", "Primeira Classe", 100.0, False])  # Assento, Classe, Preço, Ocupado
    assentos.append(linha)

# Classe normal: fileiras 7 a 30
for fileira in range(7, 31):
    linha = []
    for letra in ['A', 'B', 'C', 'D', 'E', 'F']:
        linha.append([f"{fileira}{letra}", "Classe Normal", 80.0, False])  # Assento, Classe, Preço, Ocupado
    assentos.append(linha)

# Função para exibir o mapa de assentos. Mostra se os assentos estão ocupados (X) ou disponíveis.
def exibir_assentos():
    print("\n=== Mapa de Assentos ===")
    print("Primeira Classe (R$ 100,00):")

    # Exibe os assentos da primeira classe
    for i in range(6):  # Primeiras 6 fileiras são de primeira classe
        linha = ""
        for assento in assentos[i]:
            if assento[3]:  # Verifica se está ocupado
                linha += "[X] "  # Assento ocupado
            else:
                linha += f"[{assento[0]}] "  # Assento disponível
        print(linha)

    print("\nClasse Normal (R$ 80,00):")

    # Exibe os assentos da classe normal
    for i in range(6, len(assentos)):  # Da fileira 7 em diante é classe normal
        linha = ""
        for assento in assentos[i]:
            if assento[3]:  # Verifica se está ocupado
                linha += "[X] "  # Assento ocupado
            else:
                linha += f"[{assento[0]}] "  # Assento disponível
        print(linha)

# Função para marcar um assento para um passageiro.
def marcar_assento():
    exibir_assentos()  # Mostra os assentos disponíveis e ocupados
    escolha = input("\nEscolha o assento desejado (ex: 1A): ").upper()

    # Percorre todas as fileiras e assentos para localizar a escolha do usuário
    for i in range(len(assentos)):
        for assento in assentos[i]:
            if assento[0] == escolha:
                if not assento[3]:  # Verifica se o assento está livre
                    nome = input("Informe o nome do passageiro: ")
                    assento[3] = True  # Marca o assento como ocupado
                    print(f"Assento {escolha} foi marcado para {nome}.")
                    print(f"Classe: {assento[1]}, Preço: R$ {assento[2]:.2f}")
                    return  # Sai da função após marcar o assento
                else:
                    print("Assento já está ocupado. Escolha outro.")
                    return
    print("Assento inválido.")  # Se o assento não for encontrado

# Função para desmarcar um assento.
def desmarcar_assento():
    exibir_assentos()  # Mostra o mapa de assentos
    escolha = input("\nEscolha o assento que deseja desmarcar (ex: 1A): ").upper()

    # Percorre todas as fileiras e assentos para localizar a escolha do usuário
    for i in range(len(assentos)):
        for assento in assentos[i]:
            if assento[0] == escolha:
                if assento[3]:  # Verifica se o assento está ocupado
                    print(f"Assento {escolha} foi desmarcado.")
                    assento[3] = False  # Libera o assento
                    return
                else:
                    print("Assento já está livre.")
                    return
    print("Assento inválido.")  # Se o assento não for encontrado

# Função para remarcar um assento.
def remarcar_assento():
    exibir_assentos()  # Mostra o mapa de assentos
    antigo_assento = input("\nEscolha o assento atual do passageiro (ex: 1A): ").upper()

    # Localiza o antigo assento
    for i in range(len(assentos)):
        for assento in assentos[i]:
            if assento[0] == antigo_assento:
                if assento[3]:  # Verifica se o assento está ocupado
                    print(f"Remarcando assento para o passageiro do assento {antigo_assento}.")
                    novo_assento = input("Escolha o novo assento (ex: 2B): ").upper()

                    # Localiza o novo assento
                    for j in range(len(assentos)):
                        for novo in assentos[j]:
                            if novo[0] == novo_assento:
                                if not novo[3]:  # Verifica se o novo assento está livre
                                    assento[3] = False  # Libera o antigo assento
                                    novo[3] = True  # Ocupa o novo assento
                                    print(f"Assento {novo_assento} foi marcado.")
                                    return
                                else:
                                    print("Novo assento já está ocupado.")
                                    return
                    print("Novo assento inválido.")
                    return
                else:
                    print("Assento original não está ocupado.")
                    return
    print("Assento original inválido.")  # Se o assento antigo não for encontrado

# Função para imprimir relatórios detalhados sobre os assentos.
def imprimir_relatorio():
    ocupados = 0
    total_pago = 0
    ocupados_primeira_classe = 0
    ocupados_classe_normal = 0
    total_pago_primeira_classe = 0
    total_pago_classe_normal = 0

    # Percorre todos os assentos para calcular os relatórios
    for i in range(len(assentos)):
        for assento in assentos[i]:
            if assento[3]:  # Se o assento estiver ocupado
                ocupados += 1
                total_pago += assento[2]
                if assento[1] == "Primeira Classe":
                    ocupados_primeira_classe += 1
                    total_pago_primeira_classe += assento[2]
                else:
                    ocupados_classe_normal += 1
                    total_pago_classe_normal += assento[2]

    print("\n=== Relatório de Assentos ===")
    print(f"Quantidade de assentos ocupados: {ocupados}")
    print(f"Quantidade de assentos vazios: {180 - ocupados}")
    print(f"Quantidade de assentos ocupados na Primeira Classe: {ocupados_primeira_classe}")
    print(f"Quantidade de assentos ocupados na Classe Normal: {ocupados_classe_normal}")
    print(f"Total pago pelos passageiros da Primeira Classe: R$ {total_pago_primeira_classe:.2f}")
    print(f"Total pago pelos passageiros da Classe Normal: R$ {total_pago_classe_normal:.2f}")
    print(f"Total geral pago: R$ {total_pago:.2f}")

# Função para exibir o menu principal e receber as escolhas do usuário.
def menu():
    while True:
        print("1. Exibir mapa de assentos")
        print("2. Marcar assento")
        print("3. Desmarcar assento")
        print("4. Remarcar assento")
        print("5. Imprimir relatório")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        # Verifica a escolha do usuário e chama a função correspondente
        if escolha == '1':
            exibir_assentos()
        elif escolha == '2':
            marcar_assento()
        elif escolha == '3':
            desmarcar_assento()
        elif escolha == '4':
            remarcar_assento()
        elif escolha == '5':
            imprimir_relatorio()
        elif escolha == '6':
            print("Saindo do sistema. Até logo!")
            break  # Encerra o loop, saindo do programa
        else:
            print("Opção inválida, tente novamente.")  # Avisa se a opção for inválida

# Inicia o programa chamando o menu
menu()
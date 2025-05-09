
while True:
    print("\n--- Menu de Análise ---")
    print("1 - Analisar Brix e pH")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            # Análise de Brix
            brix = float(input("Digite o valor de Brix: "))

            if 22.9 <= brix <= 24.2:
                print("Brix: Perfeito")
            elif 24.3 <= brix <= 26.7:
                print("Brix: Bom")
            elif 26.8 <= brix <= 28.2:
                print("Brix: Médio")
            elif 28.3 <= brix <= 29.9:
                print("Brix: Ruim")
            else:
                print("Brix: Fora de análise")

            # Análise de pH
            ph = float(input("Digite o valor de pH: "))

            if 12.9 <= ph <= 14.3:
                print("pH: Perfeito")
            elif 14.4 <= ph <= 16.9:
                print("pH: Bom")
            elif 17.0 <= ph <= 19.2:
                print("pH: Médio")
            elif 19.3 <= ph <= 21.3:
                print("pH: Ruim")
            else:
                print("pH: Fora de análise")

        case "2":
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida. Tente novamente.")

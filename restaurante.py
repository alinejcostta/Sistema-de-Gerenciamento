restaurante = []

while True:
    print(f"""
    
    -------- Cadastro de Restaurante ---------
          
        1. Cadastrar Cardápio
        2. Visualizar Cardápio
        3. Visualizar Cardápio com Detalhes
        4. Prato Mais Barato e Prato Mais Caro
          
        0. Sair


""")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Cadastrar Cardápio")
        nome_prato = input("Digite o nome do prato: ")
        categoria = input("Digite a categoria: ")
        preco = float(input("Digite o preço: "))
        tempo_preparo = float(input("Digite o tempo de preparo: "))
        descricao = input("Digite a descrição: ")

        novo_rest = {
            "Nome do Prato": nome_prato,
            "Categoria": categoria,
            "Preço": preco,
            "Tempo de Preparo": tempo_preparo,
            "Descrição": descricao
        }

        restaurante.append(novo_rest)

    elif opcao == "2":
        print("Visualizar Cardápio")
        contador = 1
        for prato in restaurante:
            print(f"{contador}. {prato["Nome do Prato"]} R$ {prato["Preço"]:,.2f}")
            contador += 1

    elif opcao == "3":
        print("Visualizar Cardápio")
        contador = 1
        for prato in restaurante:
            print(f"{contador}. {prato["Nome do Prato"]} R$ {prato["Preço"]:.2f}")
            contador += 1
        
        detalhe = int(input("Digite o número do prato desejado: "))

        detalhe_novo = restaurante[detalhe-1]
        
        print(f"""
              
        ---- DETALHES DO PRATO ----
              
        Nome do Prato: {detalhe_novo["Nome do Prato"]}
        Categoria: {detalhe_novo["Categoria"]}
        Preço: {detalhe_novo["Preço"]:,.2f}
        Tempo de Preparo: {detalhe_novo["Tempo de Preparo"]} minutos
        Descrição: {detalhe_novo["Descrição"]}

""")

        prato_caro = 0
        prato_barato = float("inf")
        nome_prato_caro = ""
        nome_prato_barato = ""

    elif opcao == "4":
        
        for p in restaurante:
            if p["Preço"] > prato_caro:
                prato_caro = p["Preço"]
                nome_prato_caro = p["Nome do Prato"]
            if p["Preço"] < prato_barato:
                prato_barato = p["Preço"]
                nome_prato_barato = p["Nome do Prato"]

        print(f"O prato mais barato é {nome_prato_barato} ({prato_barato:,.2f}) e o mais caro é {nome_prato_caro} ({prato_caro:,.2f})")


    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")
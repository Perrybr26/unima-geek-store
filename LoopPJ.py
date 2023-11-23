def remover_produto_por_nome(sacola, nome_produto):
    for produto in sacola:
        if produto._nome == nome_produto:
            sacola.remove(produto)
            return True
    return False

def compras():
    sacola = []
    compras_total = []

    while True:
        print("""Escolha o que deseja fazer:
        1) Adicionar produto
        2) Remover produto
        3) Finalizar compras
        """)
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            print("Produtos disponíveis: ")
            print("Quadrinhos")
            print("Canecas")
            print("Camisas")
            opcao_produto = input("Digite o nome do produto: ").strip().upper()
            valor = float(input("Digite o preço do produto: "))

            if opcao_produto == "QUADRINHOS":
                autor = input("Autor do quadrinho: ")
                editora = input("Editora do quadrinho: ")
                produto = Quadrinho(valor, autor, editora)

            elif opcao_produto == "CAMISAS":
                tamanho = input("P,M e G: ")
                produto = Camisa(valor, tamanho)

            elif opcao_produto == "CANECAS":
                capacidade = float(input("Capacidade da caneca: "))
                material = input("Material da caneca: ")
                produto = Caneca(valor, capacidade, material)

            else:
                print("Produto não existe!")
                continue

            quantidade = int(input("Informe a quantidade desejada: "))
            compras_total.extend([produto] * quantidade)
            print(f"{quantidade} {opcao_produto}(s) adicionado(s) ao carrinho.")

        elif opcao == 2:
            if compras_total == []:
                print("Não há nenhum produto na sacola")
            else:
                print("Produtos na sacola:")
                for i, produto in enumerate(compras_total, start=1):
                    print(f"{i} - {produto._nome}")

                nome_produto_remover = input("Informe o nome do produto a ser removido: ").strip()
                if remover_produto_por_nome(compras_total, nome_produto_remover):
                    print(f"Produto '{nome_produto_remover}' removido da sacola.")
                else:
                    print(f"Produto '{nome_produto_remover}' não encontrado na sacola.")

        elif opcao == 3:
            if compras_total == []:
                print("Nenhuma compra realizada!")
            else:
                print("Produtos na sacola:")
                for i, produto in enumerate(compras_total, start=1):
                    print(f"{i} - {produto._nome}")

            break

        else:
            print("Opção Inválida")

compras()
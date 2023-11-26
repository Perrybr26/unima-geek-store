import random


class Produto:
    def __init__(self, nome, valor, serial):
        self._nome = nome
        self._valor = valor
        self.generate_serial(serial)

    def generate_serial(self, base):
        key = random.randint(100000, 199999)
        self._serial = key * base


class Quadrinho(Produto):
    def __init__(self, valor, autor, editora):
        super().__init__('Quadrinho', valor, 7)
        self._autor = autor
        self._editora = editora


class Caneca(Produto):
    def __init__(self, valor, capacidade):
        super().__init__('Caneca', valor, 5)
        self._capacidade = capacidade


class Camisa(Produto):
    def __init__(self, valor, tamanho):
        super().__init__('Camisa', valor, 3)
        self._tamanho = tamanho


def remover_produto_por_serial(sacola, serial_produto):
    for produto in sacola:
        if produto._serial == serial_produto:
            sacola.remove(produto)
            return True
    return False


def tratar_entrada_negativa(mensagem):
    entrada = float(input(mensagem))
    if entrada <= 0:
        print("Entrada inválida")
        entrada = tratar_entrada_negativa(mensagem)
    return entrada


def tratar_tamanho_invalido():
    tamanho = input("P,M ou G? ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido")
        tamanho = tratar_tamanho_invalido()
    return tamanho


def tratar_quantidade_invalida():
    quantidade = int(input("Informe a quantidade desejada: "))
    if quantidade < 0:
        print("Quantidade inválida")
        quantidade = tratar_quantidade_invalida()
    return quantidade

# Programa em si
sacola = []
compras_total = []

while True:
    try:
        print("""Escolha o que deseja fazer:
        1) Adicionar produto
        2) Remover produto
        3) Finalizar compras
        """)
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            print("Produtos disponíveis: ")
            print("1) Quadrinhos")
            print("2) Camisas")
            print("3) Canecas")
            opcao_produto = int(input("Digite o código do produto: "))
            valor = tratar_entrada_negativa("Digite o preço do produto: ")
            quantidade = tratar_quantidade_invalida()

            if opcao_produto == 1:
                autor = input("Autor do quadrinho: ")
                editora = input("Editora do quadrinho: ")
                for i in range(quantidade):
                    produto = Quadrinho(valor, autor, editora)
                    compras_total.extend([produto])

                opcao_produto = "QUADRINHO"

            elif opcao_produto == 2:
                tamanho = tratar_tamanho_invalido()
                for i in range(quantidade):
                    produto = Camisa(valor, tamanho)
                    compras_total.extend([produto])

                opcao_produto = "CAMISA"

            elif opcao_produto == 3:
                capacidade = tratar_entrada_negativa("Capacidade da caneca (litros): ")
                for i in range(quantidade):
                    produto = Caneca(valor, capacidade)
                    compras_total.extend([produto])

                opcao_produto = "CANECA"

            else:
                print("Produto não existe!")
                continue

            print(f"{quantidade} {opcao_produto}(s) adicionado(s) ao carrinho.")

        elif opcao == 2:
            if compras_total == []:
                print("Não há nenhum produto na sacola")
            else:
                print("Produtos na sacola:")
                for i, produto in enumerate(compras_total, start=1):
                    print(f"{i}) {produto._serial} - {produto._nome} ... {produto._valor}")

                serial_produto_remover = int(input("Informe o número de série do produto a ser removido: ").strip())
                if remover_produto_por_serial(compras_total, serial_produto_remover):
                    print(f"Produto de código: '{serial_produto_remover}' removido da sacola.")
                else:
                    print(f"Produto de código: '{serial_produto_remover}' não encontrado na sacola.")

        elif opcao == 3:
            if compras_total == []:
                print("Nenhuma compra realizada!")
            else:
                valor_total = 0
                print("Produtos na sacola:")
                for i, produto in enumerate(compras_total, start=1):
                    print(f"{i}) {produto._serial} - {produto._nome} ... {produto._valor}")
                    valor_total += produto._valor

                print(f"Valor total: {valor_total}")

            break

        else:
            print("Opção Inválida")
    except ValueError:
        print("Entrada inválida")

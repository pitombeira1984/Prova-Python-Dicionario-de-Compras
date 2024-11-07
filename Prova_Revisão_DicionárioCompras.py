
def DicionarioCompras():
    produtos = {}

    for i in range(5):
        while True:
            try:
                produto_id = int(input(f"Digite o ID do produto {i+1}: "))
            
                if produto_id in produtos:
                    print("ID já existente. Por favor, insira um ID único.")
                    continue
                break
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")

        nome = input(f"Digite o nome do produto {i+1}: ")
    
        while True:
            try:
                preco = float(input(f"Digite o preço do produto {nome}: R$ "))
                break  
            except ValueError:
                print("Preço inválido. Por favor, insira um valor numérico.")

    
        produtos[produto_id] = {"nome": nome, "preco": preco}


    total = sum(produto["preco"] for produto in produtos.values())


    print("\nProdutos inseridos:")
    for produto_id, dados in produtos.items():
        print(f"ID: {produto_id}, Nome: {dados['nome']}, Preço: R$ {dados['preco']:.2f}")

    print(f"\nO valor total da compra é: R$ {total:.2f}")

DicionarioCompras()

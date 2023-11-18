class Cardapio:
    def __init__(self):
        self.itens = []
        self.precos = []

    def mostrar_itens(self):
        print(f"MENU ")
        for x in range(len(self.itens)):
            print(f"N {x+1}: {self.itens[x].ljust(45,'.')} {self.precos[x]}")

    def adicionar_lista(self,item,preco):
        self.itens.append(item)
        self.precos.append(preco)

    def remover_iten(self,item):
        del self.itens[item - 1]
        del self.precos[item - 1]
    
    def auto_itens(self):
        adicionar = self.itens.append
        adicionar_preco = self.precos.append
        adicionar("Batata Frita")
        adicionar_preco(20.0)
        adicionar("Bacon")
        adicionar_preco(15.00)
        adicionar("Coca Cola")
        adicionar_preco(5.00)
    
        
class Pedido:
    def __init__(self):
        self.itens = []
        self.precos = []
        self.total = 0
    
    def mostra_itens(self):
        for x in range(len(self.itens)):
            print(f"({x + 1})Item: {self.itens[x]} Preço: {self.precos[x]}")

    def adicionar_item(self,item,preco):
        self.itens.append(item)
        self.precos.append(preco)
    
    def remover_item(self,item):
        del self.itens[item - 1]
        del self.precos[item - 1]
    
    def finalizar_pedido(self):
        print(f"""Você pediu {self.itens}.
        """)
        total = 0
        for x in range(self.precos):
            total + self.precos[x]  
        
        print(f"O seu pedido deu {total}")

    def soma_total(self):
        for x in range(len(self.precos)):
            self.total = self.total + self.precos[x]
        return self.total

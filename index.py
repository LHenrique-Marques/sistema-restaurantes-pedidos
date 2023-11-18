from collections import namedtuple
from classes import *

def mostra_adm_menu():
            return ("""
            Olá Administrador, o que deseja fazer? 

            1- Adicionar itens a lista.
            2- Remover itens da lista
            3- Mostrar o menu
            4- Voltar ao login

        """)


cardapio = Cardapio()
pedido = Pedido()
cardapio.auto_itens()

login = namedtuple('Login_senha', ['login','senha'])
administradores = [login("henrique","1234"),login("bruno","456")]
while True:
    quest = input("Digite seu nome:")
    senha = input("Digite sua senha:")
    if login(quest,senha) in administradores:
        print(mostra_adm_menu())
        while True:
            try:
                user_escolha = int(input("Escolha o número da sua opção:   "))
            except:
                input("ERRO.Digite um número correspondente as opções....")
            
            if user_escolha == 1:
                cardapio.adicionar_lista(input("Nome do Item:  "), float(input("Preço do item:  ")))
                print(mostra_adm_menu())

            if user_escolha == 2:
                cardapio.mostrar_itens()
                cardapio.remover_iten(int(input("Digite o Número do item que deseja remover:  ")))
                print(mostra_adm_menu())
            if user_escolha == 3:
                cardapio.mostrar_itens()
                print(mostra_adm_menu())
            if user_escolha == 4:
                break


    else:
        print(f"Olá {quest}, estes são os itens do meu cardápio")
        cardapio.mostrar_itens()
        while True:
            pergunta = int(input(f"""
            Olá {quest}, o que deseja fazer?
            0 - Retornar ao login
            1 - adicionar item no pedido
            2 - remover item do pedido
            3 - finalizar pedido

            
            
            """))

            if pergunta == 1:
                cardapio.mostrar_itens()
                indice = int(input("Digite o indice do pedido que você deseja adicionar: "))
                qt = int(input("Digite quantos você deseja: "))
                for x in range(qt):
                    pedido.adicionar_item(cardapio.itens[indice - 1],cardapio.precos[indice - 1])
                    print("Produto adicionado com sucesso...")

            elif pergunta == 2:
                pedido.mostra_itens()
                indice2 = int(input("Digite o indice do produto que você deseja remover: "))
                pedido.remover_item(indice2)
                print("Produto removido com sucesso....")


            elif pergunta == 3:
                print(f"""Seu pedido foi: 
                {pedido.mostra_itens()}""")
                pedido.soma_total()
                print(pedido.total)
                perg = input("Finalizar comanda? s/n : ")
                if perg == "s":
                    print("Comanda finalizada....")
                    pedido.total = 0
                    pedido.itens = []
                    pedido.precos = []
                elif perg == "n":
                    print("Comanda em aberto....")
                    pedido.total = 0

            elif pergunta == 0:
                break



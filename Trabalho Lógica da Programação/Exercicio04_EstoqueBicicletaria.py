#Apresentando meu código identificador e meu nome
print("\nCódigo Identificador: 4500068\nAluna: Francisca Ívyne Ripardo de Sousa\n\nExercicio 4 \n")

#Empresa de Logística
print("Bem-vindo ao Estoque da Bicicletaria da Ívyne Ripardo")

#Variavel Global
estoque_peca = []
codigo_peca = 0


#Função de Cadastro
def cadastrarPeca(codigo):
  print("-"*28,"CADASTRO","-"*28)
  print("O código do produto: {}".format(codigo))
  nome_peca = input("Digite o nome da peça: ")
  fabricante = input("Digite o fabricante da peça: ")
  valor_peca = float(input("Digite o valor da peça(R$): \n"))
  #Dicionário das peças
  dicionario_peca = {"Código": codigo,
                     "Nome": nome_peca,
                     "Fabricante:": fabricante,
                     "Preço": valor_peca,}
  print("Peça Cadastrada com Sucesso...\n")
  #Incluindo uma cópia do dicionário na lista global
  estoque_peca.append(dicionario_peca.copy())


#Função de Consulta
def consultarPeca():
  #Criando um loop para caso a opção seja inválida
  while True:
    #try e except para verificar se a opcao é um número
      print("-"*28,"CONSULTA DE PEÇA","-"*28,"\n")
      print("1 - Consultar Todas as Peças ")
      print("2 - Consultar Produto por Código")
      print("3 - Consultar Produto por Fabricante")
      print("4 - Retornar à Tela de Menu")
      opcao = int(input("Digite a opção que deseja: "))

      if (opcao == 1):
        print("-"*28,"TODOS OS PRODUTOS","-"*28,"\n")
        for peca in estoque_peca: #a variável peca vai varrer toda a lista de estoque
          print("-"*20)
          for key,value in peca.items(): #varrer a lista com a chave e seu valor
            print("{} : {}".format(key,value))
          print("-"*20)

      elif (opcao == 2):
        print("-"*28,"CONSULTA POR CÓDIGO","-"*28,"\n")
        cod = int(input("Entre com o Código desejado: ")) #Pede o número do código
        for peca in estoque_peca: #a variável peca vai varrer toda a lista de estoque
          if peca["Código"] == cod: #Verifica se o Código está na lista
            print("-"*20)
            for key, value in peca.items(): #varrer a lista com a chave e seu valor
              print("{} : {}".format(key,value))
            print("-"*20)

      elif (opcao == 3):
        print("-"*28,"CONSULTA POR FABRICANTE","-"*28,"\n")
        cod = int(input("Entre com o Fabricante: "))
        for peca in estoque_peca: #a variável peca vai varrer toda a lista de estoque
          if peca["Fabricante"] == cod: #Verifica se o Código está na lista
            print("-"*20)
            for key, value in peca.items(): #varrer a lista com a chave e seu valor
              print("{} : {}".format(key,value))
            print("-"*20)

      elif (opcao == 4):
        print("\nRetornando em 3...")
        print("2...")
        print("1...\n")
        return #Sai da função consultarPeca() e volta para o main
        
      else: #Caso o valor não seja nenhuma das alternativas, ele retorna ao começo da função
        print("\nERRO, VALOR INVÁLIDO")
        print("Digite um número das opções!!!\n")
        continue


#Função de Remover 
def removerPeca():
    print("-"*28,"EXCLUIR PRODUTOS","-"*28,"\n")
    cod = int(input("Entre com o código da peça que deseja remover: "))
    for peca in estoque_peca:
      if peca["Código"] == cod:
        estoque_peca.remove(peca)
        print("Produto Removido!!!")

#                     MAIN

#                     MENU

#Criando um loop para caso a opção seja inválida
while True:
  #try e except para verificar se a opcao é um número
  try:
    print("-"*28,"MENU","-"*28,"\n")
    print("1 - Cadastrar Peça")  
    print("2 - Consultar Peça")
    print("3 - Remover Peça")
    print("4 - sair\n")  
    opcao = int(input("Digite a opção que deseja: "))


    if (opcao == 1):
      codigo_peca = codigo_peca + 1
      cadastrarPeca(codigo_peca)
    elif (opcao == 2):
      consultarPeca()
    elif (opcao == 3):
      removerPeca()
    elif (opcao == 4):
      print("\nEncerrando o sistema em 3..")
      print("2...")
      print("1...")
      print("Encerrado")
      break
    else:
      print("\nERRO, VALOR INVÁLIDO")
      print("Digite um número das opções!!!\n")
      continue #Volta para o inicio do Menu
  except ValueError:
    print("\nERRO, VALOR INVÁLIDO")
    print("Digite um número das opções!!!\n")
    continue #Volta para o inicio do Menu

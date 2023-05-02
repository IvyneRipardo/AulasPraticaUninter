#Apresentando meu código identificador e meu nome
id = ("\nCódigo Identificador: 4500068\nAluna: Francisca Ívyne Ripardo de Sousa\n\nExercicio 2 ")
print(id)

#Empresa X
print("\nBem-vindo a Lanchonete Ívyne Ripardo\n")

#Menu

def menu():
  print("\n----------------Cardápio--------------------")
  print("Código |        Descrição      | Valor(R$")
  print("   100 |     Cachorro-Quente   | 9,00")
  print("   101 | Cachorro-Quente Duplo | 11,00")
  print("   102 |         X-Egg         | 12,00")
  print("   103 |         X-Salada      | 13,00")
  print("   104 |         X-Bacon       | 14,00")
  print("   105 |         X-Tudo        | 17,00")
  print("   200 |   Refrigerante Lata   | 5,00")
  print("   201 |       Chá Gelado      | 4,00")
  print("--------------------------------------------\n")

menu()

#Entrada do código do pedido
preco = 0 #Acumulador do preço total
while True:

#Verificando se o código é válido
  cod = int(input("Entre com o código do produto desejado:\n"))
  if (cod != 100 and cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod != 105 and cod != 200 and cod != 201):
    print("\nOpção Inválida!!!\n")
    menu()
    continue
#Verificando qual o produto e o valor através do código
  if (cod == 100):
    print("\nFoi escolhido o Cachorro-Quente")
    preco = preco + 9
  elif (cod == 101):
    print("\nFoi escolhido o Cachorro-Quente Duplo")
    preco = preco + 11
  elif (cod == 102):
    print("\nFoi escolhido o X-Egg")
    preco = preco + 12
  elif (cod == 103):
    print("\nFoi escolhido o X-Salada")
    preco = preco + 13
  elif (cod == 104):
    print("\nFoi escolhido o X-Bacon")
    preco = preco + 14
  elif (cod == 105):
    print("\nFoi escolhido o X-Tudo")
    preco = preco + 17
  elif (cod == 200):
    print("\nFoi escolhido o Refrigerante Lata")
    preco = preco + 5
  elif (cod == 201):
    print("\nFoi escolhido o Chá Gelado")
    preco = preco + 4
  
#Saída
  ped = input("\nDeseja pedir mais alguma coisa?\n Digite: \n s = Sim \n n = Não\n")
  if (ped == "s"):
    menu()
    continue
  else:
    print("----------- NOTA FISCAL -----------")
    print("\nO valor total do pedido = R${:.2f}\n".format(preco))
    print("-----------------------------------\n")
    break
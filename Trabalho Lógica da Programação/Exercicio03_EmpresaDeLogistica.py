#Apresentando meu código identificador e meu nome
print("\nCódigo Identificador: 4500068\nAluna: Francisca Ívyne Ripardo de Sousa\n\nExercicio 3\n ")

#Empresa de Logística
print("Bem-vindo a Empresa de Logística da Ívyne Ripardo")

#Função da verificação de dimensões do objeto e o valor
def dimensoesObjeto():
  while True:
    try:
      print("\n","-"*25,"MEDIDAS","-"*30,"\n")
      print("Atenção, ao invés de vírgula, utilizar ponto!!!")
      largura = float(input("Digite a Largura do Objeto (cm):\n"))
      comprimento = float(input("Digite o Comprimento do Objeto (cm):\n"))
      altura = float(input("Digite a Altura do Objeto (cm):\n"))

      cubico = altura * largura * comprimento
      
      #Verificando o valor do cm³ e se é aceito
      if (cubico < 1000):
        return 10
      elif (1000 <= cubico < 10000):
        return 20
      elif (10000 <= cubico < 30000):
        return 30
      elif (30000 <= cubico < 100000):
        return 50
      else:
        print("-"*60,"\n")
        print("Valor cúbico não aceito")
        print("Dimensões grandes não são permitidas")
        print("Tente Novamente!!!\n")
        print("-"*60,"\n")
        continue
    except ValueError:
      print("-"*60,"\n")
      print("Letras e códigos não são aceitos")
      print("Digite um valor númerico!!!!\n")
      print("-"*60)
      continue
    
#Função para calcular o multiplicador do peso    
def pesoObjeto():
  while True:
    try:
      print("\n","-"*28,"PESO","-"*28)
      peso = float(input("Digite o peso do Objeto (Kg):\n"))
      if (peso<=0.1):
        return 1
      elif (0.1 <= peso < 1):
        return 1.5
      elif (1 <= peso < 10):
        return 2
      elif (10 <= peso < 30):
        return 3
      else:
        print("-"*60,"\n")
        print("Peso não aceito")
        print("Objeto acima do peso")
        print("Digitar novamente o peso do Objeto (Kg)!!!\n")
        print("-"*60,"\n")
        continue
    except ValueError:
      print("-"*60,"\n")
      print("Letras e códigos não são aceitos")
      print("Digite um valor númerico!!!!\n")
      print("-"*60)
      continue 

#Função para calcular o multiplicador da rota
def rotaObjeto():
  while True:
      print("\n","-"*28,"ROTA","-"*28)
      print("\n Código |      Rota")
      print("   RS   | de Rio de Janeiro até São Paulo")
      print("   SR   | de São Paulo até Rio de Janeiro")
      print("   BS   | de Brasília até São Paulo ")
      print("   SB   | de São Paulo até Brasília")
      print("   BR   | de Brasília até Rio de Janeiro")
      print("   RB   | de Rio de Janeiro até Brasília")
      print("-"*60,"\n")

      rota = input("Digite a sigla de sua rota:\n")
      
      if (rota=="RS" or rota=="rs"):
        return 1
      elif (rota=="SR" or rota=="sr"):
        return 1
      elif (rota=="BS" or rota=="bs"):
        return 1.2
      elif (rota=="SB" or rota=="sb"):
        return 1.2
      elif (rota=="BR" or rota=="br"):
        return 1.5
      elif (rota=="RB" or rota=="rb"):
        return 1.5
      else:
        print("-"*60,"\n")
        print("\nERRO - Rota não encontrada")
        print("Digite novamente a sigla da rota que deseja!!!")
        print("-"*60,"\n")
        continue

#Chamando as funções e calculando o total
objeto = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = objeto*peso*rota

#Nota fiscal, repassando valor total e cálculo
print("\n","-"*22," Nota Fiscal ","-"*22,"\n")
print("Total a pagar(R$){:.2f}\n\n(dimensões: R${:.2f} * peso:{} * rota:{})".format(total,objeto,peso,rota),"\n")
print("-"*60)
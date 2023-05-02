#Apresentando meu código identificador e meu nome
id = ("\nCódigo Identificador: 4500068\nAluna: Francisca Ívyne Ripardo de Sousa\n\nExercicio 1 ")
print(id)

#Empresa X
print("\nBem-Vindo a Loja de Atacado de Ívyne Ripardo")

#Entradas do valor e quantidade de produto e variavéis
valor = float(input("\nValor da unidade do produto:\t\n!!! Por Favor, colocar ponto no lugar da vírgula!!!\n"))
qnt = int(input("Quantidade de produtos:\n"))
perc = 0
desc = 0

#Verificar condição de desconto
if(qnt <= 9):
  perc = 0
  desc = 0
elif(10 <= qnt <= 99 ):
  perc = 5
  desc = 0.5
elif(100<= qnt <= 999):
  perc = 10
  desc = 0.10
else:
  perc = 15
  desc = 0.15

#Cálculos
valor_s = (qnt * valor)
valor_d = valor_s - (valor_s*desc)

#Retornando Valores
print("\n\n------------ Sua Nota Fiscal ------------")
print("\nO valor sem desconto = R$ {:.2f}".format(valor_s))
print("\nDesconto de {}% recebido".format(perc))
print("\nO valor total com desconto = R$ {:.2f}".format(valor_d))
print("-------------------------------------")
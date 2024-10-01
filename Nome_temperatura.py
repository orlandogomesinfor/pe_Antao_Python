#Relembrar Função  Conjunto de código que ser acionado a qualquer
#                  momento
def pessoa(nn, t):    #Definindo funcao pessoa
   print("Bom dia!",nn)
   print("Hoje é Terça-feira")
   if t<10:
       print("O dia esta muito!")
   elif t<15:
       print("O dia esta ameno!")
   elif t<30:
       print("O dia esta quente!")
   else:
       print("ATENCAO O DIA ESTA MUITO QUENTE!")
pessoa("Maria",38)    #Chama a função
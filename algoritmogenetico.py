#Pedro Moraes, Maria Eduarda, Isadora Coelho
#exercicio 8
#grupo 15

import random
import numpy as np
from matplotlib import pyplot

# CÁLCULO DA FUNÇÃO
def calculo_funcao(a, b):
  funcao = 5 + (3*a) - (4*b) - (a**2) + (a*b) - (b**2)
  return funcao

# GERA OS VALORES ENTRE O INTERVALO DE -10 - 10
def geraValores():
  num = random.uniform(-10.0000, 10.0000)
  return num

# ACHA O NÚMERO MAIS PROXIMO DE UM VALOR
def valorProximo(lst, K):
  nmp = lst[0] #nmp "numero mais proximo"
  for i in lst:
    if(abs(K - nmp) >= (abs(K - i))): #se a menor distância até o momento for maior do que a calculada, elemento mais prox muda
      nmp = i
  return nmp

# SELECAO
def selecao(populacao):
  melhorFitness = 9.3333 #9.3333 valor de z, dado pelo enunciado
  vetFitness = [] 
  vetAux = []
  nRanking = random.randint(1, len(populacao))

  # seleciona apenas os fitness da populacao
  for i in range(len(populacao)):
    vetAux.append(populacao[i]['fitness'])

  # pega fitness aleatorio e coloca no vetor vetFitness
  for i in range(nRanking):
    escolhido = random.choice(vetAux)
    vetFitness.append(escolhido)

  # seleciona o fitness com mais aptdião do vetFitness
  selecionado = valorProximo(vetFitness, melhorFitness)

  # procura a posição do numero selecionado
  for i in range(len(populacao)):
    if(populacao[i]['fitness'] == selecionado):
        pos = i
  return pos

# CRUZAMENTO
def cruzamentoX(pai1, pai2):
  media = (pai1['X'] + pai2['X']/2)
  return media

def cruzamentoY(pai1, pai2):
  media = (pai1['Y'] + pai2['Y']/2)
  return media

# ELETISMO, encontra a posição do valor mais proximo do melhor fitness
def calcElitismo(pop):
  pop = sorted(pop, key = lambda i : i ['fitness'], reverse = True)
  return(pop[0])

# MUTAÇÃO NÃO UNIFORME
def mutacao(filho):
  if(random.uniform(0, 100) <= 3):
    while filho > 10 or filho < -10:
      filho = np.random.exponential(2.5, 1)
  return filho


# IMPRIME COMPORTAMENTO DA POPULAÇÃO
def printa(POPULA = [], jota = 0): 
  x = [] 
  y = []

  POPULA = sorted(POPULA, key = lambda i : i ['fitness'], reverse = True)
  print(POPULA)

  for k in POPULA:
    x.append(k['X'])
    y.append(k['Y']) 

  print(len(POPULA))
  pyplot.xlim([-10,10])
  pyplot.ylim([-10,10])
  pyplot.scatter(x, y)
  pyplot.title(f'POPULAÇÃO ATUAL {jota}')
  pyplot.show()

# ALGORITMO GENÉTICO

def agenetico(POPULA = []):
  POPULACAO = []  # p/ POPULACOES SEGUINTES
  
  j = 0
  while(j < Geracoes - 1):
    POPULACAO.clear()
    posM = calcElitismo(POPULA)  # Pega o melhor Fitness da População
                                   # Passa um indivíduo para a próxima população
    POPULACAO.append(posM)

    while(len(POPULACAO) < len(POPULA)):
     
      # SELECAO #
      pos1 = selecao(POPULA)
      pos2 = selecao(POPULA)
      # Caso os pais sejam iguais
      while(POPULA[pos1] == POPULA[pos2]):
        pos2 = selecao(POPULA)

      # print(POP_INICIAL[pos1])  # teste pai1
      # print(POP_INICIAL[pos2])  # teste pai2
      ## CRUZAMENTO ##
      if(random.uniform(0, 100) <= 85):
        filhoX = cruzamentoX(POPULA[pos1], POPULA[pos2])
        filhoY = cruzamentoY(POPULA[pos1], POPULA[pos2])
        filhoX = mutacao(filhoX)
        filhoY = mutacao(filhoY)
        cromossomo = {'X': filhoX, 'Y': filhoY, 'fitness': 0.0}  # gera o X e Y
        cromossomo['fitness'] = calculo_funcao(cromossomo['X'], cromossomo['Y'])  # gera o Fitness
        POPULACAO.append(cromossomo)
      else:
        taxa = random.uniform(0, 1)
        if(taxa < 0.5):
          POPULACAO.append(POPULA[pos1])
        elif(taxa > 0.5):
          POPULACAO.append(POPULA[pos2])
    POPULA = POPULACAO[:] #copiar todo vetor

    
    j += 1
    print(POPULACAO)
    printa(POPULACAO, j)

# GERANDO A PRIMEIRA POPULACAO

Geracoes = int(input("QUANTA GERAÇÕES VOCÊ QUER GERAR?"))
num_elementos = int(input("QUANTOS ELEMENTOS POR GERACOES?"))
POP_INICIAL = []  # Populacao inicial

DADOS = []  # Para a plotagem do gráfico
for i in range(num_elementos):
  cromossomo = {'X': geraValores(),'Y': geraValores(),'fitness': 0.0}  # gera o X e Y
  cromossomo['fitness'] = calculo_funcao(cromossomo['X'], cromossomo['Y'])  # gera o Fitness
  POP_INICIAL.append(cromossomo)


printa(POP_INICIAL, 0)
agenetico(POP_INICIAL)

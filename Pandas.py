import pandas as pd
import matplotlib.pyplot as plt


ecom = pd.read_csv("Ecommerce Purchases.csv") #lendo os arquivos

ecom.head()# ver os dados por completo
print('\n', ecom.head)

print("--------------------------------info")
ecom.info() #para obter todas as informações sobre o dataFrame
print('\n', ecom.info())

print("------------------------------acessando colunas")
ecom['Purchase Price'].mean()# acessando a coluna de preços e verificando o preço médio
# ecom.collumns verificando as colunas disponiveis parametro não metodo

ecom['Purchase Price'].max()
ecom['Purchase Price'].min()
print(ecom['Purchase Price'].mean())

print("------------------------------verificando")
ecom[ecom['Language'] == 'en'].count()# verificando quem utilizou compras na linguagem em inglês
print('\n', ecom[ecom['Language'] == 'en'].count())
ecom[ecom['Job'] == 'Lawyer'].shape #verificando quantas pessoas tem o cargo de advogado

print("--------------------AM ou PM---------------")
ecom['AM or PM'].value_counts()#quantas pessoas fizeram compras AM ou PM
print(ecom['AM or PM'].value_counts())
ecom['Job'].value_counts()# titulos de trabalhos ordenados .hed() filtra a quantidade que eu quero
print(ecom['Job'].value_counts())
print("--------------------AM ou PM---------------")
ecom[ecom['Lot'] == '90 WT'] # verificando a região da compra 90 wt  ['Purchase Price'] coluna com o valor do preço
print(ecom[ecom['Lot'] == '90 WT'])

print("-------------------AM ou PM-------------------------")
ecom[ecom['Credit Card'] == 4926535242672835]['Email'] # verificando  o dono do seguinte cartão e os dados da pessoa
print(ecom[ecom['Credit Card'] == 4926535242672835]['Email'])


ecom[(ecom['CC Provider']== 'American Express') & (ecom['Purchase Price']> 95)]
print(ecom[(ecom['CC Provider']== 'American Express') & (ecom['Purchase Price']> 95)])
# verificando o provedor do cartão e quantos são iguais ao American
# e compras maiores que 95, e .shape para ver o tamanho disso

#quantas pessoas tem o cartão que expira em 2025 ?
sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25') #verificando quantas pessoas tem o cartão com venc. 2025
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
# função lambda que começa a partir do 3 em diante tirando 02\ do cartão

#quais são os 5 principais provedores de e-mail/hosts populares(gmail. yahoo...)
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts()
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts())
#função lambda com split o @ ficará no meio e eu determino lado esquedo é =0 e lado direito =1
# .value_counts() metodo filtra e conta os princiapsi provedores
# .iloc[:5] mostra os 5 principais mais usados.
print("---------------------Grafico")

print(len(ecom))

# Criando grupos
mean = ecom.groupby(['AM or PM', 'Language']).mean()

median = ecom.groupby(['Purchase Price', 'Credit Card']).median()

# grafico em histograma
mean.plot(kind='hist') # Precisa ser revisado
plt.title('Grafico em histograma')
plt.xlabel('label eixo x')
plt.ylabel('label eixo y')
plt.show()

# Grafico em barras
mean.plot(kind='bar') # Precisa ser revisado
plt.title('Grafico em histograma')
plt.xlabel('label eixo x')
plt.ylabel('label eixo y')
plt.show()
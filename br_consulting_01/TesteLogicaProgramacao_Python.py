## Abaixo se encontram as 4 quest�es do seu teste de L�gica de Programa��o.
## Implemente todas elas neste arquivo seguindo os padr�es da linguagem escolhida e utilizando os cabe�alhos das fun��es.
## As suas respostas ser�o corrigidas analisando a l�gica utilizada, a sua familiaridade com a linguagem e ser�o submetidas a casos de teste al�m dos exemplos presentes nesse arquivo.
## Vale lembrar que voc� tem at� 2 horas, a partir do recebimento do e-mail em hor�rio combinado anteriormente, para fazer o m�ximo de quest�es que conseguir.
## Por favor, confirme o recebimento deste teste antes de inici�-lo.
## Boa sorte!!


import numpy as np


## Maior que os da sua direita.
# Crie uma fun��o que receba um vetor de n�meros inteiros positivos e retorne um vetor com cada n�mero que seja estritamente maior que todos os n�meros ap�s ele. Por exemplo, dado o vetor [5, 9, 8, 7], � retornado [9, 8, 7], pois 9 � maior que 8 e 7, 8 � maior que 7 e 7 � o �ltimo elemento, por consequ�ncia, n�o h� ningu�m maior que ele � sua direita. J� para o vetor [3, 3, 4], � retornado apenas [4], o 3 n�o � retornado pois n�o pode ser igual, apenas maior.


## Exemplos Python:
# >>> maior_que_direita([3, 13, 11, 2, 1, 9, 5])
# >>> [13, 11, 9, 5]
#
# >>> maior_que_direita([5, 5, 5, 5, 5, 5])
# >>> [5]
#
# >>> maior_que_direita([5, 9, 8, 7])
# >>> [9, 8, 7]
#
# >>> maior_que_direita([1, 2, 3])
# >>> [3]


def maior_que_direita(vetor):

	res = []
	l = len(vetor) - 1

	for p in range(l):
		i = p + 1
		for i in range(i, l + 1):
			if vetor[p] <= vetor[i]:
				break
			if i == l:
				res.append(vetor[p])
	res.append(vetor[p + 1])

	return res



## O Estranho do Grupo
# Escreva uma fun��o que recebe uma lista com no m�nimo tr�s palavras e retorne "Verdadeiro" caso exatamente uma palavra na lista tenha tamanho diferente em rela��o �s outras. Retorne Falso, caso contr�rio. Por exemplo, na lista ["Mais","Menos","Nada","Muito"] tem duas palavras com 4 letras e outras duas com 5, ent�o � retornado Falso. J� na lista ["c�co","�gua","casa","praia"], apenas uma palavra cont�m 5 letras e todas as outras cont�m 4.


## Exemplos Python:
# >>> estranho_grupo(["c�co","�gua","casa","praia"])
# >>> Verdadeiro
#
# >>> estranho_grupo(["prova","certo","errado"])
# >>> Verdadeiro
#
# >>> estranho_grupo(["vento","ventania","ventilador"])
# >>> Falso
#
# >>> estranho_grupo(["Mais","Menos","Nada","Muito"])
# >>> Falso


def estranho_grupo(vetor):

	lengths = []

	for word in vetor:
		lengths.append(len(word))

	unique_len = np.unique(lengths, return_counts=True)

	if len(unique_len[0]) == 2:
		if 1 in unique_len[1]:
			return True
	return False



## Dist�ncia Vogal
# Escreva uma fun��o que recebe uma string e retorne uma outra string onde cada caracter � trocado pela sua dist�ncia at� a vogal mais pr�xima. Por exemplo, para a palavra "chama" deve ser retornado "21010", pois o 'c' est� a 2 caracteres da vogal mais pr�xima, o 'a', o 'h' est� a 1 s�, e assim por diante. Vale destacar que quando o caracter em si � um vogal, � retornado um 0 para ele.


## Exemplos Python:
# >>> distancia_vogal("aaaaa")
# >>> "00000"
#
# >>> distancia_vogal("babbb")
# >>> "10123"
#
# >>> distancia_vogal("abcdabcd")
# >>> "01210123"
#
# >>> distancia_vogal("shopper")
# >>> "2101101"


def distancia_vogal(palavra):

	dist_rev = ""
	count = 0

	for l in palavra[::-1]:
		if l in "aeiou":
			count = 0
			dist_rev += str(count)
		else:
			count += 1
			dist_rev += str(count)

	dist = dist_rev[::-1]
	count = -1
	res = ""

	for i in range(len(dist)-1):
		if dist[i] == '0':
			count = 0
			res += str(count)
		elif count > -1 and count <= int(dist[i+1]):
			count += 1
			res += str(count)
		else:
			res += dist[i]
	if dist[i + 1] == '0':
		res += '0'
	else:
		res += str(count+1)

	return res



## Menor Inteiro
# Dado uma lista de n�meros inteiros, crie uma fun��o que ache o menor n�mero inteiro positivo que � igualmente divisivel por todos os n�meros dentro da lista. Em outras palavras, encontre o menor m�ltiplo comum.


## Exemplos Python:
# >>> menor_inteiro([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> 2520
#
# >>> menor_inteiro([5])
# >>> 5
#
# >>> menor_inteiro([5, 7, 11])
# >>> 385
#
# >>> menor_inteiro([5, 7, 11, 35, 55, 77])
# >>> 385


def menor_inteiro(numero):

	return np.lcm.reduce(numero)

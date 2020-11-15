from termcolor import colored
from TesteLogicaProgramacao_Python import *


def print_tests(function, exer, corr):
	for i in range(len(exer)):
		print("{}{}{}{!s:<20}{}{}".format(colored("Teste ", 'blue'), colored(i + 1, 'blue'), colored(": ", 'blue'), function(exer[i]), colored("Correção: ", 'green'), corr[i]))


exer1 = [[3, 13, 11, 2, 1, 9, 5], [5, 5, 5, 5, 5, 5], [5, 9, 8, 7], [1, 2, 3]]
corr1 = [[13, 11, 9, 5], [5], [9, 8, 7], [3]]

exer2 = [["c�co","�gua","casa","praia"], ["prova","certo","errado"], ["vento","ventania","ventilador"], ["Mais","Menos","Nada","Muito"]]
corr2 = ["Verdadeiro", "Verdadeiro", "Falso", "Falso"]

exer3 = ["aaaaa", "babbb", "abcdabcd", "shopper", "bbbaabbbbabb"]
corr3 = ["00000", "10123", "01210123", "2101101", "321001221012"]

exer4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [5], [5, 7, 11], [5, 7, 11, 35, 55, 77]]
corr4 = ["2520", "5", "385", "385"]

function = [maior_que_direita, estranho_grupo, distancia_vogal, menor_inteiro]
exer = [exer1, exer2, exer3, exer4]
corr = [corr1, corr2, corr3, corr4]

for i in range (len(function)):
	print(colored("\n	EXERCÍCIO", 'magenta'), colored (i + 1, 'magenta'), colored("-", 'magenta'), colored (function[i].__name__, 'magenta'))
	print_tests(function[i], exer[i], corr[i])

print("")

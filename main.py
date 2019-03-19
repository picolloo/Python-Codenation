# coding: utf-8

import csv
from itertools import islice

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    with open('file.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter = ',')
        
        nationality = []

        next(readCSV)
        for row in readCSV:
            nationality.append(row["nationality"])

        print (len(list(set(nationality))))


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('file.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter = ',')
        
        clubs = []

        next(readCSV)
        for row in readCSV:
            clubs.append(row["club"])

        print (len(list(set(clubs))))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
     with open('file.csv', encoding="utf8") as csvfile:
        head = list(islice(csvfile, 22))
        readCSV = csv.DictReader(head, delimiter = ',')

        next(readCSV)
        for row in readCSV:
            print (row["full_name"])

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    pass

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    pass

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    pass

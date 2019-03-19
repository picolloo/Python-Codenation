# coding: utf-8

import csv
from itertools import islice
from functools import reduce
from collections import Counter

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
def q_1():
    with open('data.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        nationality = []

        next(readCSV)
        for row in readCSV:
            nationality.append(row["nationality"])

        return len(list(set(nationality)))


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('data.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        clubs = []
        for row in readCSV:
            clubs.append(row["club"])

        return len(list(set(clubs)))


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open('data.csv', encoding="utf8") as csvfile:
        head = list(islice(csvfile, 21))
        readCSV = csv.DictReader(head, delimiter=',')

        players = []
        for row in readCSV:
            players.append(row["full_name"])

        print(len(players))
        return players


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        richest = {}

        for row in readCSV:
            salary = float(row["eur_wage"])

            if len(richest) == 10:
                lower = min(richest) if richest else 0
                if (salary > lower):
                    del [lower]

            if salary in richest:
                richest[salary].append(row["full_name"])
            else:
                richest[salary] = [row["full_name"]]

        richest = dict(sorted(richest.items(), reverse=True))
        return reduce(list.__add__, list(richest.values()))[:10]


# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        older = {}
        for row in readCSV:
            age = int(row["age"])
            name = row["full_name"]

            if len(older) == 10:
                lower = min(older) if older else 0
                if age > lower:
                    del older[lower]

            if age in older:
                older[age].append(name)
            else:
                older[age] = [name]

        older = dict(sorted(older.items(), reverse=True))
        return reduce(list.__add__, list(older.values()))[:10]


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open('data.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        ages = []
        for row in readCSV:
            ages.append(row["age"])

        return {int(k): int(v) for k, v in Counter(ages).items()}

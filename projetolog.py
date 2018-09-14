# !/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = "news"

q1 = "Quais são os três artigos mais populares de todos os tempos?"

query1 = """
SELECT title,
       count(*) AS views
FROM articles
JOIN log ON log.path = '/article/' || articles.slug
GROUP BY title
ORDER BY views DESC
LIMIT 3;
"""

q2 = "Quem são os autores de artigos mais populares de todos os tempos?"

query2 = """
SELECT authors.name, count(*) as views
FROM articles
JOIN authors
ON articles.author = authors.id
JOIN log
ON articles.slug = substring(log.path, 10)
WHERE log.status LIKE '200 OK'
GROUP BY authors.name ORDER BY views DESC;
"""

q3 = "Em quais dias mais de 1% das requisições resultaram em erros?"

query3 = ("select data, percentual from percentualerro where percentual>1.0;")

# Conecta ao banco e faz a consulta


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_queryResults(query1)
result2 = get_queryResults(query2)
result3 = get_queryResults(query3)


# Funcao para imprimir os resultados


def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("%s - %d" % (title, res) + " views")
    print("\n")

print(q1)
print_results(result1)
print(q2)
print_results(result2)
print(q3)
print(str(result3[0][0]) + " - " + str(result3[0][1]) + "%")

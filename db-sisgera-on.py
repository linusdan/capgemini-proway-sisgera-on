#!/usr/bin/env python
# SISGERA ON - Sistema de Gerenciamento de Anúncios Online
# Script para criação / conexão do banco de dados (SQLite)
# Maintainer: Danilo Santos (danilosantos07@protonmail.com)
# versão 20210515 (Codename: Taste)

import sqlite3

# Para a criação do banco de dados, descomentar as linhas 12, 14, 15, 17 e 33
# Para conexão, descomentar linhas 12, 14 e 15

banco = sqlite3.connect('sisgera.db')

cursor = banco.cursor()
print("Banco de dados criado / conectado com sucesso!")

#cursor.execute("CREATE TABLE sisgera (nome_anuncio text, cliente text, data_inicio text, data_termino text, quantidade_dias text, dias_hora text, investimento_dia real, valor_total_investido real, maxima_visualizacoes integer, maxima_cliques integer, maxima_compartilhamentos integer)") 
#cursor.execute("CREATE TABLE sisgera (nome_anuncio text, cliente text, data_inicio text, data_termino text, investimento_dia real, )")


# Inserção de valores teste: Descomentar linhas 12, 14, 21 e 33
#cursor.execute("INSERT INTO sisgera VALUES ('AnuncioUm','Danilo','13/05/2021','16/05/2021',130.00)")


# Para ver se a criação do banco de dados foi bem-sucedida pelo terminal, descomentar linhas 12, 14, 27, 28, 29, 30, 31 e 33.
# Para visualização por interface, utilizar o programa DB Browser for SQLite (recomendado).

print('-=' * 30)
print("Dados do banco cadastrados: ")
cursor.execute("SELECT * FROM sisgera")
print(cursor.fetchall())
print('-=' * 30)

banco.commit()

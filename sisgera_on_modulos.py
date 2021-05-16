#!/usr/bin/env python
#
# SISGERA ON - Sistema de Gerenciamento de Anúncios Online
# Módulo de funções do SISGERA ON
# Maintainer: Danilo Santos (danilosantos07@protonmail.com)
# versão 20210513 (Codename: Taste)

import sqlite3
import time
from datetime import datetime

# Script de conexão do banco de dados
banco = sqlite3.connect('sisgera.db')
cursor = banco.cursor()


def menu():
    # Menu de opções do sistema
    opcao_menu = 0
    while opcao_menu != 3:
        print('''
        =================================================================
        ===  SISGERA ON - Sistema de Gerenciamento de Anúncios Online ===
        ===             Cadastro e relatório de anúncios              ===
        ===                                                           ===
        ===  1) Cadastrar anúncio                                     ===
        ===  2) Ver relatório de anúncios cadastrados                 ===
        ===  3) Sair                                                  ===
        =================================================================
        ''')
        opcao_menu = int(input("Escolha opção: "))
        if opcao_menu == 1:
            cadastrar_anuncio()
        elif opcao_menu == 2:
            relatorio()
        elif opcao_menu == 3:
            print("Encerrando sistema...")
            time.sleep(1)
        else:
            print("Opção inválida. Tente novamente. ")
    print("Sistema finalizado! Até logo!")


def cadastrar_anuncio():
    while True:
        # 1) Inserir nome do anúncio
        nome_anuncio = str(input("Nome do anúncio: "))

        # 2) Inserir nome do cliente
        cliente = str(input("Nome do cliente: "))

        # 3) Obter data de início do contrato
        obter_data_inicio = input("Data de início [DD/MM/YYYY]: ")
        # 3.1) Uso da função strptime para formatação da string para data:
        converter_data_inicio = datetime.strptime(obter_data_inicio, '%d/%m/%Y')
        # 3.2) SQLite não aceita manipulação do módulo datetime com a função strptime para inserção do dado no banco, logo
        # módulo tem que convertido para strftime:
        data_inicio = converter_data_inicio.strftime('%d/%m/%Y')

        # 4) Obter data de término do contrato
        obter_data_termino = input("Data de término [DD/MM/YYYY]: ")
        converter_data_termino = datetime.strptime(obter_data_termino, '%d/%m/%Y')
        data_termino = converter_data_termino.strftime('%d/%m/%Y')

        # 5) Investimento/dia do cliente
        investimento_dia = float(input("Quanto o cliente deseja investir por dia? (R$) "))

        # Formula responsável por calcular a diferença de dias inserida no cadastro
        # de anúncios para obter o valor total investido pelo cliente
        quantidade_dias = (converter_data_termino - converter_data_inicio).days
        dias_hora = quantidade_dias * 24
        valor_total_investido = dias_hora * investimento_dia
        
        # Cálculo da quantidade máxima de visualizações
        valor_anuncio = 1.00 / 30
        alcance_compartilhamento = 3 * 40 * 4
        maxima_visualizacoes = valor_total_investido * valor_anuncio * alcance_compartilhamento

        # Cálculo da quantidade máxima de cliques
        maxima_cliques = valor_total_investido / 12 * 20

        # Cálculo da quantidade máxima de compartilhamentos
        maxima_compartilhamentos = valor_total_investido / 3 * 4
        
        # Inserção de dados do cadastro (comentar linhas 86 e 87 caso precisar testar a saída de dados)
        cursor.execute("INSERT INTO sisgera VALUES('"+nome_anuncio+"','"+cliente+"','"+data_inicio+"','"+data_termino+"',"+str(quantidade_dias)+","+str(dias_hora)+","+str(investimento_dia)+","+str(valor_total_investido)+","+str(maxima_visualizacoes)+","+str(maxima_cliques)+","+str(maxima_compartilhamentos)+")")
        banco.commit()
        
        # Área de testes [Output] - Comentar linhas 90 a 106 para evitar mostrar dados desnecessários no sistema de produção
        #print()
        #print('-=' * 30)
        #print("AREA DE TESTES [OUTPUT - SEM BANCO DE DADOS]")
        #print()
        #print("Nome do anúncio: ", nome_anuncio)
        #print("Cliente: ", cliente)
        #print("Data de início do contrato: ", data_inicio)
        #print("Data de término do contrato: ", data_termino)
        #print("Dias de contrato: ", quantidade_dias)
        #print("Dias/Hora de contrato: ", dias_hora,'H')
        #print(f'Investimento do cliente por dia: (R$) {investimento_dia:,.2f}')
        #print(f'Valor total investido é de R$ {valor_total_investido:,.2f}')
        #print("Quantidade máxima de visualizações: ", int(maxima_visualizacoes))
        #print("Quantidade máxima de cliques: ", int(maxima_cliques))
        #print("Quantidade máxima de compartilhamentos: ", int(maxima_compartilhamentos))
        #print('-=' * 30)
        #print()
        resposta = str(input('Deseja cadastrar outro cliente? [S/N] '))
        if resposta in 'Nn':
            print(f'Anúncios cadastrados: {len(resposta)}')
            break
            return menu()


def relatorio():
    print("Paramore - No Friend.mp3")
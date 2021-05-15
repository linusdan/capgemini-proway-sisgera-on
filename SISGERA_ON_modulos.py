#!/usr/bin/env python
#
# SISGERA ON - Sistema de Gerenciamento de Anúncios Online
# Módulo de funções do SISGERA ON
# Maintainer: Danilo Santos (danilosantos07@protonmail.com)
# versão 20210513 (Codename: Taste)

import time
from datetime import datetime

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
    dados = dict()
    while True:
        # Inserir nome do anúncio
        dados['nome_anuncio'] = str(input("Nome do anúncio: "))

        # Inserir nome do cliente
        dados['cliente'] = str(input("Nome do cliente: "))

        # Obter data de início
        dados['obter_data_inicio'] = input("Data de início [DD/MM/YYYY]: ")
        dados['data_inicio'] = datetime.strptime(dados['obter_data_inicio'], '%d/%m/%Y')

        # Obter data de término
        dados['obter_data_termino'] = input("Data de término [DD/MM/YYYY]: ")
        dados['data_termino'] = datetime.strptime(dados['obter_data_termino'], '%d/%m/%Y')

        # Investimento/dia
        dados['investimento_dia'] = float(input("Quanto o cliente deseja investir por dia? (R$) "))

        # Formula responsável por calcular a diferença de dias inserida no cadastro
        # de anúncios para obter o valor total investido pelo cliente
        quantidade_dias = (dados['data_termino'] - dados['data_inicio']).days
        dias_hora = quantidade_dias * 24
        valor_total_investido = dias_hora * dados['investimento_dia']

        print()
        print('-=' * 30)
        print("Nome do anúncio: ", dados['nome_anuncio'])
        print("Cliente: ", dados['cliente'])
        print("Data de início do contrato: ", dados['data_inicio'])
        print("Data de término do contrato: ", dados['data_termino'])
        print("Dias de contrato: ", quantidade_dias)
        print("Dias/Hora de contrato: ", dias_hora, 'H')
        print(f'Investimento do cliente por dia: (R$) ', dados['investimento_dia'])
        print(f'Valor total investido é de R$ {valor_total_investido:,.2f}')
        print('-=' * 30)
        print()
        resposta = str(input('Deseja cadastrar outro cliente? [S/N] '))
        if resposta in 'Nn':
            print(f'Anúncios cadastrados: {len(resposta)}')
            break
            return menu()


def relatorio():
    print("Paramore - No Friend.mp3")

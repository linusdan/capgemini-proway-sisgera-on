# capgemini-proway-sisgera-on
## SISGERA ON - Sistema de Gerenciamento de Anúncios Online

**SISGERA ON** é um sistema escrito em python onde permite o cadastro de anúncios de clientes.

O sistema após o cadastro tem a possibilidade de exibir o relatório da pessoa onde contém o valor investido pelo cliente e quantidade máxima de visualizações, cliques e compartilhamentos do anúncio online solicitado.


## Table of Contents

- [Estrutura](#Estrutura)
- [Instalação](#Instalação)
   - [Python](#Python)
   - [PIP](#PIP)
   - [SQLite3](#SQLite3)
- [Uso](#Uso)


## Estrutura
| Arquivo | Descrição |
| --- | --- |
| sisgera-main.py | Arquivo principal para execução do programa pelo terminal. |
| db-sisgera-on.py | Script para criação / conexão do banco de dados (SQLite). Para uso: Ler comentários do arquivo. |
| sisgera_on_modulos.py | Módulo de funções do programa. |
| sisgera.db | Banco de dados do sistema (SQLite). |  



## Instalação
Para compilação e execução do programa, é necessário ter instalado:
- Python 3+
- PIP (gerenciador de pacotes de software da linguagem Python)
- SQLite3


### Python

#### Windows:
1) Faça o download do arquivo: [**Windows 32-bit**](https://www.python.org/ftp/python/3.9.5/python-3.9.5.exe) | [**Windows 64 bit**](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)  
2) Instale o arquivo dando dois cliques.

#### Linux:  

No terminal, digite:

```bash
# Ubuntu / Debian:
 $ sudo apt install python3

# Arch Linux / Manjaro:
 $  sudo pacman -S python3
 ```

OBS: Para outras distribuições linux, por gentileza, pesquisar o método de instalação na documentação do sistema operacional.

#### Mac:
1) Abra o terminal.
2) Instale o [**homebrew**](https://brew.sh/#install).
3) Após a instalação, digite:
```bash
 $  brew install python3
 ```

Para verificar se o python foi instalado com sucesso, digite no terminal:
```bash
 $  python3 --version
 ```

### PIP
No terminal, digite:

#### Windows: 
1) Download [**get-pip.py**](https://bootstrap.pypa.io/get-pip.py) numa pasta do seu computador.  
2) Abra o prompt de comando e navegue até a pasta contendo o instalador get-pip.py  
3) Execute o seguinte comando:  
```bash
 $  python3 get-pip.py
 ```


#### Linux:
```bash
# Ubuntu
 $  sudo apt install python3-pip

# Arch / Manjaro
 $  sudo pacman -S python-pip

# Mac
 $  brew install python3

# Para verificar se foi instalado com sucesso, digite:
 $  pip -V
```

### SQLite3
#### Windows: 
1) Baixe o arquivo [**SQLite Tools**](https://www.sqlite.org/2021/sqlite-tools-win32-x86-3350500.zip).
2) Descompacte o arquivo.
3) Execute o arquivo '.exe'. Irá abrir o terminal com as linhas de comando.

#### Linux:
Abra o terminal e digite:
```bash
 $  pip install wheel db-sqlite3
 ```

#### Mac:
Não é necessário instalar, pois já é instalado por padrão no sistema operacional.
Cheque a instalação digitando no terminal:
```bash
 $  sqlite3
 ```

Para checar a instalação no windows e linux, digite no terminal / prompt de comando:
```bash
 $  sqlite3
 ```

Para sair do prompt de comando, aperte as telas ``` CTRL+C ```.

Para visualização das tabelas do banco de dados pela interface gráfica, instale o [**DB Browser for SQLite**](https://sqlitebrowser.org/).


## Uso
#### Windows / Linux / Mac:

1) Faça o [**download**](https://github.com/linusdan/capgemini-proway-sisgera-on/archive/refs/heads/main.zip) do sistema.  

2) Extraia a pasta do arquivo num lugar de sua preferência.  

3) Renomeie a pasta do arquivo para SISGERA.  

4) Com o terminal / prompt de comando:  

4.1) Navegue até a pasta SISGERA  
```bash
 $  cd (pasta da sua preferência)
 $  cd SISGERA 
```

4.2) Compilação:
```bash
 $  python3 sisgera-main.py
```

Ao compilar, irá aparecer a tela com três opções para escolha:  
 ```bash
 1) Cadastrar anúncio
 2) Ver relatório de anúncios cadastrados
 3) Sair
 ```

**Opção 1:**
 Ao escolher, será solicitado os dados necessários para efetuar o cadastro.  
 Será solicitado:
 ```bash
  1) Nome do anúncio:
  2) Cliente:
  3) Data de início: [DD/MM/YYYY]
  4) Data de término: [DD/MM/YYYY]
  5) Investimento por dia (R$):
 ```
 
 Digite os dados conforme solicitado e tecle enter.  
 Após a conclusão, será mostrado que o cadastro foi efetuado.
 Será perguntado se deseja fazer outro cadastro.  
 Caso não queira, sistema irá informar retorno ao menu principal.  

**Opção 2:**
 ```bash
 Exibe o relatório de cadastro de acordo com nome do cliente ou intervalo de tempo.
 Para fazer a busca, selecione se quer busca por nome do cliente ou data de inicio do contrato do cadastro.
 Digite a informação selecionada e pronto! Dado exibido :)
 Será perguntado se deseja fazer outra consulta.  
 Caso não queira, sistema irá informar retorno ao menu principal.  
 ```
 
**Opção 3:**
 ```bash
 Sistema é encerrado.
  ```

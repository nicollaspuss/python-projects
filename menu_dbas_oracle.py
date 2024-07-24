# !/usr/bin/python3
# --------------------------------------------------------
# Author: Nicollas Peres Puss
# Date: 24/07/2024
# Project: Platform Python - Oracle Database.
# --------------------------------------------------------
# V1:
# V1.1: Project with option of reset password of every production databases for DBA user.
# V1.2: Project with option of reset password of some production database for DBA user.
# --------------------------------------------------------
# V2:
# V2.1: Project with option of Plataform for executing script of every production databases for DBA user.
# --------------------------------------------------------
# V3:
# V3.1: Project listing the string connection of every production databases.
# --------------------------------------------------------
import os 
import sys
import time
import string
import time
import cx_Oracle

# Lista de DBAs - Oracle - Sicredi:
dbas = { 
    'DBA1': 'user1',
    'DBA2': 'user2',
    'DBA3': 'user3',
    'DBA4': 'user4',
    'DBA5': 'user5',
    'DBA6': 'user6',
    'DBA7': 'user7',
    'DBA8': 'user8',
    'DBA9': 'user9',
    'DBA10': 'user10',
    'DBA11': 'user11'
}

# Reset de senha - Single database:
def reset_password_single_databases():
    print("Digite o nome do usuário DBA para reset de senha: ")
    print("Digite sua nova senha para reset de senha: ")
    print("Digite o nome do database para reset de senha: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    usuario = input("User: ")
    if usuario.lower() in [dbas[key].lower() for key in dbas]:
        senha = input("Senha: ")
        database = input("Database: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Removendo arquivos .txt da última execução...")
        print("Removendo arquivos .txt da última execução...")
        os.system("rm string_single_database.txt")
        os.system("rm string_single_database_ajustado.txt")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Verificando o database desejado...")
        con = cx_Oracle.connect('username/password@host:port/service_name')
        cur = con.cursor()
        cur.execute("select distinct string_conexao from usernamer.username_databases where upper(dbname) = upper('" + database + "') and status = 'ACTIVE' and TIPO_AMBIENTE = 'PROD' and string_conexao is not null")
        for result in cur:
            string_conexao = open('string_single_database.txt', 'w')
            print(result, file = string_conexao)
        con.close()
        string_conexao.close()
        os.system("cat string_single_database.txt | rev | cut -c4- | rev | cut -c 3- > string_single_database_ajustado.txt")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Conectando-se no database desejado...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        f = open("string_single_database_ajustado.txt")
        for line in f:
            try:
                con = cx_Oracle.connect('username/password@' + line)
                cur = con.cursor()
                cur.execute("alter user " + usuario + " identified by " + senha)
                print("Database: " + line + " - Senha do usuário " + usuario + " atualizada para: " + senha + " com sucesso!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            except cx_Oracle.DatabaseError as e:
                print("Erro no banco de dados: " + line, end='')
                print(str(e))
            sys.exit()
    else:
        print("Usuário não é um DBA")
        sys.exit()

# Reset de senha - Todos databases:
def reset_password_all_databases():
    print("Digite o nome do usuário DBA para reset de senha: ")
    print("Digite sua nova senha para reset de senha: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    usuario = input("Usuário: ")
    if usuario.lower() in [dbas[key].lower() for key in dbas]:
        senha = input("Senha: ")
        print("Removendo arquivos .txt da última execução...")
        print("Removendo arquivos .txt da última execução...")
        os.system("rm string_all_databases.txt")
        os.system("rm string_all_databases_ajustado.txt")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Conectando-se em todos os databases...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        con = cx_Oracle.connect('username/password@host:port/service_name')
        cur = con.cursor()
        cur.execute("select distinct string_conexao from usernamer.username_databases where status = 'ACTIVE' and TIPO_AMBIENTE = 'PROD' and dbname not in ('DB1', 'DB2') and string_conexao is not null order by string_conexao")
        for result in cur:
            string_conexao = open('string_all_databases.txt', 'a')
            print(result, file = string_conexao)
        con.close()
        os.system("cat string_all_databases.txt | rev | cut -c4- | rev | cut -c 3- >> string_all_databases_ajustado.txt")
        f = open("string_all_databases_ajustado.txt")
        for line in f:
            try:
                con = cx_Oracle.connect('username/password@' + line)
                cur = con.cursor()
                cur.execute("alter user " + usuario + " identified by " + senha)
                print("Database: " + line + " - Senha do usuário " + usuario + " atualizada para: " + senha + " com sucesso!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                continue
            except cx_Oracle.DatabaseError as e:
                print("Erro no banco de dados: " + line, end='')
                print(str(e))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                continue
            sys.exit()
    else:
        print("Usuário não é um DBA")
        sys.exit()

# Execução de script - Todos databases:
def exec_script_consulta_all_databases():
    print("Digite o nome do usuário DBA para execução do script: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    usuario = input("User: ")
    if usuario.lower() in [dbas[key].lower() for key in dbas]:
        print("Removendo arquivos .txt da última execução...")
        print("Removendo arquivos .txt da última execução...")
        print("Removendo arquivos .txt da última execução...")
        os.system("rm script_string_all_databases.txt")
        os.system("rm script_string_all_databases_ajustado.txt")
        os.system("rm retorno_query.txt")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Verificando todos os databases...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        con = cx_Oracle.connect('username/password@host:port/service_name')
        cur = con.cursor()
        cur.execute("select distinct string_conexao from usernamer.username_databases where status = 'ACTIVE' and TIPO_AMBIENTE = 'PROD' and dbname not in ('DB1', 'DB2') and string_conexao is not null order by string_conexao")
        for result in cur:
            string_conexao = open('script_string_all_databases.txt', 'a')
            print(result, file = string_conexao)
        con.close()
        os.system("cat script_string_all_databases.txt | rev | cut -c4- | rev | cut -c 3- >> script_string_all_databases_ajustado.txt")
        print("Conectando-se em todos os databases e executando o script...")
        print("")
        os.system("sleep 3")
        os.system("clear")
        print("|--------------------------------------------------|")
        print("|--- Python Client Oracle - Developer - Sicredi ---|")
        print("|--------------------------------------------------|")
        print("|                   Release 3.0                    |")
        print("|--------------------------------------------------|")
        print("")
        print("Observações: ")
        print("- Digite a query sem ; no final.")
        print("- Coloque a query por extensa, sem quebra de linhas.")
        print("- O client não retorna as colunas, portanto sugere-se o uso de concatenação.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        sql = input("SQL> ")
        f = open("script_string_all_databases_ajustado.txt")
        for line in f:
            try:
                con = cx_Oracle.connect('username/password@' + line)
                cur = con.cursor()
                cur.execute(sql)
                print("Database: " + line + "Retorno:")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                    query_result = open('retorno_query.txt', 'a')
                    print("Database: " + line, row, file = query_result)
                    continue
            except cx_Oracle.DatabaseError as e:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Erro no banco de dados: " + line, end='')
                print(str(e))
                continue
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Verifique o arquivo retorno_query.txt com o resultado final.")
        sys.exit()
    else:
        print("Usuário não é um DBA")
        sys.exit()

# Listando strings - Todos os databases:
def list_strings_all_databases():
    print("Digite o nome do usuário DBA que vai verificar todas as strings dos bancos de dados de produção: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    usuario = input("User: ")
    if usuario.lower() in [dbas[key].lower() for key in dbas]:
        print("Removendo arquivos .txt da última execução...")
        print("Removendo arquivos .txt da última execução...")
        os.system("rm script_string_all_databases.txt")
        os.system("rm script_string_all_databases_ajustado.txt")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Verificando todos os databases-se no service_name...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Strings: ")
        con = cx_Oracle.connect('username/password@host:port/service_name')
        cur = con.cursor()
        cur.execute("select distinct string_conexao from usernamer.username_databases where status = 'ACTIVE' and TIPO_AMBIENTE = 'PROD' and string_conexao is not null order by string_conexao")
        for result in cur:
            string_conexao = open('script_string_all_databases.txt', 'a')
            print(result, file = string_conexao)
        con.close()
        os.system("cat script_string_all_databases.txt | rev | cut -c4- | rev | cut -c 3- >> script_string_all_databases_ajustado.txt")
        os.system("cat script_string_all_databases_ajustado.txt")
        sys.exit()
    else:
        print("Usuário não é um DBA")
        sys.exit()

# Menu escolha:
def exibir_menu():
    os.system("clear")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~ Menu - DBAs - Oracle ~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Digite 1 para reset de senha para algum database de produção.")
    print("2. Digite 2 para reset de senha em todos os databases de produção.")
    print("3. Digite 3 para execução de script de consulta em todos os databases de produção.")
    print("4. Digite 4 para listar as strings de todos os bancos de produção.")
    print("5. Digite 5 para sair.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def main():
    while True:
        exibir_menu()
        opcao = input("Opção: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if opcao == "1":
            reset_password_single_databases()
        elif opcao == "2":
            reset_password_all_databases()
        elif opcao == "3":
            exec_script_consulta_all_databases()
        elif opcao == "4":
            list_strings_all_databases()
        elif opcao == "5":
            print("Saindo.")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

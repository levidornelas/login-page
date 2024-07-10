import psycopg2
from urllib.parse import urlparse

# URL de conexão do banco (Railway)
DATABASE_URL = ""

# Extrair as informações de conexão da URL(database, usuário, password,etc)
url = urlparse(DATABASE_URL)

# Credenciais do banco de dados
DATABASE = url.path[1:]
USER = url.username
PASSWORD = url.password
HOST = url.hostname
PORT = url.port

def conect_to_database():
  try:
    conexao = psycopg2.connect(
                          database = DATABASE,
                          user = USER,
                          password = PASSWORD,
                          host = HOST,
                          port = PORT
    )


    connection = conexao.cursor()
    connection.execute('SELECT version();')
    db_versao = connection.fetchone()
    connection.close()
    conexao.close()

    return(f'Conectado ao PostgreSQL! versão: {db_versao}')
  
  except Exception as e:  
    return(f'Ocorreu um erro ao se conectar com o banco: {e}')

def register_users(username,senha):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        # Inserir dados do aluno
        inserir_sql = """INSERT INTO users (username,password) VALUES (%s, %s)"""
        gravar_insert = (username,senha)
        cursor.execute(inserir_sql, gravar_insert)
        connection.commit() #garantir que todas as alterações sejam refletidas permanentemente no banco.
        cursor.close()
        connection.close()
        return "Aluno cadastrado com sucesso!"
    
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")
    
def show_users():
  try:
      # Conexão ao banco de dados PostgreSQL
      connection = psycopg2.connect(
          database=DATABASE,
          user=USER,
          password=PASSWORD,
          host=HOST,
          port=PORT
        )
      
      cursor = connection.cursor()
      cursor.execute('select * from alunos')
      alunos = cursor.fetchall()
      cursor.close()
      connection.close()
      
      return alunos 
  
  except Exception as e:
     return(f'Ocorreu um erro: {e}')


import psycopg2

def check_login(username, senha):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        comando_sql = 'SELECT password FROM users WHERE username = %s'
        cursor.execute(comando_sql, (username,))
        resultado = cursor.fetchone()
        cursor.close()
        connection.close()

        if resultado is None:
            return 'Usuário não encontrado! Por favor tente novamente.'

        senha_salva = resultado[0]

        if senha_salva == senha:
            return 'Login realizado com sucesso!'
        else:
            return 'Erros de credenciais! Por favor tente novamente.'

    except Exception as e:
        print(f'Aconteceu um erro: {e}')
        return 'Ocorreu um erro ao tentar realizar o login.'

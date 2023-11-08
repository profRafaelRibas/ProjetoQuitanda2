from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql
import uuid

app = Flask(__name__)
app.secret_key = "quitandadozezinho"

usuario = "usuario"
senha = "senha"
login = False

# Função para verificar sessão
def verifica_sessao():
    if "login" in session and session["login"]:
        return True
    else:
        return False

# Conexão com o banco de dados
def conecta_database():
    conexao = sql.connect("db_quitanda.db")
    conexao.row_factory = sql.Row
    return conexao

# Iniciar o banco de dados
def iniciar_db():
    conexao = conecta_database()
    with app.open_resource('esquema.sql', mode='r') as comandos:
        conexao.cursor().executescript(comandos.read())
    conexao.commit()
    conexao.close()

# Rota da página inicial
@app.route("/")
def index():
    iniciar_db()
    conexao = conecta_database()
    produtos = conexao.execute('select * from produtos order by id_prod desc').fetchall()
    conexao.close()
    title="Home"
    return render_template("home.html", produtos=produtos, title=title)

# Final do codigo - executando o servidor
app.run(debug=True)
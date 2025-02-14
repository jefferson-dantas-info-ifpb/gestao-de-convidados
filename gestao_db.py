import sqlite3 as sqlite
from helpers import tupla_para_usuario


def cria_tabela():
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


cria_tabela()


def inserir_usuario(nome, email, senha):
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
        """,
        (nome, email, senha),
    )
    conn.commit()
    conn.close()
    return obter_usuario_por_id(cursor.lastrowid)


def atualizar_senha_usuario(id, senha):
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE usuarios SET senha = ? WHERE id = ?
        """,
        (senha, id),
    )
    conn.commit()
    conn.close()


def listar_usuarios():
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios ORDER BY id DESC
        """
    )
    dados = cursor.fetchall()
    usuarios = list(map(tupla_para_usuario, dados))
    conn.close()
    return usuarios


def obter_usuario_por_id(valor):
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios WHERE id = ? LIMIT 1
        """,
        (valor,),
    )
    dados = cursor.fetchall()
    conn.close()
    if len(dados) == 0:
        return None
    else:
        return list(map(tupla_para_usuario, dados))[0]


def obter_usuario_por_nome(valor):
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios WHERE nome = ? LIMIT 1
        """,
        (valor,),
    )
    dados = cursor.fetchall()
    conn.close()
    if len(dados) == 0:
        return None
    else:
        return list(map(tupla_para_usuario, dados))[0]


def obter_usuario_por_email(valor):
    conn = sqlite.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios WHERE email = ? LIMIT 1
        """,
        (valor,),
    )
    dados = cursor.fetchall()
    conn.close()
    if len(dados) == 0:
        return None
    else:
        return list(map(tupla_para_usuario, dados))[0]

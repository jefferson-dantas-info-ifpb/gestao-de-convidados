from flask import Flask, render_template, request, flash
from convidados import (
    Convidado,
    convidados,
    procurar_convidado_pelo_email,
    procurar_convidado_pelo_nome,
)

app = Flask(__name__)
app.secret_key = "fwi7kLYr7g9vzGZyYC9wxb21jiDoxe90"


@app.get("/")
def home():
    return render_template("index.html", title="Verificar convidado na lista")


@app.post("/")
def verificar():
    nome = request.form["nome"]

    convidado = procurar_convidado_pelo_nome(nome)

    if convidado is not None:
        flash(f'O convidado "{nome}" está na lista!', "info")
    else:
        flash(f'O convidado "{nome}" NÃO está na lista!', "error")

    return render_template(
        "index.html", convidado=nome, title="Verificar convidado na lista"
    )


@app.get("/login")
def login_page():
    return render_template("login.html", title="Login")


@app.post("/login")
def login():
    email = request.form["email"]
    senha = request.form["senha"]

    convidado = procurar_convidado_pelo_email(email)

    if convidado is None:
        flash("O convidado não está na lista", "error")
        return render_template("login.html", email=email, title="Login")

    if convidado.senha == senha:
        return render_template("convidado.html", convidado=convidado, title="Convidado")
    else:
        flash("Senha incorreta", "error")
        return render_template("login.html", email=email, title="Login")


@app.get("/cadastrar")
def cadastrar_page():
    return render_template("cadastrar.html", title="Cadastrar convidado")


@app.post("/cadastrar")
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]

    convidado = procurar_convidado_pelo_email(email)

    if convidado is not None:
        flash("Um convidado com este e-mail já está cadastrado", "error")
        return render_template("cadastrar.html", title="Cadastrar convidado")

    novo_convidado = Convidado(nome, email, senha)
    convidados.append(novo_convidado)
    flash("Convidado cadastrado com sucesso!", "info")
    return render_template(
        "convidado.html", convidado=novo_convidado, title="Convidado"
    )


app.run(debug=True)

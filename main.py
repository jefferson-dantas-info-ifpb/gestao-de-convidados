import gestao_db
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "fwi7kLYr7g9vzGZyYC9wxb21jiDoxe90"


@app.get("/")
def home():
    return render_template("index.html", title="Verificar convidado na lista")


@app.post("/")
def verificar():
    nome = request.form["nome"]

    convidado = gestao_db.obter_usuario_por_nome(nome)

    if convidado is not None:
        flash(f'"{nome}" está na lista de convidados!', "info")
    else:
        flash(f'"{nome}" NÃO está na lista de convidados!', "error")

    return render_template(
        "index.html", convidado=nome, title="Verificar convidado na lista"
    )


@app.get("/lista")
def lista():
    convidados = gestao_db.listar_usuarios()
    return render_template(
        "lista.html", convidados=convidados, title="Lista de convidados"
    )


@app.get("/login")
def login_page():
    return render_template("login.html", title="Login")


@app.post("/login")
def login():
    email = request.form["email"]
    senha = request.form["senha"]

    convidado = gestao_db.obter_usuario_por_email(email)

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

    convidado = gestao_db.obter_usuario_por_email(email)

    if convidado is not None:
        flash("Um convidado com este e-mail já está cadastrado", "error")
        return render_template("cadastrar.html", title="Cadastrar convidado")

    novo_convidado = gestao_db.inserir_usuario(nome, email, senha)
    flash("Convidado cadastrado com sucesso!", "info")
    return render_template(
        "convidado.html", convidado=novo_convidado, title="Convidado"
    )


@app.post("/excluir")
def excluir():
    id = request.form["id"]
    gestao_db.excluir_usuario(id)
    flash("Usuário excluído com sucesso!", "info")
    return redirect("/lista")


@app.get("/recuperar_senha")
def recuperar_senha_page():
    return render_template("recuperar_senha.html", title="Recuperar senha")


@app.post("/recuperar_senha")
def recuperar_senha():
    email = request.form["email"]
    nome = request.form["nome"]
    senha = request.form["senha"]

    convidado = gestao_db.obter_usuario_por_email(email)

    if convidado is None or convidado.nome.lower() != nome.lower():
        flash("O e-mail não existe ou o nome do convidado não está correto", "error")
        return render_template(
            "recuperar_senha.html", email=email, nome=nome, title="Recuperar senha"
        )

    gestao_db.atualizar_senha_usuario(convidado.id, senha)
    flash("Senha alterada com sucesso!", "info")
    return redirect("/login")


app.run(debug=True)

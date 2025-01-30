from flask import Flask, render_template, request, flash
from convidados import (
    Convidado,
    convidados,
    procurar_convidado_pelo_email,
    procurar_convidado_pelo_nome,
)

app = Flask(__name__)
app.secret_key = "fwi7kLYr7g9vzGZyYC9wxb21jiDoxe90"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form["nome"]

        convidado = procurar_convidado_pelo_nome(nome)

        if convidado is not None:
            flash(f'O convidado "{nome}" está na lista!', "info")
        else:
            flash(f'O convidado "{nome}" NÃO está na lista!', "error")

        return render_template(
            "index.html", convidado=nome, title="Verificar convidado na lista"
        )
    else:
        return render_template("index.html", title="Verificar convidado na lista")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        convidado = procurar_convidado_pelo_email(email)

        if convidado is None:
            flash("O convidado não está na lista", "error")
            return render_template("login.html", email=email, title="Login")

        if convidado.senha == senha:
            return render_template(
                "convidado.html", convidado=convidado, title="Convidado"
            )
        else:
            flash("Senha incorreta", "error")
            return render_template("login.html", email=email, title="Login")
    else:
        return render_template("login.html", title="Login")


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        convidado = procurar_convidado_pelo_email(email)

        if convidado is not None:
            flash("Um convidado com este e-mail já está cadastrado", "error")
            return render_template("convidado.html", title="Convidado")

        novo_convidado = Convidado(nome, email, senha)
        convidados.append(novo_convidado)
        flash("Convidado cadastrado com sucesso!", "info")
        return render_template(
            "convidado.html", convidado=novo_convidado, title="Convidado"
        )
    else:
        return render_template("cadastrar.html", title="Cadastrar convidado")


app.run(debug=True)

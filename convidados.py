class Convidado:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


convidados = [
    Convidado("João", "joao@email.com", "joao123"),
    Convidado("Maria", "maria@email.com", "maria123"),
]


def procurar_convidado_pelo_nome(nome):
    for convidado in convidados:
        if convidado.nome.lower() == nome.lower():
            return convidado


def procurar_convidado_pelo_email(email):
    for convidado in convidados:
        if convidado.email.lower() == email.lower():
            return convidado

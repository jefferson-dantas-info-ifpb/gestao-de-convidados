class Convidado:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

def tupla_para_usuario(tupla):
    id, nome, email, senha = tupla
    return Convidado(id, nome, email, senha)

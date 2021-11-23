class Usuario_informacao_exception(Exception):
    ...


class Usuario_nao_encontrado(Usuario_informacao_exception):
    def __init__(self):
        self.status_code = 404
        self.detail = "Informações do Usuario não encontrada"


class Usuario_ja_existente(Usuario_informacao_exception):
    def __init__(self):
        self.status_code = 409
        self.detail = "Usuario já existente"


class Endereco_informacao_exception(Exception):
    ...


class Endereco_nao_encontrado(Endereco_informacao_exception):
    def __init__(self):
        self.status_code = 404
        self.detail = "Endereço não encontrado"


class Endereco_ja_existente(Endereco_informacao_exception):
    def __init__(self):
        self.status_code = 409
        self.detail = "Endereço ja existente"



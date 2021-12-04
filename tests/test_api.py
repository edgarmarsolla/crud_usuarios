from httpx import get, post, put, delete

url_ls_usuarios = 'https://projetocrudusuario.herokuapp.com/usuarios'
url_ls_enderecos = 'https://projetocrudusuario.herokuapp.com/endereco'
url_ls_usuario_por_id = 'https://projetocrudusuario.herokuapp.com/usuario/2'
url_ls_usuario_por_id2 = 'https://projetocrudusuario.herokuapp.com/usuario/123456'
url_ls_endereco_por_id = 'https://projetocrudusuario.herokuapp.com/endereco/3'
url_ls_endereco_por_id2 = 'https://projetocrudusuario.herokuapp.com/endereco/9789645'
url_add_usuario = 'https://projetocrudusuario.herokuapp.com/addusuarios'
url_add_endereco = 'https://projetocrudusuario.herokuapp.com/addendereco'
urls_put_usuairo = 'https://projetocrudusuario.herokuapp.com/usuarioput/3'
urls_put_usuairo2 = 'https://projetocrudusuario.herokuapp.com/usuarioput/78952'
urls_put_endereco = 'https://projetocrudusuario.herokuapp.com/enderecoput/5'
urls_del_endereco = 'https://projetocrudusuario.herokuapp.com/enderecodel/5'
urls_del_usuario =  'https://projetocrudusuario.herokuapp.com/usuariodel/3'


def test_get_todos_usuarios_tem_que_devolver_200():
    resquest = get(url_ls_usuarios)
    assert resquest.status_code == 200


def test_get_todos_enderecos_tem_que_devolver_200():
    resquest = get(url_ls_enderecos)
    assert resquest.status_code == 200


def test_get_usuario_pelo_id_tem_que_devolver_200():
    resquest = get(url_ls_usuario_por_id)
    assert resquest.status_code == 200


def test_get_usuario_pelo_id_tem_que_devolver_404():
    resquest = get(url_ls_usuario_por_id2)
    assert resquest.status_code == 404


def test_get_endereco_pelo_id_tem_que_devolver_200():
    resquest = get(url_ls_endereco_por_id)
    assert resquest.status_code == 200


def test_get_endereco_pelo_id_tem_que_devolver_404():
    resquest = get(url_ls_endereco_por_id2)
    assert resquest.status_code == 404


#def test_post_cria_o_usuario_tendo_que_devolver_200():
    #add_usuario = {"usuario_nome": "Karina", "usuario_email": "ka@gmail.com", "usuario_cpf": "222.222.222-22", "usuario_pis": "22222222222", "usuario_senha": "123"}
    #resquest = post(url_add_usuario, json=add_usuario)
    #assert resquest.status_code == 200


#def test_post_cria_o_usuario_tendo_que_devolver_409_pois_esse_usuario_ja_existe():
#    add_usuario = {"usuario_nome": "Maria", "usuario_email": "ka@gmail.com", "usuario_cpf": "222.222.222-22", "usuario_pis": "22222222222", "usuario_senha": "123"}
#    resquest = post(url_add_usuario, json=add_usuario)
#    assert resquest.status_code == 409


#def test_post_cria_o_endereco_tendo_que_devolver_200():
#    add_endereco = {"endereco_pais": "EUA",
#                    "endereco_estado": "Texas",
#                    "endereco_municipio": "Houston",
#                    "endereco_cep": "xxxxxx-xxx",
#                    "endereco_logradouro": "Rua Oi",
#                    "endereco_numero_da_casa": "1000",
#                    "endereco_complemento": "123",
#                    "endereco_usuario": 3}
#
#    request = post(url_add_endereco, json=add_endereco)
#    assert request.status_code == 200

#def test_put_atualiza_o_usuario_tendo_que_devolver_200():
#    put_usuario = {"usuario_nome": "Maria",
#                   "usuario_email": "ka@gmail.com",
#                   "usuario_cpf": "222.222.222-22",
#                   "usuario_pis": "22222222222",
#                   "usuario_senha": "123"}
#    resquest = put(urls_put_usuairo, json=put_usuario)
#    assert resquest.status_code == 200


def test_put_atualiza_o_usuario_tendo_que_devolver_404():
    put_usuario = {"usuario_nome": "Maria",
                   "usuario_email": "ka@gmail.com",
                   "usuario_cpf": "222.222.222-22",
                   "usuario_pis": "22222222222",
                   "usuario_senha": "123"}
    resquest = put(urls_put_usuairo2, json=put_usuario)
    assert resquest.status_code == 404


#def test_put_atualiza_o_endereco_tendo_que_devolver_200():
#    put_endereco = {"endereco_pais": "EUA",
#                    "endereco_estado": "Texas",
#                    "endereco_municipio": "Houston",
#                    "endereco_cep": "xxxxxx-xxx",
#                    "endereco_logradouro": "Rua Oi",
#                    "endereco_numero_da_casa": "1000",
#                    "endereco_complemento": "123",
#                    "endereco_usuario": 3}

#    request = put(urls_put_endereco, json=put_endereco)
#    assert request.status_code == 200


#def test_delete_deletando_o_endereco_tendo_que_devolver_200():

#    request = delete(urls_del_endereco)
#   assert request.status_code == 200

def test_delete_deletando_o_endereco_tendo_que_devolver_404():

    request = delete(urls_del_endereco)
    assert request.status_code == 404

#def test_delete_deletando_o_usuario_tendo_que_devolver_200():

#    request = delete(urls_del_usuario)
#    assert request.status_code == 200


def test_delete_deletando_o_usuario_tendo_que_devolver_404():

    request = delete(urls_del_usuario)
    assert request.status_code == 404
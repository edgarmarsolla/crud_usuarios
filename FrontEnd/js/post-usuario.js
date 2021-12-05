async function fazPost(url, body) {
    console.log("Body", body)
    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
        },
        body: JSON.stringify(body),
    })
    
    let resposta = await response.json()
    
    
    return resposta

}

async function post_endereco(usuario_id) {

    console.log(usuario_id)

    let url = "https://projetocrudusuario.herokuapp.com/addendereco"
    let pais = document.getElementById("endereco_pais").value
    let estado = document.getElementById("endereco_estado").value
    let municipio = document.getElementById("endereco_municipio").value
    let cep = document.getElementById("endereco_cep").value
    let logradouro = document.getElementById("endereco_logradouro").value
    let numero = document.getElementById("endereco_numero_da_casa").value
    let complemento = document.getElementById("endereco_complemento").value
    let idusuario = usuario_id

    body = {        
        "endereco_pais": pais,
        "endereco_estado": estado,
        "endereco_municipio": municipio,
        "endereco_cep": cep,
        "endereco_logradouro": logradouro,
        "endereco_numero_da_casa": numero,
        "endereco_complemento": complemento,
        "endereco_usuario": idusuario
    }

    await fazPost(url, body);


}

async function cadastraUsuario() {
    event.preventDefault();
    let url = "https://projetocrudusuario.herokuapp.com/addusuarios"
    let nome = document.getElementById("usuario_nome").value
    let email = document.getElementById("usuario_email").value
    let cpf = document.getElementById("usuario_cpf").value
    let pis = document.getElementById("usuario_pis").value
    let senha = document.getElementById("usuario_senha").value
    let senha2 = document.getElementById("usuario_senha2").value
    console.log(nome)
    console.log(email)
    console.log(cpf)
    console.log(pis)
    console.log(senha)
    console.log(senha2)
    
    if (senha == senha2){
        body = {
            "usuario_nome": nome,
            "usuario_email": email,
            "usuario_cpf": cpf,
            "usuario_pis": pis,
            "usuario_senha": senha    
        }

        let teste = await fazPost(url, body);

        console.log(teste.usuario_id)
        let id = teste.usuario_id

        await post_endereco(id);


    }else{
        return alert("Senha diferente de Confirma Senha");
    }


    
    
    
}


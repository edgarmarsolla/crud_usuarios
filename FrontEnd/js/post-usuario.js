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

async function cadastraUsuario() {
    event.preventDefault();
    let url = "http://127.0.0.1:8000/addusuarios"
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


    }else{
        return alert("Senha diferente de Confirma Senha");
    }

    
    
    
}
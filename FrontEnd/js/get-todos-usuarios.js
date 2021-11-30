function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send()
    return request.responseText
}

function criaLinha(usuario) {
    let linha = document.createElement("tr");
    let tdId = document.createElement("td");
    let tdnome = document.createElement("td");
    let tdemail = document.createElement("td");
    let tdcpf = document.createElement("td");
    let tdpis = document.createElement("td");
    let tdsenha = document.createElement("td");

    tdId.innerHTML = usuario.usuario_id
    tdnome.innerHTML = usuario.usuario_nome
    tdemail.innerHTML = usuario.usuario_email
    tdcpf.innerHTML = usuario.usuario_cpf
    tdpis.innerHTML = usuario.usuario_pis
    tdsenha.innerHTML = usuario.usuario_senha

    linha.appendChild(tdId);
    linha.appendChild(tdnome);
    linha.appendChild(tdemail);
    linha.appendChild(tdcpf);
    linha.appendChild(tdpis);
    linha.appendChild(tdsenha);

    return linha;


}

function main() {
    let json = fazGet("http://127.0.0.1:8000/usuarios");
    let dados = JSON.parse(json);
    let tabela = document.getElementById("usuario");
    console.log(dados);
    let limit = dados.limit;
    let usuarios = dados.data;
    usuarios.forEach(element => {
        let linha = criaLinha(element);
        tabela.appendChild(linha);
    });
      

}

main()
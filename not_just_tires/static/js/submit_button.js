function submitButton() {

    let p = document.createElement('p');
    let button = document.createElement('button')

    button.id = "submit-button"
    button.type = "submit"
    button.className = "form-control"
    button.innerText = "Submeter!"

    p.appendChild(button)

    document.getElementById("main-div").appendChild(p)

}

submitButton()

document.getElementById("submit-button").onclick = function() {
        
    // var form_data = {
    //     "comprador": document.getElementById('form-comprador').value,
    //     "tipo_transacao": document.getElementById('form-tipo_transacao').value,
    //     "tipo_pneu": document.getElementById('form-tipo_pneu').value,
    //     "quantidade": document.getElementById('form-quantidade').value,
    //     "preco_unitario": document.getElementById('form-preco_unitario').value,
    //     "data": document.getElementById('form-data').value,
    //     "observacoes": document.getElementById('form-observacoes').value
    // }

    document.getElementById("main-form").submit()

}
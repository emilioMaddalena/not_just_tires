function printTransactions(trans) {
    
    for (let step = 0; step < trans.length; step++) {
    
        // Create, fill and post one card per transaction
        let card = document.createElement('div');
        fillTransCard(card, trans[step])
        document.getElementById("main-div").appendChild(card);

    }

}

function nameToString(varObj) {
    return Object.keys(varObj)[0];
}

function formatDateString(date) {
    // Takes a data in the form dd/mm/yyyy and produces yyyy-mm-dd
    return [date.slice(6,10), date.slice(3,5), date.slice(0,2)].join('-');
}

function fillTransCard(card, trans) {

    const { id, comprador, data, observacoes, preco_unitario, quantidade, tipo_pneu, tipo_transacao } = trans;
    
    let myQueryString = {
        'field_ID': id,
        'field_comprador': comprador,
        'field_tipo_transacao': tipo_transacao,
        'field_tipo_pneu': tipo_pneu,
        'field_quantidade': quantidade,
        'field_preco_unitario': preco_unitario,
        'field_data': formatDateString(data),
        'field_observacoes': observacoes
    }

    card.className = 'alert alert-primary';
    
    // Transac info

    let msg = document.createElement('div')
    msg.style.marginBottom = '10px'
    msg.style.fontWeight = 'bold'
    msg.innerText = `${tipo_transacao}: ${data}`
    card.appendChild(msg)
    
    let info1 = document.createElement('div')
    info1.innerText = `Comprador: ${comprador}`
    card.appendChild(info1)   
    
    let tipo = document.createElement('div')
    tipo.innerText = `Tipo de pneu: ${tipo_pneu}`
    card.appendChild(tipo)   

    let info2 = document.createElement('div')
    info2.innerText = `Total: R$ ${quantidade * preco_unitario} \xa0 (${quantidade} pneus de ${preco_unitario} reais).`
    card.appendChild(info2)    

    // Buttons

    let div_buttons = document.createElement('div')
    div_buttons.style.marginTop = '10px'
    
    let mod_button = document.createElement('button')
    mod_button.className = 'btn btn-warning'
    mod_button.style.marginRight = '10px'
    mod_button.innerText = 'Modificar'
    mod_button.onclick = function() {

        window.location.href = "./form?" + new URLSearchParams(myQueryString)

    }
    div_buttons.appendChild(mod_button)

    let del_button = document.createElement('button')
    del_button.className = 'btn btn-danger';
    del_button.innerText = 'Deletar'
    del_button.onclick = function() {
        
        // Delete everything
        // let password = prompt("Enter the deletion password:", "123456");
        // fetch('./clear-DB', { method: 'POST', body: password})
        //     .then(window.location.reload());

        fetch('./del-trans', { method: 'POST', body: id})
            .then(window.location.reload());
            
        // alert("DELETE BUTTON WAS CLICKED!")

    }
    div_buttons.appendChild(del_button)

    card.appendChild(div_buttons)
}

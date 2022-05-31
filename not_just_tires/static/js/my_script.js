function printTransactions(trans) {
    
    for (let step = 0; step < trans.length; step++) {
    
        // Create, fill and post one card per transaction
        let card = document.createElement('div');
        fillTransCard(card, trans[step])
        document.getElementById("main-div").appendChild(card);

    }

}

function fillTransCard(card, trans) {

    const { ID, comprador, data, observacoes, preco_unitario, quantidade, tipo_pneu, tipo_transacao } = trans;

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

        //fetch(['./form/', ID].join(''), { method: 'GET'})
        window.location.href = ['./form/', ID].join('');

    }
    div_buttons.appendChild(mod_button)

    let del_button = document.createElement('button')
    del_button.className = 'btn btn-danger';
    del_button.innerText = 'Deletar'
    del_button.onclick = function() {
        
        fetch('./del-trans', { method: 'POST', body: ID})
            .then(window.location.reload());
            
        // alert("DELETE BUTTON WAS CLICKED!")

    }
    div_buttons.appendChild(del_button)

    card.appendChild(div_buttons)
}

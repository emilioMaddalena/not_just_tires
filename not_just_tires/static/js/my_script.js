// import bootstrap symbols here?

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
    card.innerText = comprador;

}

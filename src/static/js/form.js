{/* <label style="color:red;">*</label><label>Tipo de pneu:</label>
<select class="form-control" id="field_tipo_pneu" name="tipo_pneu">
    <option style="display:none"> -- Selecionar -- </option>
    <option>Passeio A</option>
    <option>Passeio B</option>
    <option>Caminhonete</option>
    <option>Caminhão</option>
    <option>Carcaça</option>
</select>
</div>
<div class="form-group">
<label style="color:red;">*</label><label>Quantidade:</label>
<p><input class="form-control" id="field_quantidade" type="number" name="quantidade" min="1" /></p>
</div>
<div class="form-group">
<label style="color:red;">*</label><label>Preco unitário:</label>
<p><input class="form-control" id="field_preco_unitario" type="number" name="preco_unitario" min="0" step="0.01" /></p>
</div> */}

function add_item(data) {

    let items_list = document.getElementById('items');
    
    let tipo_pneu = setup_tipo(items_list, 0);
    let quantidade = setup_quantidade(items_list, 0);

    items_list.appendChild(tipo_pneu);
    items_list.appendChild(quantidade);
}

function setup_tipo(items_list, counter){
    
    let names = [' -- Selecionar -- ', 
                'Passeio A', 
                'Passeio B', 
                'Caminhonete', 
                'Caminhão', 
                'Carcaça'];

    items_list.insertAdjacentHTML(
        'beforeend',
        '<label style="color:red;">*</label><label>Tipo de pneu:</label>'
    );

    // Create Field
    let tipo_pneu = document.createElement('select');
    tipo_pneu.className = 'form-control';
    tipo_pneu.id = 'field_tipo_pneu';

    // Create and append options
    for (let name of names){        
        let opt = document.createElement('option');
        opt.innerText = name;
        if (name == ' -- Selecionar -- '){
            opt.style = "display:none";
        }
        tipo_pneu.appendChild(opt);
    }

    return tipo_pneu;
}


function setup_quantidade(items_list, counter){

    items_list.insertAdjacentHTML(
        'beforeend',
        '<label style="color:red;">*</label><label>Quantidade:</label>'
    );

    let quantidade = document.createElement('input');
    quantidade.className = 'form-control';
    quantidade.id = 'field_quantidade';
    quantidade.min = '1';
    quantidade.type = 'number';

    return quantidade;
}
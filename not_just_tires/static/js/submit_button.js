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
    
    document.getElementById("main-form").submit();

}

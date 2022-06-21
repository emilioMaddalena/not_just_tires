let alert_message = "A data não deve pode ser no futuro!"

function checkTime(field_id) {

    // Check if the entered date is not in the furute
    var today = new Date().toJSON().slice(0,10).replace(/-/g,'-');
    var input = document.getElementById(field_id).value;

    if ( Date.parse(input) > Date.parse(today) ){
        
        console.log("It's the future!");
        alert(alert_message);
        return false

    } else {

        console.log("It's the present or past!");
        return true

    }

}
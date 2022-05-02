def check_mandatory_fields(form):
    '''
    Check if all mandatory fields were filled upon the form submission.
    '''
    optional = ["observacoes"]
    
    # Catching empty fields that are mandatory
    for item in form: 
        if (not form[item]) and (item not in optional): 
            return False
    
    return True
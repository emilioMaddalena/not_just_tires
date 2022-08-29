import json

def load_transactions(path, num, head="0"):
    '''
    Load a specific num of transactions from the json file
    '''
    with open(path) as f:
        
        data = json.load(f)
        data["transacoes"] = data["transacoes"][:num]
        return data

def formatIndividualDate(datetime):
    
    if (len(str(datetime.month)) == 1):
        return ''.join([str(datetime.day), '/0', str(datetime.month), '/', str(datetime.year)])
    
    else:
        return ''.join([str(datetime.day), '/', str(datetime.month), '/', str(datetime.year)])

def formatDictDates(myDict):
    
    for transac in myDict['transacoes']:
        transac['data'] = formatIndividualDate(transac['data'])
        
    return

def sql_to_dict(db_obj):
    
    db_obj_dict = [el.__dict__ for el in db_obj]
    for el in db_obj_dict: del el['_sa_instance_state']
    out_dict = {"transacoes": db_obj_dict}
    formatDictDates(out_dict)
    
    return out_dict
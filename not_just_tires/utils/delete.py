import json
    
def delete_transaction(path, del_id):
    
    with open(path, 'r') as f:
        
        data = json.load(f)
        for pos in range(len(data["transacoes"])):
            
            current_id = data["transacoes"][pos]['ID']
            
            if str(current_id) == str(del_id): 
                del data["transacoes"][pos]
                break

    with open(path, 'w') as f:
        
        json.dump(data, f)
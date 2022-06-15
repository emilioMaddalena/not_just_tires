import json
import uuid
    
def store_in_json(path, data):
    '''
    Store a transaction in the json file. If the ID is not given, create a unique new ID for it.
    '''
    data = data.to_dict()
    
    with open(path, 'r') as f:
        
        current_contents = json.load(f)
    
    with open(path, 'w') as f:
        
        id = data['id']
         
        # generate unique ID and append to the data
        if not id: 
            print("\nCREATING A NEW ID!\n")
            data['id'] = str(uuid.uuid4())
            current_contents['transacoes'].append(data)

        # use the provided ID to delete the existing entry
        else: 
            print("\nID ALREADY SENT, REAPLCING OLD TRANSAC!\n")
            for pos in range(len(current_contents['transacoes'])):
                
                if current_contents['transacoes'][pos]['id'] == id: 
                    del current_contents["transacoes"][pos]
                    break
            
            current_contents['transacoes'].insert(pos, data)

        # write back
        json.dump(current_contents, f)
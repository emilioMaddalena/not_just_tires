import json
import uuid
    
def store_in_json(path, data, id):
    '''
    Store a transaction in the json file. If the ID is not given, create a unique new ID for it.
    '''
    data = data.to_dict()
    
    with open(path, 'r') as f:
        
        current_contents = json.load(f)
    
    with open(path, 'w') as f:
        
        # generate unique ID and append to the data
        if not id: 
            data['ID'] = str(uuid.uuid4())
        
        # use the provided ID to delete the existing entry
        else: 
            data['ID'] = str(id)
            for pos in range(len(current_contents['transacoes'])):
                if current_contents['transacoes'][pos]['ID'] == id: 
                    del current_contents["transacoes"][pos]
                    break
        
        # append the data onto the json contents and write back
        current_contents['transacoes'].append(data)
        json.dump(current_contents, f)
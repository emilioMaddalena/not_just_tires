import json
import uuid
    
def store_in_json(path, data):
    
    data = data.to_dict()
    
    with open(path, 'r') as f:
        
        current_contents = json.load(f)
    
    with open(path, 'w') as f:
        
        # generate unique ID and append to the data
        data['ID'] = str(uuid.uuid4())
        
        # append the data onto the json contents and write back
        current_contents['transacoes'].append(data)
        json.dump(current_contents, f)
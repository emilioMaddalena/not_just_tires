import json

def load_transactions(path, num, head="0"):
    '''
    Load a specific num of transactions from the json file
    '''
    with open(path) as f:
        
        data = json.load(f)
        data["transacoes"] = data["transacoes"][:num]
        return data
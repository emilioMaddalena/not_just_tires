import json

def get_ids(num, head):
    return (int(head), int(head)+int(num))
    
def load_transactions(num, head="0"):
    
    # idHead, idTail = get_ids(num, head)
    
    with open("data/test-data.json") as f:
        
        data = json.load(f)
        data["transacoes"] = data["transacoes"][:num]
        return data
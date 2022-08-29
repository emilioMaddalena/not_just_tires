def generate_report(data):
    
    report = {'entradas': compute_entradas(data),
              'saidas': compute_saidas(data),
              'recusa': compute_recusas(data),
              'balanco_estoque': compute_balanco_estoque(data)}
    
    return report

def compute_entradas(data):
    
    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Venda' else 0;
        total_global += total_transac

    return total_global

def compute_saidas(data):

    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Compra' else 0;
        total_global += total_transac

    return total_global

def compute_recusas(data):
    
    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Recusa' else 0;
        total_global += total_transac

    return total_global


def compute_balanco_estoque(data):
    pass
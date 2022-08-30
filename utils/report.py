def generate_report(data):
    
    report = {'valor_vendas': compute_valor_vendas(data),
              'valor_compras': compute_valor_compras(data),
              'num_vendas': compute_num_vendas(data),
              'num_compras': compute_num_compras(data),
              'recusa': compute_recusas(data),
              'balanco_estoque': compute_balanco_estoque(data)}
    
    return report

def compute_valor_vendas(data):
    
    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Venda' else 0;
        total_global += total_transac

    return total_global

def compute_valor_compras(data):

    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Compra' else 0;
        total_global += total_transac

    return total_global

def compute_num_vendas(data):
    
    num = 0;
    for transac in data['transacoes']:
        num = num + 1 if transac['tipo_transacao'] == 'Venda' else num

    return num

def compute_num_compras(data):
    
    num = 0;
    for transac in data['transacoes']:
        num = num + 1 if transac['tipo_transacao'] == 'Compra' else num

    return num

def compute_recusas(data):
    
    total_global = 0;
    for transac in data['transacoes']:
        total_transac = transac['preco_unitario']*transac['quantidade'] if transac['tipo_transacao'] == 'Recusa' else 0;
        total_global += total_transac

    return total_global


def compute_balanco_estoque(data):
    pass
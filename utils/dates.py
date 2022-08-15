def formatIndividualDate(datetime):
    
    if (len(str(datetime.month)) == 1):
        return ''.join([str(datetime.day), '/0', str(datetime.month), '/', str(datetime.year)])
    
    else:
        return ''.join([str(datetime.day), '/', str(datetime.month), '/', str(datetime.year)])

def formatDictDates(myDict):
    
    for transac in myDict['transacoes']:
        transac['data'] = formatIndividualDate(transac['data'])
        
    return
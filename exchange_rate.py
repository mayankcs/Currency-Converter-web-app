import requests

def get_exchange_rate(source,target,date=0):

    ''' this funtion return exchange rate for 
        source currency to target currency 
        
        Source is the currency code of source currency
        Target is the currency code of Target currency
        date is set to zero by default, but if specified then exchange rate
        of that date would be returned

    return type is list containing exchange rate and date'''

    if date==0:
        url = 'https://api.exchangerate.host/convert?from=%s&to=%s'%(source,target)
    else:    
        url = 'https://api.exchangerate.host/convert?from=%s&to=%s&date=%s'%(source,target,date)

    response = requests.get(url)
    data = response.json()
    return [data['info']['rate'],data['date']]



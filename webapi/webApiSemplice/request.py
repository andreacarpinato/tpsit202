import requests

URL= "http://127.0.0.1:5000/api/v1/resources/books"

PARAMS={'id':1}

#invio richiesta
r=requests.get(url=URL,params=PARAMS)
#estrazione dati
data=r.json
print(data)
from tinydb import TinyDB, Query
import requests
import json

def get_data(id):
    response = get_name(id).copy()
    response.update({"current_price": get_price(id)})
    response["id"]=id
    return  response

def get_name(id):
    payload = {'fields': 'description', 'id_type': 'TCIN','key':'43cJWpLjH8Z8oR18KdrZDBKAgLLQKJjz'}
    r = json.loads(requests.get('https://api.target.com/products/v3/{0}'.format(id), params=payload))
    return {"name":r["description"]["name"]} #considering name is in description

def get_price(id):
    db = TinyDB('data.json')
    try:
        query = Query()
        response = db.search(query.id==id)[0]
    except Exception as e:
        response={}
    return  response["current_price"]
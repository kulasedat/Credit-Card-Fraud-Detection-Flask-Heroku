import requests

url = 'http://localhost:5000/predict_api'


request.get( {timeout: 1500})

r = requests.post(url,json={'V1':-0.1,'V10':-1.4,'V11':-0.9,'V13':-1.8,	'V19':0.6,	
                            'V22':0.1,	'V24':-2.6 
})

print(r.json())

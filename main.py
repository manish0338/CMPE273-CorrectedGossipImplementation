import requests,time

message = {"time": (time.time()+7.0),"ctime": (time.time()+5.0 + 2.0)}

requests.post(url="http://localhost:5000/api", json=message)

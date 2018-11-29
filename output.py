import requests

csum = 0
isum = 0
ccsum = 0

for i in range(5000, 5020):
    r = requests.get(url="http://localhost:"+str(i)+"/api")
    csum = csum + int(r.json()['count'])
    isum = isum + int(r.json()['icount'])
    #ccsum = ccsum + int(r.json()['ccount'])

print(csum)
print(isum)
print(ccsum)
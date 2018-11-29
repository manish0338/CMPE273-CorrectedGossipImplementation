from flask import Flask, request
from flask_restful import Resource, Api
import time, random, requests, threading, sys

app = Flask(__name__)
api = Api(app)

count = 0
message = ""
icount = 0
ccount = 0
infected = False


class GossipNode(Resource):

	def get(self):
		global count
		return {"count": count,"icount":icount,"ccount":ccount}

	def post(self):
		global message
		global infected
		
		message = request.json
		
		if(infected == False):
			global icount
			icount = 1
			infected = True
			pollThread = threading.Thread(target=gossip,name = "Polling Thread")
			pollThread.daemon = True
			pollThread.start()
		
		return "",201
		
def gossip():
	global message
	global count
	while float(message['time'])>time.time():
		
		count = count +1
		port = random.randint(0,19)+5000
		time.sleep(1)
		try:
			requests.post(url = "http://localhost:"+str(port)+"/api",json = message)
		except Exception as e:
			pass
	correction()
			
def correction():
	port = int(sys.argv[1])
	global ccount
	
	while float(message['ctime'])>time.time():
		global count
		count = count + 1
		ccount = ccount + 1
		port1 = 5000 + ((port+1)%20)
		time.sleep(1)
		try:
			requests.post(url = "http://localhost:"+str(port1)+"/api",json = message)
		except Exception as e:
			pass
			

api.add_resource(GossipNode, '/api')

if __name__ == '__main__':
	app.run(port=int(sys.argv[1]),debug=False)

from flask import Flask, request
from flask_restful import Resource, Api
import time, random, requests, threading, sys

app = Flask(__name__)
api = Api(app)

count = 0
message = ""
infected = False


class GossipNode(Resource):

	def get(self):
		global count
		icount = 0
		if(infected == True):
			icount = icount + 1
		return {"count": count,"icount": icount}

	def post(self):
		global message
		global infected
		
		if(infected == False):
			message = request.json
			infected = True
			pollThread = threading.Thread(target=gossip,name = "Polling Thread")
			pollThread.daemon = True
			pollThread.start()
		
		return "",201
		
def gossip():
	global message
	global count
	while float(message['time'])>time.time():
		count = count+1
		port = 5000+random.randint(0,19)
		time.sleep(1)
		print("send msg to -->  localhost: "+ str(port))
		try:
			requests.post(url = "http://localhost:"+str(port)+"/api",json = message)
		except Exception as e:
			pass
			

api.add_resource(GossipNode, '/api')

if __name__ == '__main__':
	app.run(port=int(sys.argv[1]),debug=False)

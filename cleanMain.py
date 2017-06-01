from socketIO_client import SocketIO, LoggingNamespace
import sys
import time
sys.path.append("../PyRow")
import pyrow
# Opens socket connection to communicate between Erg Telemetry and NODE
addr = 'localhost'
port = 8080
socketIO = SocketIO(addr, port, LoggingNamespace)

# print ("Meow")
# Send dummy data
data = {'time':'','distance':'','driveLength': 1.24,'driveTime': 0.6,'strokeRecoveryTime': 1.42,'strokeRecoveryDistance': 9.86,'peakDriveForce': 181.70000000000002,'avgDriveForce': 102,'strokePower': 241,'strokeCalories': 1129,'strokeCount': 39}
socketIO.emit('strokeData',data)
data = {'cid':'2','status': 9, 'distance': '11.2', 'heartrate': 0, 'power': int(6), 'calhr': 320.6496, 'calories': int(0),'forceplot': [], 'pace': 87.8277952417603, 'spm': 51, 'time': 9.29}
socketIO.emit('ergData',data)
deltaTime = 0.1
def searchErgs():
	number_ergs=0
	ergs = []
	while(number_ergs==0):
		ergs = pyrow.find()
		ergs = list(ergs)
		number_ergs = len(ergs)
		print "Ergs connected:" + str(number_ergs)
		print ("Searching for ergs")
		time.sleep(deltaTime)
	return ergs
erg = searchErgs()[0]
m = pyrow.pyrow(erg)
# print m.get_status()
ergInfo = m.get_erg()
num_zeros = 0
num_ones = 0
prev_time = 0

while(1):
	try:
		data = m.get_monitor(forceplot=True)
		data['cid'] = ergInfo['cid']
		print data
		#print data['forceplot']
		
		if(0==len(data['forceplot'])):
			num_zeros +=1
			if(num_ones>3):
				print "endedstarted "+str(prev_time)+" " +str(data['time'])
				data['driveTime']=data['time']-prev_time 
				prev_time = data['time']
				socketIO.emit('strokeData',data)
			num_ones=0

		else:
			num_ones +=1
			#print num_zeros
			if(num_zeros>3):
				
				print "rowe started "+str(prev_time)+" " +str(data['time'])
				data['strokeRecoveryTime']=data['time']-prev_time 
				prev_time = data['time']
				socketIO.emit('strokeData',data)
			num_zeros = 0
		socketIO.emit('ergData',data)
		time.sleep(0.01)
	except IOError as e:
		time.sleep(1)
		print e
		print "Search for ergs again"
		erg = searchErgs()[0]
		m = pyrow.pyrow(erg)
		# print m.get_status()
		ergInfo = m.get_erg()

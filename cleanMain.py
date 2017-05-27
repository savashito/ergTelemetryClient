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
while(1):
	try:
		data = m.get_monitor(forceplot=True)
		data['cid'] = ergInfo['cid']
		print data.forceplot
		print len(data.forceplot)
		socketIO.emit('ergData',data)
		time.sleep(deltaTime)
	except:
		time.sleep(1)
		print "Search for ergs again"
		erg = searchErgs()[0]
		m = pyrow.pyrow(erg)
		# print m.get_status()
		ergInfo = m.get_erg()

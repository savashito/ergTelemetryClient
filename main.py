import sys
import time
from socketIO_client import SocketIO, LoggingNamespace
sys.path.append("../PyRow")
import pyrow
addr = ''
if(len(sys.argv)>1 and sys.argv[1]=='local'):
    addr = 'localhost'
else:
    addr = '54.153.114.110'# '192.168.0.3'
print sys.argv
print "Connecting to "+addr
ergs = pyrow.find()
ergs = list(ergs)
number_ergs = len(ergs)
print "Ergs connected:" + str(number_ergs)
if(number_ergs>0):
	erg = ergs[0]
	m = pyrow.pyrow(erg)
	print m.get_status()
	ergInfo = m.get_erg()
	# cid serial
	with SocketIO(addr, 80, LoggingNamespace) as socketIO:
		while 1:
			data = m.get_monitor(forceplot=True)
			data['cid'] = ergInfo['cid']
			print data
			socketIO.emit('ergData',data)




with SocketIO(addr, 80, LoggingNamespace) as socketIO:
    # socketIO.emit('connection')
    data = {'cid':2,'status': 9, 'distance': 11.2, 'heartrate': 0, 'power': 6, 'calhr': 320.6496, 'calories': 0, 'pace': 387.8277952417603, 'spm': 51, 'time': 9.29}
    # socketIO.wait(seconds=1)
    # for i in range(10):
    totalTime = 0
    deltaTime = 0.5 # s
    deltaDistance = 5 # m per s
    totalDistance = 0
    while 1:
    	data['distance'] = totalDistance
    	data['time'] = totalTime
    	socketIO.emit('ergData',data)
    	time.sleep(deltaTime)
    	totalDistance = totalDistance +deltaDistance*deltaTime
    	totalTime = totalTime+deltaTime

    	# socketIO.emit('boop',{'data','meow','Muerte': 'world '+str(i)})

    socketIO.wait(seconds=1)
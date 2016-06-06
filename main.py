import sys
from socketIO_client import SocketIO, LoggingNamespace
sys.path.append("../PyRow")
import pyrow

addr = '192.168.0.3'
ergs = pyrow.find()
number_ergs = len(list(ergs))
print "Ergs connected:" + str(number_ergs)
if(number_ergs>0):
	erg = ergs.next()
	m = pyrow.pyrow(erg)
	print m.get_status()
	with SocketIO(addr, 80, LoggingNamespace) as socketIO:
		while 1:
			data = m.get_monitor()
			print data
			socketIO.emit('ergData',data)




with SocketIO(addr, 80, LoggingNamespace) as socketIO:
    # socketIO.emit('connection')
    # socketIO.wait(seconds=1)
    for i in range(10):
    	socketIO.emit('ergData',{'Muerte': 'world '+str(i)})
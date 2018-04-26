from socketIO_client import SocketIO, LoggingNamespace
import sys
import time
# sys.path.append("../PyRow")
# import pyrow
# Opens socket connection to communicate between Erg Telemetry and NODE
addr = '127.0.0.1'
# addr = 'localhost'
port = 8080
print ("listen to coonectios")
socketIO = SocketIO(addr, port, LoggingNamespace)
print ("Meow")
# Send dummy data
# data = {'time':'','distance':'','driveLength': 1.24,'driveTime': 0.6,'strokeRecoveryTime': 1.42,'strokeRecoveryDistance': 9.86,'peakDriveForce': 181.70000000000002,'avgDriveForce': 102,'strokePower': 241,'strokeCalories': 1129,'strokeCount': 39}
# socketIO.emit('strokeData',data)
import random
distance = 0
distance1 = 0
distance2 = 0

mTime = 0
dx = 0
prev_time = 0
while 1:
	distance = distance + 1
	distance1 = distance1 +1
	distance2 = distance2 +1
	mTime = mTime +0.5
	# data = {'time':'','distance':'','driveLength': 1.24,'driveTime': 0,'i':0,'strokeRecoveryTime': 0,'strokeRecoveryDistance': 9.86,'peakDriveForce': 181.70000000000002,'avgDriveForce': 102,'strokePower': 241,'strokeCalories': 1129,'strokeCount': 39}
	# socketIO.emit('strokeData',data)
	# data = {'time':'','distance':'','driveLength': 1.24,'driveTime': 0,'i':1,'strokeRecoveryTime': 0,'strokeRecoveryDistance': 9.86,'peakDriveForce': 181.70000000000002,'avgDriveForce': 102,'strokePower': 241,'strokeCalories': 1129,'strokeCount': 39}
	# socketIO.emit('strokeData',data)
	####
	if(distance%4==0):
		k = 3
		dx = int(random.random()*k)-k/2.0
	# else:
		# dx = 0
	# data = {'cid':'2','status': 9, 
	# 	'distance': distance , 
	# 	'heartrate': 0,'i':0, 'power': int(6), 'calhr': 320.6496, 'calories': int(0),
	# 	'forceplot': [], 
	# 	'pace': 107.8277952417603+dx, 
	# 	'spm': 35, 'time': mTime}
	ergData = 	{'i':0,'time':mTime, 'distance':distance, 'flags':0, 'totalWOGDistance':0, 'totalWOGTime':0, 'WOGTimeType':0, 'drag':122, 'speed':2, 'SPM':3, 'heartrate':4, 'pace':107.8277952417603+dx, 'avgPace':107.8277952417603, 'restDistance':7, 'restTime':8,'intervalCount':9,'avgPower':10, 'calories':11, 'splitAvgPace':12, 'splitAvgPower':13, 'splitAvgCalories':14, 'splitTime':15, 'splitDistance':16}
	socketIO.emit('ergData',ergData)
	# socketIO.emit('ergData',data)
	# print data
	# data = {'cid':'2','status': 9, 'distance': distance1+30.0, 'heartrate': 0,'i':1, 'power': int(6), 'calhr': 320.6496, 'calories': int(0),'forceplot': [], 'pace': 107.8277952417603+dx, 'spm': 41, 'time': mTime}
	# socketIO.emit('ergData',data)
	# # print data
	# data = {'cid':'2','status': 9, 'distance': distance2+15.0, 'heartrate': 0,'i':2, 'power': int(6), 'calhr': 320.6496, 'calories': int(0),'forceplot': [], 'pace': 87.8277952417603, 'spm': 22, 'time': mTime}
	# socketIO.emit('ergData',data)
	# print data
	time.sleep(0.4)
	strokeData = {'time':23}
	strokeData = 	{'i':0,'time':mTime, 'distance':distance, 'driveLength':3, 'driveTime':4, 'strokeRecoveryTime':mTime-prev_time, 'strokeRecoveryDistance':6, 'peakDriveForce':7, 'avgDriveForce':8, 'workPerStroke':8, 'strokeCount':10, 'strokePower':11, 'strokeCalories':12, 'projectedWorkTime':13, 'projectedWorkDistance':14}
	
	prev_time = strokeData['time']
	socketIO.emit('strokeData',strokeData)
	time.sleep(0.1)

  # ergData = 	{'i':0,'time':0,'speed':0, 'SPM':0, 'heartrate':0, 'pace':0, 'avgPace':0, 'restDistance':0, 'restTime':0,'intervalCount':0,'avgPower':0, 'calories':0, 'splitAvgPace':0, 'splitAvgPower':0, 'splitAvgCalories':0, 'splitTime':0, 'splitDistance':0}
  # strokeData = 	{'i':0,'time':0 'distance':0, 'driveLength':0, 'driveTime':0, 'strokeRecoveryTime':0, 'strokeRecoveryDistance':0, 'peakDriveForce':0, 'avgDriveForce':0, 'workPerStroke':0, 'strokeCount':0, 'strokePower':0, 'strokeCalories':0, 'projectedWorkTime':0, 'projectedWorkDistance':0}
# deltaTime = 0.01
# # def searchNewErgs()
# def searchErgs():
# 	number_ergs=0
# 	ergs = []
# 	while(number_ergs==0):
# 		print ("Searching for ergs")
# 		ergs = pyrow.find()
# 		ergs = list(ergs)
# 		number_ergs = len(ergs)
# 		print "Ergs connected:" + str(number_ergs)
		
# 		time.sleep(deltaTime)

# 	return ergs
# # erg = searchErgs()[0]
# # m = pyrow.pyrow(erg)
# # # print m.get_status()
# # ergInfo = m.get_erg()



# import threading

# m = [0,0,0,0]
# def USBErgService (  ):
# 	running = True;
# 	num_zeros = [0,0,0,0]
# 	num_ones = [0,0,0,0]
# 	prev_time = [0,0,0,0]
	
# 	ergs = searchErgs()
# 	n_ergs = len(ergs)
# 	for i in range(len(ergs)):
# 		m[i] = pyrow.pyrow(ergs[i])	
# 	while(running):
# 		ergs = pyrow.find()
# 		ergs = list(ergs)
# 		if n_ergs != len(ergs):
# 			# new erg connection
# 			running = False
# 			return
# 			# for i in range(n_ergs,len(ergs)):
# 				# running = False
# 				# break
# 				# print i
# 				# time.sleep(1)

# 				# ergs = pyrow.find()
# 				# ergs = list(ergs)
# 				# m[i] = pyrow.pyrow(ergs[i])	
# 			# n_ergs=	len(ergs)
# 		try:
# 			for i in range(n_ergs):
# 				# m = pyrow.pyrow(ergs[i])
# 				# print m.get_status()
# 				ergInfo = m[i].get_erg()
# 				data = m[i].get_monitor(forceplot=True)
# 				data['cid'] = ergInfo['cid']
# 				data['i'] = i
# 				print data
# 				#print data['forceplot']
			
# 				if(0==len(data['forceplot'])):
# 					num_zeros[i] +=1
# 					if(num_ones[i]>3):
# 						print "endedstarted "+str(prev_time[i])+" " +str(data['time'])
# 						data['driveTime']=data['time']-prev_time[i] 
# 						prev_time[i] = data['time']
# 						socketIO.emit('strokeData',data)
# 					num_ones[i]=0

# 				else:
# 					num_ones[i] +=1
# 					#print num_zeros
# 					if(num_zeros[i]>3):
						
# 						print "rowe started "+str(prev_time[i])+" " +str(data['time'])
# 						data['strokeRecoveryTime']=data['time']-prev_time[i] 
# 						prev_time[i] = data['time']
# 						socketIO.emit('strokeData',data)
# 					num_zeros[i] = 0
# 	#			print data
# 				socketIO.emit('ergData',data)
# 			# ergs = pyrow.find()
# 			# print len(list(ergys))
# 			# ergs = list(ergs)
# 			# number_ergs = len(ergs)
# 			time.sleep(0.01)
# 				# ergs = searchErgs()
		
# 		except Exception as e:
# 			running=False;
# 			n_ergs = 0
# 			# time.sleep(1)
# 			print e
# 			print "Search for ergs again"
# 			return

# 			# erg = searchErgs()[0]
# 			# m = pyrow.pyrow(erg)
# 			# print m.get_status()
# 			# ergInfo = m.get_erg()
# # while(1):
# USBErgServiceT = threading.Thread(name='daemon', target=USBErgService)
# USBErgServiceT.start()
# USBErgServiceT.join()
# # time.sleep(1)
# pyrow.release(m);
# print m

# USBErgServiceT = threading.Thread(name='daemon', target=USBErgService)
# USBErgServiceT.start()
# USBErgServiceT.join()

#time.sleep(1)
#USBErgServiceT = threading.Thread(name='daemon', target=USBErgService)
#USBErgServiceT.start()
#USBErgServiceT.join()



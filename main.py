import sys
sys.path.append("../PyRow")
import pyrow

ergs = pyrow.find()
number_ergs = len(list(dev))
print number_ergs
erg = ergs.next()
m = pyrow.pyrow(erg)
print m.get_status()
while 1:
	data = m.get_monitor()
	print data
import serial
import sys

assert len(sys.argv) == 2
print sys.argv

# try to open the comm
mcomm = None
try:
    mcomm=serial.Serial( sys.argv[1],timeout=1)
except serial.serialutil.SerialException:
    print 'BOOM! @ %s' % sys.argv[1]
    #raise serial.serialutil.SerialException
if not mcomm or not mcomm.isOpen():
    print "Problem opening port. Exiting..."
    sys.exit(3)


##print mcomm

print 'Slave: Checking comm...',
bytesWaiting = mcomm.inWaiting()
print '%d bytes waiting...' % bytesWaiting,
response = mcomm.read(bytesWaiting)
print 'Got: "%s"' % response


mcomm.close()

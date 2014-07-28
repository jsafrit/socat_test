import serial
import sys
import time

assert len(sys.argv) == 2
##print sys.argv

# try to open the comm
mcomm = None
try:
    mcomm=serial.Serial( sys.argv[1],timeout=None)
except serial.serialutil.SerialException:
    print 'BOOM! @ %s' % sys.argv[1]
    #raise serial.serialutil.SerialException
if not mcomm or not mcomm.isOpen():
    print "Problem opening port. Exiting..."
    sys.exit(3)


##print mcomm

while True:
    print 'slave: Checking comm...',
    bytesWaiting = mcomm.inWaiting()
    #print '%d bytes waiting...' % bytesWaiting,
    if bytesWaiting:
        response = mcomm.read(bytesWaiting)
        print 'Got: "%s"' % response.strip()
    else:
        print    
    time.sleep(1)
    
print 'slave done...'
mcomm.close()

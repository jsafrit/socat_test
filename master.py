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

msg = 'MySecretMessage'
print 'master: Sending: "%s"' % msg
mcomm.write(msg)


mcomm.close()

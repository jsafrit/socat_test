import serial
import sys
import time

def parseMsg(st):
    #st = str(st)
    newst = str(st.decode()).strip().split('\n')
    for sst in newst:
        print('slave: %s' % sst)


assert len(sys.argv) == 2
##print sys.argv

# try to open the comm
mcomm = None
try:
    mcomm=serial.Serial( sys.argv[1],timeout=None)
except serial.serialutil.SerialException:
    print('BOOM! @ %s' % sys.argv[1])
    #raise serial.serialutil.SerialException
if not mcomm or not mcomm.isOpen():
    print("Problem opening port. Exiting...")
    sys.exit(3)


##print mcomm

while True:
    print('slave: Checking comm:',)
    bytesWaiting = mcomm.inWaiting()
    
    if bytesWaiting:
        print('%d bytes waiting.' % bytesWaiting)
        response = mcomm.read(bytesWaiting)
        parseMsg(response)
        #print 'Got: "%s"' % response.strip()
    else:
        print('Nothing yet.')
    time.sleep(1)
    
print('slave done...')
mcomm.close()

import serial
import sys
import time

def parseMsg(st):
    newst = st.decode().strip().split('\n')
    for sst in newst:
        print('slave: %s' % sst)

# comm must be specified from launch
assert len(sys.argv) == 2

# must be run under python3
assert sys.version[0] == '3'

# try to open the comm
mcomm = None
try:
    mcomm = serial.Serial( sys.argv[1],timeout=None)
except serial.serialutil.SerialException:
    print('BOOM! @ %s' % sys.argv[1])

if not mcomm or not mcomm.isOpen():
    print('Problem opening port. Exiting...')
    sys.exit(3)


while True:
    print('  slave: Checking comm: ',end='')
    bytesWaiting = mcomm.inWaiting()
    
    if bytesWaiting:
        print('%d bytes waiting.' % bytesWaiting)
        response = mcomm.read(bytesWaiting)
        parseMsg(response)
    else:
        print('Nothing yet.')
    time.sleep(1)
    
print('slave done...')
mcomm.close()

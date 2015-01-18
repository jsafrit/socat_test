import serial
import sys
import time 

# comm must be specified from launch
assert len(sys.argv) == 2

# must be run under python3
assert sys.version[0] == '3'

# try to open the comm
mcomm = None
try:
    mcomm = serial.Serial( sys.argv[1],timeout=1)
except serial.serialutil.SerialException:
    print('BOOM! @ %s' % sys.argv[1])

if not mcomm or not mcomm.isOpen():
    print('Problem opening port. Exiting...')
    sys.exit(3)

# read in fortunes file
ff = open('fortunes.txt')
fortunes = ff.readlines()

for fortune in fortunes:
    time.sleep(.2)
    mcomm.write(fortune.encode())

print('master done...')
mcomm.close()

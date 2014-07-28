import serial
import os
import shlex,subprocess
import time

# create virtual com ports for testing
cmdline = 'socat PTY,link=COM8 PTY,link=COM9'
args = shlex.split(cmdline)
pComms = subprocess.Popen(args)

print 'PID of socat is %d' % pComms.pid
time.sleep(1)

#print p.poll()

c1 = serial.Serial('COM8')
c2 = serial.Serial('COM9')

assert c1.isOpen()
assert c2.isOpen()
os.system('ls -alF .')

msg = 'HELLO'
print 'Sending: "%s"' % msg
c1.write(msg)

print 'Checking comm...',
response = c2.read(5)
print 'Got: "%s"' % response




pComms.terminate()
time.sleep(2)
print pComms.poll()


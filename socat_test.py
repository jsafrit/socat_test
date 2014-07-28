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

##c1 = serial.Serial('COM8')
c2 = serial.Serial('COM9')

##assert c1.isOpen()
assert c2.isOpen()
#os.system('ls -alF .')

##msg = 'MySecretMessage'
##print 'Sending: "%s"' % msg
##c1.write(msg)
cmdline = 'python master.py COM8'
args = shlex.split(cmdline)
mc = subprocess.Popen(args)
mc.wait()

time.sleep(.1)

print 'Checking comm...',
bytesWaiting = c2.inWaiting()
print '%d bytes waiting...' % bytesWaiting,
response = c2.read(bytesWaiting)
print 'Got: "%s"' % response

#assert msg==response



print 'Closing socat...'
pComms.terminate()
time.sleep(2)



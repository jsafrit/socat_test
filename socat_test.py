import serial
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
##c2 = serial.Serial('COM9')

##assert c1.isOpen()
##assert c2.isOpen()

##msg = 'MySecretMessage'
##print 'Sending: "%s"' % msg
##c1.write(msg)
cmdline = 'python master.py COM8'
args = shlex.split(cmdline)
mc = subprocess.Popen(args)
#mc.wait()

# just give the master a head start for no reason
time.sleep(3)

##print 'Checking comm...',
##bytesWaiting = c2.inWaiting()
##print '%d bytes waiting...' % bytesWaiting,
##response = c2.read(bytesWaiting)
##print 'Got: "%s"' % response
cmdline = 'python slave.py COM9'
args = shlex.split(cmdline)
sc = subprocess.Popen(args)
##print mc.poll()
##sc.wait()
##mc.wait()

#do not close down until master is finished
done = mc.poll()
while done is None:
    print '...'
    time.sleep(1)
    done = mc.poll()

#tosin final message from main just cause we can...
c1.write('It is finished...')

#give time for last messages to get through...
time.sleep(2)
print 'Closing slave...'
sc.terminate()
time.sleep(1)

print 'Closing socat...'
pComms.terminate()
time.sleep(1)

import serial
import shlex,subprocess
import time

# create virtual com ports for testing
cmdline = 'socat PTY,link=COM8 PTY,link=COM9'
args = shlex.split(cmdline)
pComms = subprocess.Popen(args)

# Give it time to establish comms
time.sleep(1)

c1 = serial.Serial('COM8')
assert c1.isOpen()

cmdline = 'python3 slave.py COM9'
args = shlex.split(cmdline)
sc = subprocess.Popen(args)
print('slave started...')

cmdline = 'python3 master.py COM8'
args = shlex.split(cmdline)
mc = subprocess.Popen(args)
print('master started...')

# do not close down until master is finished
while mc.poll() is None:
    time.sleep(1)

# toss in final message from main just cause we can...
c1.write(b'\nIt is finished...')

# give time for last messages to get through...
time.sleep(1)
print('Closing slave...')
sc.terminate()
time.sleep(1)

# close up the virtual comms
print('Closing socat...')
pComms.terminate()
time.sleep(1)

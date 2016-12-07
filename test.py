from __future__ import division
import signal
import sys
import numpy as np


test = [0,0,19500,19500,19500,19450]
overall = sum(test)
p = []
#Create the probablilities
for fit in test:
    print(fit/overall)
    p.append(fit/overall)

print(overall)
print(sum(p))

# def signal_handler(signal, frame):
#         print('You pressed Ctrl+C!')
#         sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')
# signal.pause()
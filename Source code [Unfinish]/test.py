# print status FAIL
'''
print('[' + '█'*50 + ']')
input('press key')

import time

print("          Wryyyyyyyyyyyyyyyyyy", end="\r")
time.sleep(2)
print('zaworldo')


import sys,time
print("FAILED...") 
print("FAILED...") 
print("FAILED...") 
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line 
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line 
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line 
time.sleep(2)
print("SUCCESS!")
'''

# read log line(?) FAIL
'''
f = open('D:\.github\chia-auto-plot\Source code [Unfinish]\Chia-Auto-Plot-27-05-21T22-44-18.txt','r')
log = f.read()
f.close()
line_count = (log.count('\n') + 1)
print(line_count)
'''

# list final directory unFinish
stop_list = []
final_list = []
final_dir = ['a','b','c']
final_count = [4,5,3]
stop_count = 0
for i in range(max(final_count)):
    for i in range(len(final_count)):
        if final_count[i] > 0:
            final_list += final_dir[i]
            final_count[i] = final_count[i] - 1
            stop_count+=1
    stop_list.append(stop_count)

print(final_list)
print(stop_list)

for i in stop_list:
    print(final_list[i-1])
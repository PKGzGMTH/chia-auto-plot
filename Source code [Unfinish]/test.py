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


'''working_log = ['test.txt']
def get_log_process():
    f = open(f'D:\\.github\\chia-auto-plot\\Source code [Unfinish]\\{working_log[0]}','r')
    log = f.read()
    f.close()
    line_count = (log.count('\n')+1)
    print(f'total line is of this log : {line_count}')
    line = 0
    # Get num of Bucket split to line
    for i in log.split("\n"):
        line += 1
        if 'buckets' in i:
            print(i.strip())
            buckets = i.split(' ')[1]
            print(f'Bucket is {buckets}')
        if 'Starting phase' in i:
            print(line)
            

get_log_process()'''

data = [['a', 'b', 'c'], ['aaaaaaaaaaaaaaaaaaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'csdfaseav']]

col_width = max(len(word) for row in data for word in row) + 2  # padding
for row in data:
    print ("".join(word.ljust(col_width) for word in row))

    
''' calculate total line in .txt
    P1 = 4 + (129(buckets) 2) + 1
    P2 = 34
    P3 = 2 + 
    P4 =
    Finish = line_count = (log.count('Renamed final file from'))

'''


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
    print(final_list[i-1])'''
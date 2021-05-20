import subprocess
import time
import os
os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

main_command = 'start C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoExit C:\\Users\\' + (os.getlogin()) + '\\AppData\\Local\\chia-blockchain\\app-1.1.5\\resources\\app.asar.unpacked\\daemon\\chia'
temp_list = []

print('How many Threads of CPU do you have?')
threads_total = int(input())

print('How many Tempolary drive you have?')
temp_total = int(input())

for i in range(temp_total):
    print('\nPlease Enter loaction of Tempolary Directory drive ' + str(i+1))
    temp_dir = str(input())
    print('Please Enter capacity of drive ' + str(i+1))
    temp_count = int(int(input())/257)

    print('\nLocation of Tempolary directory ' + str(i+1) + ' is \"' + temp_dir + '\"  and total temp is : ' + str(temp_count))
    print('Please enter \'Confirm!\' to confirm this.\n')
    if input() != 'Confirm!':
        print('Skip this!')
        break

    i+1


'''
plot_range = int(input())

for i in range(plot_range):
    print('please select Tempolary directory of plot ' + str(i+1))
    input_ = str(input())
    temp_list.append( input_ )
    print(bcolors.OKGREEN + 'Set Tempolary directory of plot ' + str(i+1) +' in ' + input_ + ' Succesfully' + bcolors.ENDC)
    print()
    i+= 1
print(bcolors.HEADER + 'Temp list set :' + bcolors.ENDC)
print(temp_list)
print('\nplease select Final directory')
final_dir = str(input())

for i in range(plot_range):
    plot_command = main_command + ' plots create -k 32 -e -b 4000 -r 2 -t ' + temp_list[i] + ' -d ' + final_dir
    print(plot_command)
    #subprocess.call(plot_command, shell=True)
    i+= 1
    time.sleep(900)
'''
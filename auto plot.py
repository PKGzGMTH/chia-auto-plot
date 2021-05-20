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

print('How much you want to plot in same time?')
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
    subprocess.call(plot_command, shell=True)
    i+= 1
    time.sleep(900)
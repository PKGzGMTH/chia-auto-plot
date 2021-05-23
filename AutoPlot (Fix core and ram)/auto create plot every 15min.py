import subprocess
import datetime
import os
import time
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

def chia_get_version():
    # Search Version Chia
    chia_directory = os.listdir(os.environ['USERPROFILE'] + "\\AppData\\Local\\chia-blockchain\\")
    chia_version = ""
    for chia_data in chia_directory:
        if "app-" in chia_data:
            chia_version = chia_data
            
    # Check Condition
    if len(chia_version) == 0:
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("[" + str(timeNow) + "][System] Please install Chia-Blockchian on you computer")
        input("Press Enter to continue...")
        exit()
    else:
        # Set Chia Execute Folders
        global chia
        chia = os.environ['USERPROFILE'] + f"\\AppData\\Local\\chia-blockchain\\{chia_version}\\resources\\app.asar.unpacked\\daemon\\chia.exe"

chia_get_version()
main_command = f'start C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoExit {chia}'
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
print(bcolors.FAIL + '\nplease don\'t close this windows' + bcolors.ENDC)
for i in range(plot_range):
    plot_command = main_command + f' plots create -k 32 -b 4000 -r 3 -u 128 -t ' + temp_list[i] + ' -d ' + final_dir
    print(plot_command)
    subprocess.call(plot_command, shell=True)
    i+= 1
    time.sleep(900)
print(bcolors.OKGREEN + 'You can close this windows now' + bcolors.ENDC)
input("Press Enter to continue...")
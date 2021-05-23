import subprocess
import datetime
import os
import time
os.system('cls')
temp_list = []

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

def print_info():
    print(bcolors.OKGREEN + 'Auto Create Plot Every 15 minute [ Version 0.1 ]' + bcolors.ENDC)
    print(bcolors.HEADER + 'This program will Plot k=32, Bucket128 and use 4000M of ram per Plot' + bcolors.ENDC)

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

def plot_setting():

    # Total number of Tempolary Directory
    print('\nHow much you want to plot in same time? (or Number of Tempolary Directory)')
    global plot_range
    plot_range = int(input())

    if plot_range <= 0:
        print(bcolors.FAIL + 'Error, Please enter a number of Tempolary Directory [Least is 1]' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        os.close()
        

    for i in range(plot_range):
        print('please select Tempolary directory of plot ' + str(i+1))
        input_ = str(input())
        temp_list.append( input_ )
        print(bcolors.OKGREEN + 'Set Tempolary directory of plot ' + str(i+1) +' in ' + input_ + ' Succesfully' + bcolors.ENDC)
        print()
        i+= 1

    print(bcolors.HEADER + 'Temp list set :' + bcolors.ENDC)
    print(temp_list)


    # Final Directory Setting
    global final_dir
    print('\nplease select Final directory')
    final_dir = str(input())


    # Plot Count setting
    print(f'\nPlease Enter Number of {bcolors.OKGREEN}Plot Count{bcolors.ENDC} [Default is 1 Plot count]')
    global plot_count
    plot_count = '-n '
    input_plot_count = input()

    if input_plot_count == '':
            input_plot_count = int(1)

    plot_count_state_error = False
    try :
        input_plot_count = int(input_plot_count)

        if input_plot_count <= 0:
            print(bcolors.FAIL + 'Error, Please enter a number of Plot count [Least is 1]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            plot_count_state_error = True
            os.close()

    except:
        if plot_count_state_error == True :
            os.close()
        print(bcolors.FAIL + 'Error, Please enter Only a number of Plot Count' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    plot_count += str(input_plot_count)
    print(bcolors.OKGREEN + 'Set Plot count : ' + str(input_plot_count) + bcolors.ENDC)


    # Threads Setting
    print(f'\nPlease Enter Number {bcolors.OKGREEN}Threads{bcolors.ENDC} to use to {bcolors.OKGREEN}create Plots(per Plot){bcolors.ENDC} [Default is 2 Threads]')
    global threads
    threads = '-r '
    input_threads = input()
    if input_threads == '':
            input_threads = int(2)

    threads_state_error = False
    try :
        input_threads = int(input_threads)

        if input_threads <= 0:
            print(bcolors.FAIL + 'Error, Please enter a number of threads [Least is 1 Threads]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            threads_state_error = True
            os.close()

    except:
        if threads_state_error == True :
            os.close()
        print(bcolors.FAIL + 'Error, Please enter Only a number of threads' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    threads += str(input_threads)
    print(bcolors.OKGREEN + 'Set Threads for Plotting : ' + str(input_threads) + bcolors.ENDC)

def start_create_plot():
    print(bcolors.FAIL + '\nplease don\'t close this windows' + bcolors.ENDC)

    for i in range(plot_range):
        main_command = f'start C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoExit {chia}'

        plot_command = main_command + f' plots create -k 32 -b 4000 {threads} {plot_count} -u 128 -t {temp_list[i]} -d {final_dir}'
        print(plot_command)
        subprocess.call(plot_command, shell=True)
        i+= 1
        time.sleep(900)

    print(bcolors.OKGREEN + 'You can close this windows now' + bcolors.ENDC)
    input(bcolors.OKGREEN + "Press Enter to continue..." + bcolors.ENDC)

print_info()
chia_get_version()
plot_setting()
start_create_plot()
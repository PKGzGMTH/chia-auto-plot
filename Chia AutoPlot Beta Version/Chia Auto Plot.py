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
    print(f'{bcolors.OKGREEN}Auto Create Plot with CMD.exe [ Version 0.1-cmd ]{bcolors.ENDC}')
    print(f'{bcolors.HEADER}Now you can setup Every thing!, Let\'t Start!!{bcolors.ENDC}')
    print(f'\nYou can Follow our New Version at {bcolors.WARNING}github.com/PKGzGMTH/chia-auto-plot' + bcolors.ENDC)

def chia_get_version():
    # Search Version Chia
    chia_directory = os.listdir(
        os.environ['USERPROFILE'] + "\\AppData\\Local\\chia-blockchain\\")
    chia_version = ""
    for chia_data in chia_directory:
        if "app-" in chia_data:
            chia_version = chia_data

    # Check Condition
    if len(chia_version) == 0:
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("[" + str(timeNow) +
              "][System] Please install Chia-Blockchian on you computer")
        input("Press Enter to continue...")
        exit()
    else:
        # Set Chia Execute Folders
        global chia
        chia = os.environ['USERPROFILE'] + \
            f"\\AppData\\Local\\chia-blockchain\\{chia_version}\\resources\\app.asar.unpacked\\daemon\\chia.exe"

def get_Bucket_setup():
    print(
        f'\nPlease Enter Number {bcolors.OKGREEN}Bucket{bcolors.ENDC} [Default is 128]')
    global Bucket
    Bucket = '-u '
    input_Bucket = input()
    if input_Bucket == '':
        input_Bucket = int(128)

    Bucket_state_error = False
    try:
        input_Bucket = int(input_Bucket)

        if input_Bucket < 32 or input_Bucket > 128:
            print(
                bcolors.FAIL + 'Error, Please enter a number of Bucket [32-128]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            Bucket_state_error = True
            os.close()

    except:
        if Bucket_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of Bucket' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    Bucket += str(input_Bucket)
    print(bcolors.OKGREEN + 'Setup number Bucket : ' +
          str(input_Bucket) + bcolors.ENDC)

def get_K_size_setup():
    print(
        f'\nPlease Enter Number {bcolors.OKGREEN}K-size{bcolors.ENDC} You want to create [Default is 32]')
    global K_size
    K_size = '-k '
    input_K_size = input()
    if input_K_size == '':
        input_K_size = int(32)

    K_size_state_error = False
    try:
        input_K_size = int(input_K_size)

        if input_K_size < 32 or input_K_size > 35:
            print(
                bcolors.FAIL + 'Error, Please enter a number of K size [32-35]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            K_size_state_error = True
            os.close()

    except:
        if K_size_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of K size' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    K_size += str(input_K_size)
    print(bcolors.OKGREEN + 'Setup K size : ' +
          str(input_K_size) + bcolors.ENDC)

def get_ram_setup():
    # ram setting
    print(
        f'\nPlease Enter Number {bcolors.OKGREEN}Ram{bcolors.ENDC} to use to {bcolors.OKGREEN}create Plots(per Plot){bcolors.ENDC} [Default is 4000]')
    global ram
    ram = '-b '
    input_ram = input()
    if input_ram == '':
        input_ram = int(4000)

    ram_state_error = False
    try:
        input_ram = int(input_ram)

        if input_ram < 2900:
            print(
                bcolors.FAIL + 'Error, Please enter a number of ram [Least is 2900]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            ram_state_error = True
            os.close()

    except:
        if ram_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of ram' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    ram += str(input_ram)
    print(bcolors.OKGREEN + 'Setup Ram for plotting ' +
          str(input_ram) + ' per plot' + bcolors.ENDC)

def get_plot_directory_setup():
    print('\nHow many number of plot you want to plotting in same time? (Number of Queue)')
    global plot_range
    plot_range = int(input())

    if plot_range <= 0:
        print(bcolors.FAIL +
              'Error, Please enter a number of Tempolary Directory [Least is 1]' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        os.close()

    for i in range(plot_range):
        print('\nplease select Tempolary directory of plot ' + str(i+1))
        input_ = str(input())
        temp_list.append(input_)
        print(bcolors.OKGREEN + 'Set Tempolary directory of plot ' +
              str(i+1) + ' in ' + input_ + ' Succesfully' + bcolors.ENDC)
        print()
        i += 1

    print(bcolors.HEADER + 'Temp list setup :' + bcolors.ENDC)
    print(temp_list)

    # Final Directory Setting
    global final_dir
    print('\nplease select Final directory')
    final_dir = str(input())

def get_plot_count_setup():
    print(
        f'\nPlease Enter Number of {bcolors.OKGREEN}Plot Count{bcolors.ENDC} [Default is 1 Plot count]')
    global plot_count
    plot_count = '-n '
    input_plot_count = input()

    if input_plot_count == '':
        input_plot_count = int(1)

    plot_count_state_error = False
    try:
        input_plot_count = int(input_plot_count)

        if input_plot_count <= 0:
            print(
                bcolors.FAIL + 'Error, Please enter a number of Plot count [Least is 1]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            plot_count_state_error = True
            os.close()

    except:
        if plot_count_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of Plot Count' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    plot_count += str(input_plot_count)
    print(bcolors.OKGREEN + 'Set Plot count : ' +
          str(input_plot_count) + bcolors.ENDC)

    # Threads Setting

def get_threads_setup():
    print(
        f'\nPlease Enter Number {bcolors.OKGREEN}Threads{bcolors.ENDC} to use to {bcolors.OKGREEN}create Plots(per Plot){bcolors.ENDC} [Default is 2 Threads]')
    global threads
    threads = '-r '
    input_threads = input()
    if input_threads == '':
        input_threads = int(2)

    threads_state_error = False
    try:
        input_threads = int(input_threads)

        if input_threads <= 0:
            print(
                bcolors.FAIL + 'Error, Please enter a number of threads [Least is 1 Threads]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            threads_state_error = True
            os.close()

    except:
        if threads_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of threads' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    threads += str(input_threads)
    print(bcolors.OKGREEN + 'Set Threads for Plotting : ' +
          str(input_threads) + ' per plot' + bcolors.ENDC)

### Not Fix
def get_delay_to_creat_setup():
    print(
        f'\nPlease Enter time of {bcolors.OKGREEN}delay to create new Plot{bcolors.ENDC} [Default is 15 minute]')
    global delay_time
    delay_time = '-u '
    input_delay_time = input()
    if input_delay_time == '':
        input_delay_time = int(128)

    delay_time_state_error = False
    try:
        input_delay_time = int(input_delay_time)

        if input_delay_time < 32 or input_delay_time > 128:
            print(
                bcolors.FAIL + 'Error, Please enter a number of delay_time [32-128]' + bcolors.ENDC)
            input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
            delay_time_state_error = True
            os.close()

    except:
        if delay_time_state_error == True:
            os.close()
        print(bcolors.FAIL +
              'Error, Please enter Only a number of delay time' + bcolors.ENDC)
        input(bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)
        exit()
    delay_time += str(input_delay_time)
    print(bcolors.OKGREEN + 'Setup number Bucket : ' +
          str(input_delay_time) + bcolors.ENDC)

def start_create_plot():

    get_K_size_setup()
    get_Bucket_setup()
    get_threads_setup()
    get_ram_setup()
    get_plot_directory_setup()
    get_plot_count_setup()
    #get_delay_to_creat_setup()

    print(bcolors.FAIL + '\nplease don\'t close this windows' + bcolors.ENDC)

    for i in range(plot_range):

        terminal_command = f'start /wait cmd /c {chia}'
        #terminal_command = f'start powershell.exe -NoExit {chia}'

        plot_command = terminal_command + \
            f' plots create {K_size} {ram} {threads} {plot_count} {Bucket} -t {temp_list[i]} -d {final_dir}'
        print(plot_command)
        #subprocess.call(plot_command, shell=True)
        i += 1
        time.sleep(1200)

    print(bcolors.OKGREEN + 'You can close this windows now' + bcolors.ENDC)
    input(bcolors.OKGREEN + "Press Enter to continue..." + bcolors.ENDC)

# Main Program #
print_info()
chia_get_version()
start_create_plot()

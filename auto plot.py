import subprocess
import time
import os
import psutil

main_command = 'start powershell.exe -NoExit C:\\Users\\' + (os.getlogin()) + '\\AppData\\Local\\chia-blockchain\\app-1.1.5\\resources\\app.asar.unpacked\\daemon\\chia'
temp_list = []
Drive_list = []
Drive_size = []
Drive_code = []
Temp_list_PlotCount = []
Temp_list_Dir = []

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
def GetPcInfo() :
    def toGB(bytes):
        return '%.2f' %(bytes/(1024**3))
        

    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    print(bcolors.OKBLUE + "-"*20, "Scanning Your PC", "-"*20 + bcolors.ENDC)
    print(bcolors.HEADER + '\nCPU :' + bcolors.ENDC)
    # number of cores
    print("     Cores:", psutil.cpu_count(logical=False))
    print("     Threads:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"     Max clock: {cpufreq.max:.2f}Mhz")
    threads_inFunc = int(psutil.cpu_count(logical=True))

    print(bcolors.HEADER + '\nRAM :' + bcolors.ENDC)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"     Total: {toGB(svmem.total)}" + ' GB')
    print(f"     Available: {toGB(svmem.available)}" + ' GB')
    #print(f"Used: {get_size(svmem.used)}")
    ram_inFunc = toGB(svmem.total)

    # Disk Information
    print(bcolors.HEADER + "\nDisk Drive :" + bcolors.ENDC)
    print("     Partitions info:")
    # get all disk partitions
    part_count = 0
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"      - Drive: {partition.device}")
        Drive_list.append(partition.device)
        #print(f"  Mountpoint: {partition.mountpoint}")
        #print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            print('Error, No Permission to scan Partition, Try to run as Adminstrator')
            continue
        print(f"         |-Total Size: {toGB(partition_usage.total)} GB")
        print(f"         |-Free Space: {toGB(partition_usage.free)} GB\n")
        Drive_size.append(toGB(partition_usage.free))
        Drive_code.append(part_count)
        part_count += 1
        #print(f"  Used: {get_size(partition_usage.used)}")
        #print(f"  Free: {get_size(partition_usage.free)}")
        #print(f"  Percentage: {partition_usage.percent}%")

    print("Is this Right?, Enter \"Yes\" to Confirm or Enter \"No\" to Enter Your PC spec Manually")
    Confirm_ = input()
    if Confirm_ == 'Yes':
        global threads_
        global ram_
        threads_ = int(threads_inFunc)
        ram_ = float(ram_inFunc)
    elif Confirm_ == 'No':
        print('Please Enter your threads of CPU')
        threads_ = int(input())
        print('Please Enter your total Ram size (GB)')
        ram_ = int(input())
    else :
        print(bcolors.FAIL + 'Error, please Try again.' + bcolors.ENDC)
        input("Press Enter to continue...")
        exit()

    print('\bPlease Enter your K-size' + bcolors.OKGREEN + ' (Default is 32)' + bcolors.ENDC)
    K_size = input()
    if K_size == '' : K_size = 32
    
    global TempSize
    #Tempolary size
    if K_size == 32 : TempSize = 256.6
    elif K_size == 33 : TempSize = 550
    elif K_size == 34 : TempSize = 1118
    elif K_size == 35 : TempSize = 2335
    else : TempSize = 256.6
    #test
    TempSize = 30


    print(bcolors.OKGREEN + '\nUse ' + str(threads_) + ' threads and ' + str(ram_) + ' GB of Ram for Plotting K' + str(K_size )+ '\n' + bcolors.ENDC)
    print('List of drive :')
    print(bcolors.OKGREEN + '  code  |  partition  |  Size' + bcolors.ENDC)
    for i in range(len(Drive_list)):
        print(bcolors.OKGREEN+'   ' + str(Drive_code[i]) + '    |     ' + Drive_list[i] + '     | ' + Drive_size[i] + bcolors.ENDC); i+1


def plotting_setting() :
    Maximum_plot_tempdir = 0

    print('\nHow many Tempolary Directory Partition you want to use for Plotting?')
    Tempdrive_total = int(input())
    if Tempdrive_total > len(Drive_list) or Tempdrive_total <= 0:
        print(bcolors.FAIL + 'Error: Wrong Number, please Try again.' + bcolors.ENDC)
        input("Press Enter to continue...")
        exit()

    for i in range(Tempdrive_total):
        print('\nPlease Enter code of Tempolary Directory Partition ' + str(i+1))
        print('From this list '+ str(Drive_code))
        _code_ = int(input())

        if _code_ not in Drive_code :
            print(bcolors.FAIL + 'Error: Wrong Tempolary Directory Partition code, please Try again.' + bcolors.ENDC)
            input("Press Enter to continue...")
            exit()
        _temp_count_ = int(float(Drive_size[_code_]) / TempSize)

        print(bcolors.OKGREEN + '\nLocation of Tempolary directory ' + str(i+1) + ' is \" ' + Drive_list[_code_] + ' \"' + bcolors.ENDC)
        print(bcolors.OKGREEN + 'Total Tempolary directory of Partition ' + str(i+1) + ' is ' + str(_temp_count_) + bcolors.ENDC)
        print('Please enter \'Ok\' to continue .\n')

        if input() != 'Ok':
            print(bcolors.FAIL + 'Error: input is wrong please Try again.' + bcolors.ENDC)
            break
        
        Maximum_plot_tempdir += _temp_count_
        Temp_list_PlotCount.append(_temp_count_)
        Temp_list_Dir.append(Drive_list[_code_])
        print(bcolors.OKGREEN + 'Set Tempolary directory of ' + str(Temp_list_Dir[i]) + ' Succesfully' + bcolors.ENDC)
        i+1
    
    print('\nPlease Enter code of Final Directory Partition ' + str(i+1))
    print('From this list '+ str(Drive_code))
    _code_ = int(input())
    if _code_ not in Drive_code :
            print(bcolors.FAIL + 'Error: Wrong Tempolary Directory Partition code, please Try again.' + bcolors.ENDC)
            input("Press Enter to continue...")
            exit()
    if _code_ in Drive_code :
        global final_dir
        final_dir = (Drive_list[_code_])

    # for Debug
    #print(Temp_list_Dir)
    #print(Temp_list_PlotCount)
    Maximum_plot_threads = int(threads_/2)
    Maximum_plot_ram =  int(ram_/4)+1

    global final_temp_count
    final_temp_count = Maximum_plot_tempdir
    if Maximum_plot_threads < final_temp_count : final_temp_count = Maximum_plot_threads
    if Maximum_plot_ram < final_temp_count : final_temp_count = Maximum_plot_ram
    if Maximum_plot_tempdir < final_temp_count : final_temp_count = Maximum_plot_tempdir
    
    print(bcolors.HEADER + '\nMaximum Number of plotting in the same time:' + bcolors.ENDC)
    print('   by Drive size  : ' + str(Maximum_plot_tempdir))
    print('   by Threads     : ' + str(Maximum_plot_threads))
    print('   by Ram         : ' + str(Maximum_plot_ram))
    print(bcolors.OKGREEN + '\nYour Pc can Create ' + str(final_temp_count) + ' plot in the same time\n' + bcolors.ENDC)
     
    plot_range = final_temp_count

    for i in range(plot_range):
        plot_command = main_command + ' plots create -k 32 -b 4000 -r 2 -t ' + Temp_list_Dir[i] + ' -d ' + final_dir
        print('\n' + plot_command)
        #subprocess.call(plot_command, shell=True)
        i+= 1
        time.sleep(2)

GetPcInfo()
plotting_setting()
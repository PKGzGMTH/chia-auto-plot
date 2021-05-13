show_PlotCount = ''
total_temp_count = int(0)

def input_resource():

    print('\bPlease enter the Thread count of your CPU.')
    cpu = int(input())

    print('\bPlease Enter your RAM capacity(GB)')
    ram = int(input())

    print('\bPlease Enter your Number K-size (Default is 32)')
    K_size = input()
    if K_size == '' : K_size = 32
    
    #Tempolary size
    if K_size == 32 : Temp_size = 256.6
    elif K_size == 33 : Temp_size = 550
    elif K_size == 34 : Temp_size = 1118
    elif K_size == 35 : Temp_size = 2335
    else : Temp_size = 256.6

    #Calculate how much you can plotting in the same time
    print('\bPlease Enter your Number of M.2 or Tempolary Directory (GB)')
    Temp_drive_count = int(input())
    for i in range(Temp_drive_count):
        i+=1
        print('\bPlease Enter Capacity of Tempolary Drive' + str(i)+ ' (GB)')
        Temp_MaxPlotCount = int(int(input()) / int(Temp_size))
        show_PlotCount += '\nMaximum Tempolary Directory of Drive'+ str(i) + ' is :' + str(Temp_MaxPlotCount)
        total_temp_count += Temp_MaxPlotCount

def Plot_plan() :
    print()

def print_result() :
    #temp count per Tempolary Drive
    print(show_PlotCount)

    #total temp count
    print(total_temp_count)

input_resource()
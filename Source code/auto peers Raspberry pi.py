from datetime import datetime
import time, subprocess, requests

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

def mainFunction():
    # Start Get and Add Node
    chia_exec_path = '/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon/chia'
    while True:
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("[" + str(timeNow) + "]" + bcolors.OKGREEN + "[System]" + bcolors.ENDC + " Fetch new node from iDisk")
        chia_api_node = requests.get('https://chia-thailand.com/nodes/api.php?t' + str(time.time()))
        chia_node_json = chia_api_node.json()
        for node_chia in chia_node_json:
            argument_chia = " show -a " + str(node_chia["IP"])
            subprocess.Popen(chia_exec_path + argument_chia, shell=True)
            time.sleep(2) # CPU fixed
        print("[" + str(timeNow) + "]" + bcolors.OKGREEN + "[System]" + bcolors.ENDC +  "Finished Connect to Full node, Reconnect all node in 120 Second")
        time.sleep(120)

mainFunction()
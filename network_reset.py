import subprocess as sp
import time
import ctypes
import sys

def run_command(command):
    sp.run(command, shell=True)

def check_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def network_reset():
    if not check_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    commands = [
        ["netsh winsock reset", 3],
        ["netsh int ip reset", 3],
        ["ipconfig /release", 5],
        ["ipconfig /renew", 3],
        ["ipconfig /flushdns", 25.5]
    ]
    
    for cmd, sleep_time in commands:
        run_command(cmd)
        time.sleep(sleep_time)

network_reset()

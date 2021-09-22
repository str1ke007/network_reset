import subprocess as sp
import time


def network_reset():
    sp.call(["netsh", "winsock", "reset"])
    time.sleep(3)
    sp.call(["netsh", "int", "ip", "reset"])
    time.sleep(3)
    sp.call(["ipconfig", "/release"])
    time.sleep(5)
    sp.call(["ipconfig", "/renew"])
    time.sleep(3)
    sp.call(["ipconfig", "/flushdns"])
    time.sleep(25.5)
    print("[+] Network Reset Successfully")


network_reset()

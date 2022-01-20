import os
import time
import requests


def restartRedSocks(): 
    os.system("killall -9 redsocks")
    os.system("redsocks -c cf.conf")    

def checkRedsocksStatus():
    while(True):
        try:
            r = requests.get("https://www.google.com", verify=False, timeout=3) 
        except:
            restartRedSocks()
            time.sleep(10)
            checkRedsocksStatus()

if __name__ == "__main__":      
    checkRedsocksStatus()
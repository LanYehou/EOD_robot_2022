import time
import _thread

def th1():
    while True:
            print ('txxx')
            time.sleep(0.1)
def th2():
    while True:
            print ('taaa')
            time.sleep(0.1)
            
_thread.start_new_thread(th1,(),)
_thread.start_new_thread(th2,(),)

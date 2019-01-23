#!/bin/python

########################encrypt function########################################################
def  en(flag,key):
        code=[]
        h=[]
        k=[]
        k16=[]
        akey=[]
        for char in flag:
                key = ((key*13)+37) %256
                char = ord(char) ^ key %256
                char +=3
                code.append(chr(char))
                h.append(hex(char))
                k.append(key)
                k16.append(hex(key))
                akey.append(chr(key%256))
        print "original: " + flag +"\n" +  "ascii:    " + str(''.join(code)) + "\n" + "hex:      " + str(''.join(h)) + "\n"+ "keysb10:  " + str(k) + "\n"+ "keysb16:  " + str(k16)  + "\n" + "keyascii: " + str(akey)
        return code
##################################################################################################


##########################decrypt function########################################################
def dec(encoded):
        for key in range(0,255):
                f=[]
                for char in encoded:
#                       char = ord(char) # comment out when using  decrypt parameters
                        key = ((key*13)+37)%256
                        flag = (char-3)^key %256
                        f.append(chr(flag))
                print ''.join(f)
        return None
##################################################################################################

###############################Parameters when using encrypt######################################
#flag = "test"
#key=0
#encoded=en(flag,key)
#print dec(encoded)
#print en(flag,key)
##############################Parameters when using decrypt#######################################


#encoded=[0x49,0xd7,0x5b,0x25]
#encoded = [0x0f, 0xa8, 0x9f, 0xfe, 0x7a, 0xd6, 0xe2, 0x08, 0xae, 0x2b, 0x5f, 0x53, 0x25, 0x9a]
encoded = [0x3c, 0xf7, 0xbf, 0x3c, 0xd9, 0x53, 0x49, 0x57, 0x33, 0x27, 0x68, 0xba, 0x70, 0x28, 0x65]
print dec(encoded)

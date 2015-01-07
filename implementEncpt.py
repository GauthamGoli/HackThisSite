import hashlib

teststr = '99Z-KH5-OEM-240-1.1\nQGG-V33-OEM-0B1-1.1\nZ93-Z29-OEM-BNX-1.1\nIQ0-PZI-OEM-PK0-1.1\nUM4-VDL-OEM-B9O-1.1\nL0S-4R2-OEM-UQL-1.1\nJBL-EYQ-OEM-ABB-1.1\nNL1-3V3-OEM-L4C-1.1\n7CQ-1ZR-OEM-U3I-1.1\nXX0-IHL-OEM-5XK-1.1\nKJQ-RXG-OEM-TW8-1.1\nOZR-LW1-OEM-5EM-1.1\n0B8-6K5-OEM-EFN-1.1\nOE2-20L-OEM-SSI-1.1\n0ME-HAE-OEM-9XB-1.1'

def md5(text):
	m=hashlib.md5()
	m.update(text)
	return m.hexdigest()

def evaltotal(strMD5):
    intTotal = 0
    for letter in strMD5:
        intTotal += int(letter, 16)
    return intTotal

def encrypt(string,password):
    passwordMD5 = md5(password)
    MD5total = evaltotal(passwordMD5)
    strlen = len(string)
    Encrypted = []
    for i in range(0,strlen):
        print i
        Encrypted.append(ord(string[i])+int(passwordMD5[i%32], 16)-MD5total)
        print ord(string[i]),int(passwordMD5[i%32], 16),MD5total
        MD5total=evaltotal(md5(string[:i+1])[:16]+md5(str(MD5total))[:16])
        print md5(string[:i+1])[:16], md5(str(MD5total))[:16]
    #return Encrypted
# test decrypt(not exactly) code:


        

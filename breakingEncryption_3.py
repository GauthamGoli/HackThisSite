# Program written to reverse that encryption algorithm in HTS Programming CHALLENGE 3


import hashlib
# global variables
hexMap={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
ordstr=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
strpass=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def md5(text):
	m=hashlib.md5()
	m.update(text)
	return m.hexdigest()

def evaltotal(strMD5):
    intTotal = 0
    for letter in strMD5:
        intTotal += int(letter, 16)
    return intTotal

def getnextkey(enc,serials,pas,intmd5):
        # returns the next character in serials based on given encrypted element, current password, current md5total
        if len(pas)==32:
                c=len(serials)
                if c in [3, 7, 11, 15, 23, 27, 31, 35, 43, 47, 51, 55, 63, 67, 71, 75, 83, 87, 91, 95]:
                        if enc!=ord('-')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return '-'
                elif c in range(8,101,20):
                        if enc!=ord('O')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return 'O'
                elif c in range(9,101,20):
                        if enc!=ord('E')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return 'E'
                elif c in range(10,101,20):
                        if enc!=ord('M')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return 'M'
                elif c in range(16,101,20):
                        if enc!=ord('1')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return '1'
                elif c in range(17,101,20):
                        if enc!=ord('.')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return '.'
                elif c in range(18,101,20):
                        if enc!=ord('1')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return '1'
                elif c in range(19,101,20):
                        if enc!=ord('\n')+int(pas[(c)%32], 16)-intmd5:
                                return ['abort']
                        #return '\n'
                
                return [chr(enc+intmd5-int(pas[(c)%32], 16))]
        elif len(pas)<32:
                c=len(pas)
                if c in range(3,101,4):
                        return ['-']
                elif c in range(8,101,20):
                        return ['O']
                elif c in range(9,101,20):
                        return ['E']
                elif c in range(10,101,20):
                        return ['M']
                elif c in range(16,101,20):
                        return ['1']
                elif c in range(17,101,20):
                        return ['.']
                elif c in range(18,101,20):
                        return ['1']
                elif c in range(19,101,20):
                        return ['\n']
                else:
                        bruted1=[] # data structure of bruted1 is [ascii code of serial character, decimal value of hex char of password]
                        for no1 in ordstr:
                                for pas1 in strpass:
                                        if(enc==no1+pas1-intmd5):
                                                bruted1.append([no1,pas1])
                        return bruted1
                                                
                                                
                                                
                        
                        
                
                

def newintmd5(serials,intmd5total):
        return evaltotal(md5(serials)[:16]+md5(str(intmd5total))[:16])

def brute(intext):
        enc1 = intext.split(' ')
        serials = ''
        password = ''
        intmd5total=range(0,481)
        brutestick=[]  # data structure of brutestick=[[ascii code, decimal value of hex character in password , intmd5totoal],.....]
        enc=[]
        for entry in enc1:
                enc.append(int(entry))
        element=enc[0]
        for no in ordstr:
                for pas in strpass:
                        for intmd5 in intmd5total:
                                if element == no + pas - intmd5:
                                        brutestick.append([no,pas,intmd5])
        #print brutestick
        for entry in brutestick:
                #print entry,'run'
                #serials0,passsword0 = serials,password
                serials0=''
                password0=''
                serials0+=chr(entry[0])
                password0+=hexMap[entry[1]]
                #serials0,password0 = (chr(entry[0])),(hexMap[entry[1]])
                intmd5total0 = newintmd5(serials0,entry[2])
                for entry1 in getnextkey(enc[1],serials0,password0,intmd5total0):
                        serials1,password1,intmd5total1 =serials0,password0,intmd5total0
                        serials1,password1 = (serials1+chr(entry1[0])),(password1+hexMap[entry1[1]])
                        intmd5total1 = newintmd5(serials1,intmd5total1)
                        for entry2 in getnextkey(enc[2],serials1,password1,intmd5total1):
                                serials2,password2,intmd5total2 = serials1,password1,intmd5total1
                                serials2,password2 = (serials2+chr(entry2[0])),(password2+hexMap[entry2[1]])
                                intmd5total2 = newintmd5(serials2,intmd5total2)
                                serials2+='-'
                                if((enc[3]-ord('-')+intmd5total2)<0 or (enc[3]-ord('-')+intmd5total2)>15):
                                        continue
                                else:
                                        password2+=hexMap[(enc[3]-ord('-')+intmd5total2)]
                                        intmd5total2 = newintmd5(serials2,intmd5total2)
                                        for entry3 in getnextkey(enc[4],serials2,password2,intmd5total2):
                                                serials3,password3,intmd5total3 = serials2,password2,intmd5total2
                                                serials3,password3 = (serials3+chr(entry3[0])),(password3+hexMap[entry3[1]])
                                                intmd5total3 = newintmd5(serials3,intmd5total3)
                                                for entry4 in getnextkey(enc[5],serials3,password3,intmd5total3):
                                                        serials4,password4,intmd5total4 = serials3,password3,intmd5total3
                                                        serials4,password4 = (serials4+chr(entry4[0])),(password4+hexMap[entry4[1]])
                                                        intmd5total4 = newintmd5(serials4,intmd5total4)
                                                        for entry5 in getnextkey(enc[6],serials4,password4,intmd5total4):
                                                                serials5,password5,intmd5total5 = serials4,password4,intmd5total4
                                                                serials5,password5 = (serials5+chr(entry5[0])),(password5+hexMap[entry5[1]])
                                                                intmd5total5,a = newintmd5(serials5,intmd5total5),7
                                                                for letter in '-OEM-':                                                                        
                                                                        if((enc[a]-ord(letter)+intmd5total5)<0 or (enc[a]-ord(letter)+intmd5total5)>15):
                                                                                break
                                                                        else:
                                                                                serials5+=letter
                                                                                password5+=hexMap[(enc[a]-ord(letter)+intmd5total5)]
                                                                                intmd5total5,a = newintmd5(serials5,intmd5total5),(a+1) #final value of a is 12
                                                                if len(serials5)<12:
                                                                        continue
                                                                #print a,'supposed to be 12',serials5,'supposed to end with -OEM- passing on'
                                                                for entry6 in getnextkey(enc[a],serials5,password5,intmd5total5):                                                                        
                                                                        serials6,password6,intmd5total6 = serials5,password5,intmd5total5
                                                                        serials6,password6 = (serials6+chr(entry6[0])),(password6+hexMap[entry6[1]])
                                                                        intmd5total6,a = newintmd5(serials6,intmd5total6),(13) # a= 13 at end of loop
                                                                        for entry7 in getnextkey(enc[a],serials6,password6,intmd5total6):
                                                                                serials7,password7,intmd5total7 = serials6,password6,intmd5total6
                                                                                serials7,password7 = (serials7+chr(entry7[0])),(password7+hexMap[entry7[1]])
                                                                                intmd5total7,a = newintmd5(serials7,intmd5total7),(14) # a = 14
                                                                                for entry8 in getnextkey(enc[a],serials7,password7,intmd5total7):
                                                                                        serials8,password8,intmd5total8=serials7,password7,intmd5total7
                                                                                        serials8,password8 = (serials8+chr(entry8[0])),(password8+hexMap[entry8[1]])
                                                                                        intmd5total8,a = newintmd5(serials8,intmd5total8),(15) # a = 15
                                                                                        for letter in '-1.1\n':
                                                                                                if((enc[a]-ord(letter)+intmd5total8)<0 or (enc[a]-ord(letter)+intmd5total8)>15):
                                                                                                        break
                                                                                                else:
                                                                                                        serials8+=letter
                                                                                                        password8+=hexMap[(enc[a]-ord(letter)+intmd5total8)]
                                                                                                        intmd5total8,a = newintmd5(serials8,intmd5total8),(a+1) # final a =20
                                                                                        if len(serials8)<20:
                                                                                                continue
                                                                                        for entry9 in getnextkey(enc[a],serials8,password8,intmd5total8):
                                                                                                serials9,password9,intmd5total9 = serials8,password8,intmd5total8
                                                                                                serials9,password9 = (serials9+chr(entry9[0])),(password9+hexMap[entry9[1]])
                                                                                                intmd5total9,a = newintmd5(serials9,intmd5total9),(21) #a =21
                                                                                                for entry10 in getnextkey(enc[a],serials9,password9,intmd5total9):
                                                                                                        serials10,password10,intmd5total10 = serials9,password9,intmd5total9
                                                                                                        serials10,password10 = (serials10+chr(entry10[0])),(password10+hexMap[entry10[1]])
                                                                                                        intmd5total10,a = newintmd5(serials10,intmd5total10),(22) #a=22
                                                                                                        for entry11 in getnextkey(enc[a],serials10,password10,intmd5total10):
                                                                                                                serials11,password11,intmd5total11=serials10,password10,intmd5total10
                                                                                                                serials11,password11 = (serials11+chr(entry11[0])),(password11+hexMap[entry11[1]])
                                                                                                                intmd5total11,a = newintmd5(serials11,intmd5total11),(23) #a=23
                                                                                                                serials11+='-'
                                                                                                                if((enc[a]-ord('-')+intmd5total11)<0 or (enc[a]-ord('-')+intmd5total11)>15):
                                                                                                                        continue
                                                                                                                else:
                                                                                                                        password11+=hexMap[(enc[a]-ord('-')+intmd5total11)]
                                                                                                                        intmd5total11,a = newintmd5(serials11,intmd5total11),(24) #a =24
                                                                                                                        for entry12 in getnextkey(enc[a],serials11,password11,intmd5total11):
                                                                                                                                serials12,password12,intmd5total12=serials11,password11,intmd5total11
                                                                                                                                serials12,password12 = (serials12+chr(entry12[0])),(password12+hexMap[entry12[1]])
                                                                                                                                intmd5total12,a = newintmd5(serials12,intmd5total12),(25)#a=25
                                                                                                                                for entry13 in getnextkey(enc[25],serials12,password12,intmd5total12):
                                                                                                                                        serials13,password13,intmd5total13=serials12,password12,intmd5total12
                                                                                                                                        serials13,password13 = (serials13+chr(entry13[0])),(password13+hexMap[entry13[1]])
                                                                                                                                        intmd5total13,a = newintmd5(serials13,intmd5total13),(26) #a=26
                                                                                                                                        for entry14 in getnextkey(enc[26],serials13,password13,intmd5total13):
                                                                                                                                                #print 'almost there'
                                                                                                                                                serials14,password14,intmd5total14=serials13,password13,intmd5total13
                                                                                                                                                serials14,password14 = (serials14+chr(entry14[0])),(password14+hexMap[entry14[1]])
                                                                                                                                                intmd5total14,a=newintmd5(serials14,intmd5total14),(27) #a=27
                                                                                                                                                for letter1 in '-OEM-':
                                                                                                                                                        if((enc[a]-ord(letter1)+intmd5total14)<0 or (enc[a]-ord(letter1)+intmd5total14)>15):
                                                                                                                                                                break
                                                                                                                                                        else:
                                                                                                                                                                serials14+=letter1
                                                                                                                                                                password14+=hexMap[(enc[a]-ord(letter1)+intmd5total14)]
                                                                                                                                                                intmd5total14,a = newintmd5(serials14,intmd5total14),(a+1) #a= 32
                                                                                                                                                if len(serials14)<32:                                                                                                                                                        
                                                                                                                                                        continue                                                                                                                                                
                                                                                                                                                while(getnextkey(enc[a],serials14,password14,intmd5total14)!=['abort']):                                                                                                                                                
                                                                                                                                                        serials14+=getnextkey(enc[a],serials14,password14,intmd5total14)[0]                                                                                                                                                        
                                                                                                                                                        intmd5total14,a = newintmd5(serials14,intmd5total14),(a+1)
                                                                                                                                                        if(len(serials14)==100):
                                                                                                                                                                return serials14
                                                                                                                                                        
                                                                                                                                                                   
      

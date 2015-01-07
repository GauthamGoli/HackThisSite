""" This program has been written to complete the programming challenge 1
in the HTS. Much of it is self explanatory . Itertools has been included
to scramble the scrambled words"""



from itertools import *

wordfile = open("wordlist.txt","r")

dictionary = wordfile.read()

words = dictionary.split()



def unscramble():
    wordfile2 = open("input.txt","r")
    dict2 = wordfile2.read()
    list1 = dict2.split()
    for word in list1:
        permuted = list(itertools.permutations(list(word)))
        for entry in permuted:
            tocheck = ''.join(entry)
            if(tocheck in words):
                print tocheck+','
                break
            
    

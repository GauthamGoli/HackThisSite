def s(text):
    for char in text:
        if ord(char)<=47:
            delimiter=char
            break
    new=text.split(delimiter)
    shift=new.pop()
    shift=int(shift)
    decrypted=''
    for char in new:
        decrypted+=chr(int(char)-shift)
    return decrypted
        

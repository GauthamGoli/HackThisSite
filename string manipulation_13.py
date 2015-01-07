
"""
This program has been written to solve the programming challenge 12 of HTS.
To copy the output directly to clipboard I have used pyperclip module and pyperclip.copy() function.
"""
def m(string1):
    

#string1='qps9tb@v4v47bqk2axdc4nqt$zb$7ln2$$snd8mv$zr#@4kla41#aaard3vj5dlye@ivbzlw2f5qdsvy4wg#umkf4ibgueir54m043soxl9gfu5em3qzyk4l5u2nct2kmekewxhqmbq?#zynerptw9ctek5wn?5@019x1qm97m2wfdvzf14i991k#0voxtyyyftbfcdwrhn57pfd5okosqjag3k5jcxfd497$006p4yq8f22q5z1gjlkpkonb#osxc23#5bj4mwrbe63vjtxnb54oni7wz@hv18l#wzhxb#78ua0ue0vzuwnnno7?0fpdxc56nsbor5j2?l40zzs?6pf9sx$8vegudlz75#p8kvryx@pl?#rrxxnaxll9p$#b9qmjqacb?18m5@kke4oubixi4fwyyqczj5n25zg49uspjqsd#@#3dw84tkjeil5q10cikesjlfufuh@@g?wb7klqvx599a#phe8fdl7d1#z$3y9n3a#ziym3tb#dp7jd32rhiz1favee7xj8c?exxphmy275z1d8t@8q@9smb$sem?rcfn4gt17vqs@f5d?7d$9klanotje0gyhh3g?$@0c?y8mo8yf45@pnscf3ii0yn2$j@4@oqgmxgj9lke4'
    #broke = string1.split()
    sump,sumc=0,0
    key=''
    for char in string1:
        if char=='0' or char=='1':
            continue        
        if (50<=ord(char)<=57):
            if char=='2' or char=='3' or char=='5' or char=='7':
                sump+=int(char)
            else:
                sumc+=int(char)
        else:
            if len(key)==25:
                continue
            key+=chr(ord(char)+1)
    return key+str((sump*sumc))


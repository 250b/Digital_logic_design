minterm=[4,11,0,1,2,3,4,5,6,10,11,13,14]  
size = minterm[0]
minterm_size = minterm[1]
pi={}
mainlist={}
checklist={}
newlist={}
list2={}

#mainlist 생성
for i in range(2,minterm_size+2):
    zero_num=size-len(bin(minterm[i])[2:])
    list_ele='0'*zero_num+bin(minterm[i])[2:]
    mainlist[list_ele]=[minterm[i]]

#pi
while True:
    keylist=mainlist.keys()
    keylist = list(keylist)
    for i in range(0,minterm_size):
        for j in range(0,minterm_size):
            string1=keylist[i]
            string2=keylist[j]
            count=0
            for k in range(0,size):
                if(string1[k]==string2[k]):    
                    count+=1
                else:
                    index=k 
            if(count==size-1):    
                if(string1 not in checklist):
                    checklist[string1]=mainlist.get(string1)
                if(string2 not in checklist):
                    checklist[string2]=mainlist.get(string2)
                obj = string1[:index]+'2'+string1[index+1:]
                if(obj not in newlist):    
                    valuelist=list(set(mainlist.get(string1)+(mainlist.get(string2))))
                    newlist[obj]=sorted(valuelist)
    for x in keylist:
        if(x not in checklist):
            pi[x]=mainlist.get(x)
    mainlist.clear()
    for y in newlist:
        mainlist[y]=newlist.get(y)
    minterm_size = len(mainlist)
    checklist.clear()
    newlist.clear()
    if (len(mainlist)==0):
        break
    
pi_keys=list(pi.keys())
pi_keys=sorted(pi_keys)
pi_list=[]
for i in pi_keys:
    pi_list.append((i.replace('2','-')))

print("<pi>\n",dict(sorted(pi.items())))
print("\n")



coldic={}
rowdic=pi

#coldic 생성
minterm_list=[]
for x in rowdic.values():
    minterm_list=list(set(minterm_list+(x)))

value_list=[]
for minterm_key in minterm_list:
    for r in rowdic:
        if(minterm_key in rowdic.get(r)):
            value_list.append(r)
    coldic[minterm_key]=value_list
    value_list=[]
print("<rowdic>\n", dict(sorted(rowdic.items())))
print("\n")
print("<coldic>\n", dict(sorted(coldic.items())))
print("\n")

epi=[]
epi_full_list=[]
loop_count=0
while 1:
    loop_count+=1
    print("loop_count: ",loop_count)

    #epi 탐색
    epi_list=[]
    for x in coldic:
        if(len(coldic.get(x))==1)& (coldic.get(x)[0] not in epi_list):
            epi_list.append(coldic.get(x)[0])
            epi_full_list.append(coldic.get(x)[0])
    
    rowdic_get=[]
    for y in epi_list:
        for r in rowdic.get(y):
            rowdic_get.append(r)
        for g in rowdic_get:
            if(g in coldic.keys()):
                del coldic[g]
            for k in rowdic.keys():
                if g in rowdic.get(k):
                    rowdic.get(k).remove(g)
        rowdic_get=[]
        del rowdic[y]
    row_check={}
    col_check={}
    for x in rowdic:
        row_check[x]=rowdic.get(x)
    for x in coldic:
        col_check[x]=coldic.get(x)
    print("<epi_list>")    
    print(epi_list)
    print("\n")
    print("<rowdic>\n", dict(sorted(rowdic.items())))
    print("\n") 
    print("<coldic>\n", dict(sorted(coldic.items())))
    print("\n")
        

    if(rowdic=={}):
        print("break!")
        epi_full_list=sorted(epi_full_list)
        for i in epi_full_list:
            epi.append(i.replace('2','-'))
        break
    
    #column dominance
    remove_list=[]
    for x in coldic:
        for y in coldic:
            if(x!=y):
                if list(sorted(set(coldic.get(x)) & set(coldic.get(y))))==list(sorted(set(coldic.get(y)))):
                    if list(sorted(set(coldic.get(x)) & set(coldic.get(y))))==list(sorted(set(coldic.get(x)))):
                        print(x, " dominate ", y)
                        if((x not in remove_list) & (y not in remove_list)):
                            remove_list.append(x)
                    else:
                        print(x, " dominate ", y)
                        if (x not in remove_list):
                            remove_list.append(x)
    
    coldic_get=[]                 
    for x in remove_list:
        for r in coldic.get(x):
            coldic_get.append(r)
        for y in coldic_get:
            if(x in rowdic.get(y)):
                rowdic.get(y).remove(x)
        coldic_get=[]
        del coldic[x]
    print("col_remove: ", remove_list)
    print("\n")
    print("<rowdic>\n", dict(sorted(rowdic.items())))
    print("\n") 
    print("<coldic>\n", dict(sorted(coldic.items())))
    print("\n")
        

    #row dominance
    remove_list=[]
    for x in rowdic:
        for y in rowdic:
            if(x!=y):
                if list(sorted(set(rowdic.get(x))&set(rowdic.get(y))))==list(sorted(set(rowdic.get(y)))):
                    if list(sorted(set(rowdic.get(x))&set(rowdic.get(y))))==list(sorted(set(rowdic.get(x)))):
                        print(x, " dominate ", y)
                        if((x not in remove_list) & (y not in remove_list)):
                            remove_list.append(y)
                    else:
                        if( y not in remove_list):
                            remove_list.append(y)
                            print(x, " dominate ", y)
    rowdic_get=[]
    for x in remove_list:
        for r in rowdic.get(x):
            rowdic_get.append(r)
        for y in rowdic_get:
            if(x in coldic.get(y)):
                coldic.get(y).remove(x)
        rowdic_get=[]
        del rowdic[x]
    print("row_remove: ", remove_list)
    print("\n")
    print("<rowdic>\n", dict(sorted(rowdic.items())))
    print("\n") 
    print("<coldic>\n", dict(sorted(coldic.items())))
    print("\n")
        
    if((rowdic==row_check) & (coldic==col_check)):
        epi_full_list=sorted(epi_full_list)
        for i in epi_full_list:
            epi.append(i.replace('2','-'))
        print("break!")
        print(epi)
        break
    
print("answer: ", pi_list + ["EPI"] + epi)

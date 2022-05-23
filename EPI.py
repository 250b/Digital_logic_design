def solution(minterm):  
    size = minterm[0] #4
    minterm_size = minterm[1] #7
    pi={}
    mainlist={}
    checklist={}
    newlist={}
    list2={}

    for i in range(2,minterm_size+2):
        zero_num=size-len(bin(minterm[i])[2:])
        list_ele='0'*zero_num+bin(minterm[i])[2:]
        mainlist[list_ele]=[minterm[i]]

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
    answer=[]
    for i in pi_keys:
        answer.append((i.replace('2','-')))

    coldom={}
    rowdom=pi
    minterm_list=[]
    for x in rowdom.values():
        minterm_list=list(set(minterm_list+(x)))
    pi_list=[]
    for y in minterm_list:
        for z in rowdom:
            if(y in rowdom.get(z)):
                pi_list.append(z)
        coldom[y]=pi_list
        pi_list=[]

    epi=[]
    for x in coldom:
        if(len(coldom.get(x))==1):
            obj=coldom.get(x)[0].replace('2','-')
            print(obj)
            epi.append(obj)
    epi=sorted(list(set(epi)))
    answer=answer+["EPI"]+ epi
    return answer

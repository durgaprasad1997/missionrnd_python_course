from heapq import nsmallest
import sys
from collections import OrderedDict


def sortingdictorder(list):
    list.sort()
    list.sort(key=lambda x:x[0].lower())
    return list


def getfval(listoflines):
    listof_fval = []
    for line in listoflines:
        line = line[:len(line) - 1]
        fval = 0
        for alpha in line:
            fval += ord(alpha)
        listof_fval.append(fval)
    return listof_fval

def findfriendword(listof_fval,k=1):
    """listofoutput=[]
    min=10000000
    i=0
    j=0
    print(listof_fval)
    while(i<len(listof_fval)):
        tempval=0
        min=1000000
        while(j<len(listof_fval)):
            if(i!=j):
                tempmin=abs(listof_fval[i]-listof_fval[j])
                if(min>tempmin):
                    min=tempmin
                    tempval=listof_fval[j]
            j+=1
        i+=1

        listofoutput.append(tempval)"""

    listofoutput=[]
    for fval in listof_fval:
        templist=listof_fval.copy()
        templist.remove(fval)

        listofoutput.append(nsmallest(k, templist, key=lambda x: abs(x - fval)))


    return listofoutput

def convertintodict(names,fval,frndfval):
    dictionaryofoutput=dict()
    listofnames=[]
    listoffrnds=[]
    counter=0
    for value in fval:
        listofnames.append(names[fval.index(value)])

    for frnds in frndfval:
        tempfrnds=[]
        for frnd in frnds:
            tempfrnds.append(names[fval.index(frnd)])
        listoffrnds.append(tempfrnds)

    dictionaryofoutput=dict(zip(listofnames,listoffrnds))
    return dictionaryofoutput





def readfromfile(argv):

    listoflines=[]
    listof_fval=[]
    listoffrnd_fval=[]


    with open(argv[0],"r") as filepointer:

        listoflines=filepointer.readlines()
        listoflines.sort()
        listoflines.sort(key=lambda x: x[0].lower())


        #print(listoflines)

        listof_fval=getfval(listoflines)





    if(len(argv)==3):
        kvalue=int(argv[2])
    else:
        kvalue=1
    listoffrnd_fval=findfriendword(listof_fval,kvalue)


    dictionaryofoutput=convertintodict(listoflines,listof_fval,listoffrnd_fval)


    with open(argv[1], "w") as filepointer:

        for key,value in dictionaryofoutput.items():
            key="".join(key)
            key=key[:len(key)-1]
            value=",".join(value)
            value=value.replace("\n"," ")
            """valuestring=""
            for val in value:
                valuestring+=val+","""""


            filepointer.write(key+" : "+value+"\n")








def main(argv):
    readfromfile(argv[1:])



if __name__=="__main__":
    main(sys.argv)

#C:/PythonCourse/interviewtextfile.txt
#C:/PythonCourse/interviewoutput.txt

def get_hcf(arg1,arg2):
    len1=len(arg1)
    len2=len(arg2)
    res=[]
    i=0
    j=0
    while(i<len1):

        while(j<len2):
            if(arg1[i][0]>=arg2[j][0]):
                if (arg1[i][0] == arg2[j][0]):
                    minvalue = min(arg1[i][1], arg2[j][1])
                    res.append((arg1[i][0], minvalue))
                    break
            else:
                break
            j+=1
        i+=1

    return res


def get_lcm(arg1, arg2):
    len1 = len(arg1)
    len2 = len(arg2)
    res = []
    i = 0
    j = 0
    count = 0
    while (i < len1):
        count = 0
        while (j < len2):
            count += 1
            if (arg1[i][0] == arg2[j][0]):

                minvalue = max(arg1[i][1], arg2[j][1])
                res.append((arg1[i][0], minvalue))
                j += 1
                break
            if (arg1[i][0] > arg2[j][0]):
                res.append((arg2[j][0], arg2[j][1]))
                count=0
            if (arg1[i][0] < arg2[j][0]):
                res.append((arg1[i][0], arg1[i][1]))
                break
            j += 1
        if (count == 0):
            res.append((arg1[i][0], arg1[i][1]))


        i += 1
    if (j < len2):
        while (j < len2):
            res.append((arg2[j][0], arg2[j][1]))
            j += 1
    return res


def multiply(arg1,arg2):
    len1 = len(arg1)
    len2 = len(arg2)
    res = []
    i = 0
    j = 0
    count = 0
    while (i < len1):
        count = 0
        while (j < len2):
            count += 1
            if (arg1[i][0] == arg2[j][0]):

                minvalue = (arg1[i][1] + arg2[j][1])
                res.append((arg1[i][0], minvalue))
                j += 1
                break
            if (arg1[i][0] > arg2[j][0]):
                res.append((arg2[j][0], arg2[j][1]))
                count=0
            if (arg1[i][0] < arg2[j][0]):
                res.append((arg1[i][0], arg1[i][1]))
                break
            j += 1
        if (count == 0):
            res.append((arg1[i][0], arg1[i][1]))


        i += 1
    if (j < len2):
        while (j < len2):
            res.append((arg2[j][0], arg2[j][1]))
            j += 1
    return res

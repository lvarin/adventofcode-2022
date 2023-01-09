'''
    Reads a file and does a comparison between the pair of lists
'''

from functools import cmp_to_key
import re

def compare(list1,list2):
    '''
        Python compares lists and lists of lists. It only fails with TypeError if the types do not match. When this happens,
        we only have to recursively, fix the problem. Once fixed, we only need to come back and make the test again for the
        whole (fixed) list of lists
    '''
    #print("Compare %s vs %s" % (list1,list2))

    try:
        if list1<list2:
            return -1
        if list1==list2:
            return 0
        else:
            return 1
    except TypeError:
        # One of the lists or sublists is an int
        for i in range(min(len(list1), len(list2))):
            if isinstance(list1[i], int):
                list1[i]=[list1[i]]
            if isinstance(list2[i], int):
                list2[i]=[list2[i]]
            compare(list1[i],list2[i])
        return compare(list1,list2)

pairs = []
with open('input') as file:
    for line in file:
        line=line.replace('\n','')
        try:
            pairs.append(eval(line))
        except SyntaxError:
            pass

pairs.append([[2]])
pairs.append([[6]])

pairs=sorted(pairs,key=cmp_to_key(compare))

result=1

i=0
for item in pairs:
    i+=1
    #print(i,item)
    if re.match('^\[+(2|6)\]+$',str(item)):
        result*=i

print(result)


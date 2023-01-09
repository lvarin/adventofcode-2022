'''
    Reads a file and does a comparison between the pair of lists
'''

def compare(list1,list2):
'''
    Python compares lists and lists of lists. It only fails with TypeError if the types do not match. When this happens,
    we only have to recursively, fix the problem. Once fixed, we only need to come back and make the test again for the
    whole (fixed) list of lists
'''
    print("Compare %s vs %s" % (list1,list2))

    try:
        if list1<list2:
            return True
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
pair_temp = []
with open('input') as file:
    for line in file:
        line=line.replace('\n','')
        try:
            pair_temp.append(eval(line))
        except SyntaxError:
            pairs.append(pair_temp)
            pair_temp = []

    pairs.append(pair_temp)

#print(pairs)

order=1
solution=0

for pair in pairs:
    print("== Pair %d ==" % order)
    if compare(pair[0], pair[1]):
        solution +=order
        print(order)
    order +=1

print("Total: ",solution)

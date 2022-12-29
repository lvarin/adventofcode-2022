class directory:
    name=''
    parent=None
    kids={}
    files={}

    def __init__(self, name, parent):
        self.name=name
        self.parent=parent
        self.kids={}
        self.files={}

    def __str__(self):
        returnString = "%s (%d) [%d]" % (self.name, len(self.kids.keys()), self.size())
        for key in self.kids.keys():
            returnString =returnString+ "{ %s }" % self.kids[key]

        print("[")
        for key in self.files.keys():
            returnString =returnString+ " %s: %s, " % (key, self.files[key])
        print("]")

        return returnString

    def size(self):
        suma=0
        for key in self.files.keys():
            suma=suma+self.files[key]
        for key in self.kids.keys():
            suma=suma+self.kids[key].size()

        return suma

def cd(_cwd, folder):
    return _cwd.kids[folder]

def printAllSizes(tree):

    if tree.size() <= 100000:
        print("%s: %d" % (tree.name, tree.size()))

    for key in tree.kids.keys():
        printAllSizes(tree.kids[key])

def printMoreThan(tree, mustdel):
    if tree.size() >= mustdel:
        print("%s: %d" % (tree.name, tree.size()))

    for key in tree.kids.keys():
        printMoreThan(tree.kids[key], mustdel)

cwd=directory('/', None)
tree = cwd

with open('input') as file:
    for line in file:
        line=line.replace('\n', '')
        words=line.split(' ')
        if(words[0]=='$'):
            if(words[1]=='cd'):
                if(words[2]=='..'):
                    cwd=cwd.parent
                else:
                    cwd=cd(cwd, words[2])
        elif(words[0]=='dir'):
            cwd.kids[words[1]]=directory(words[1],cwd)
        elif(words[0].isnumeric()):
            cwd.files[words[1]]=int(words[0])

TOTAL=70000000
NEED=30000000

print("Have: %d" % tree.size())

mustdel = NEED-(TOTAL-tree.size())

print("Must delete: %d" % mustdel)

printMoreThan(tree,mustdel)

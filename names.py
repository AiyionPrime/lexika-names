#!/usr/bin/env python3
print("names 0.2")

inp = "names.txt"
data = open(inp)
dat = data.read()
lst = dat.splitlines()

lst.sort()
#print(lst)


def shortest_len(name1, name2):
    return len(name1) if len(name1) < len(name2) else len(name2)

def diffindex(name1, name2):
    for index in range(shortest_len(name1, name2)):
        if name1[index] != name2[index]:
            return index

def getSplitStr(name1, name2):
    d = diffindex(name1,name2)
    return (name1[:d+1],name2[:d+1])

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

class Namegroup(object):
    def __init__(self, names, start, end):
        self.names = names
        self.start = start
        self.end = end

    @property
    def range(self):
        return self.start if self.start == self.end else self.start + " - " + self.end

    def __str__(self):
        return "[" + str(len(self.names))+ "] (" + self.range +  ")\n\t\t" + str(self.names)


def generateNamegroups(names, size):
    runner = "A"
    namegroups = []

    chunked = list(chunks(names, size))

    for i in range(len(chunked)):
        fn = chunked[i][-1:][0]  # get last name of current chunk
        try:
             sn = chunked[i+1][0]  # will fail at last
        except IndexError:
             sn = "\0"
        border = getSplitStr(fn, sn)
        namegroups.append(Namegroup(chunked[i], runner, border[0]))
        runner = border[1]

    return namegroups

grps = generateNamegroups(lst, 6)
for grp in grps:
     print(grp)


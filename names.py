#!/usr/bin/env python3

def shortest_len(name1, name2):
    return len(name1) if len(name1) < len(name2) else len(name2)

def diffindex(name1, name2):
    for index in range(shortest_len(name1, name2)):
        if name1[index] != name2[index]:
            return index

def getSplitStr(name1, name2):
    d = diffindex(name1,name2)
    return (name1[:d+1],name2[:d+1])

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class Namegroup(object):
    def __init__(self, tplidname, start, end):
        self.tplidname = tplidname
        self.start = start
        self.end = end

    @property
    def range(self):
        return self.start if self.start == self.end else self.start + " - " + self.end

    def __str__(self):
        return "[" + str(len(self.tplidname))+ "] (" + self.range +  ")\n\t\t" + str(self.tplidname)


def generateNamegroups(name_dict, size):
    tpllst = sorted(name_dict.items(), key=lambda t: t[1])
    runner = "A"
    namegroups = []

    chunked = list(chunks(tpllst, size))

    for i in range(len(chunked)):
        fn = chunked[i][-1:][0][1]  # get last name of current chunk
        try:
             sn = chunked[i+1][0][1]  # will fail at last
        except IndexError:
             sn = "\0"
        border = getSplitStr(fn, sn)
        namegroups.append(Namegroup(chunked[i], runner, border[0]))
        runner = border[1]
    return namegroups

if __name__=="__main__":
    print("names 0.2")

    inp = "names.txt"
    data = open(inp)
    dat = data.read()
    lst = dat.splitlines()

    dct = {}

    i=0;
    for entry in lst:
        dct[i]=entry
        i+=1 

    # dct now contains a dictionary like id --> name 

    grps = generateNamegroups(dct, 6)

    for grp in grps:
        print(grp)

#!/usr/bin/env python3
print("names 0.1")

inp = "names.txt"
data = open(inp)
dat = data.read()
lst = dat.splitlines()

lst.sort()
print(lst)

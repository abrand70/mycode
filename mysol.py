#!/usr/bin/env python3
myfile=open("sol.txt", "r")
x=myfile.read().replace('\n',' ')
print(x)
myfile.close()


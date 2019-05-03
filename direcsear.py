#!/usr/bin/env python3
#from blessings import Terminal
#t = Terminal()
#print(t.clear())
#print('Name', '\t\tDescription')




#envirdir = {'a': 'right', 'b': 'left', 'c': 'up', 'd': 'down'}
#envirdir {'a': 'right', 'b': 'left', 'c': 'up', 'd': 'down'}
#envirdir[a]
#dict_keys(['a', 'b', 'c', 'd'])
#envirdir[a]

#def lokup(n,d)

import os
import pyexcel
import fnmatch

def listypy(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=Tru):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

def write_excel(prog_list):
    data = []
    for name in prog_list:
        inp = input(f"what description do you wish to add to {name}")
        prog = {"Filename": name, "desription": inp}
        data.append(prog)
     print(data)
     filename = "Program-list.xls"
     pyexcel.save_as(records=data, dest_file_name=filename)

write_excel(listypy("*.py", "C:/Alta3/vzw4-29-19/day5/"))     

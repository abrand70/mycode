#!/usr/bin/env python3

## python3 -m pip install --user pyexcel
## python3 -m pip install --user pyexcel-xls

import pyexcel

def myfunc(varfilename):
    ## What is the name of the xls file?
    #varfilename = input('What is the name of the file? Do not include extension ')

    myexcelval = { }

    varfilename = varfilename + ".xls"

## Dump excel spreadsheet to the record format friendly to python
    excelrecords  = pyexcel.iget_records(file_name=varfilename)

    for x in excelrecords:
        totalsocket = x['ip'] + ":" + str(x['port'])
        myexcelval.update ( { x['service'] : totalsocket } ) ## adds a new
                     ## IP an driver key:value pair to our dictionary

#prints the key and value
#print(myexcelval)

    #User querys a service
    userinput = input('\nWhat is the services you would like? ')

    #The IP of the service the user requested
    print('The IP addres for that services is ' + myexcelval[userinput])


myfunc('portservice')        

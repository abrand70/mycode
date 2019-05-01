#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
#added the \n to answer question 1
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

#iplist = ["10.1.1.0", "192.6.2.3", "156.23.255.0"]

#def devicereboot(router):
#    for listip in router:
#        print("Connecting to..." + listip)
#    print("rebooting now")


#devicereboot(iplist)

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run 
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()

iplist = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

def devicereboot(router):
    for listip in router:
        print("Connecting to..." + listip)
    print("\nrebooting now")
print("\n")

devicereboot(iplist)
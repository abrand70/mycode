#!/usr/bin/env python3

iplist = ["10.1.1.0", "192.6.2.3", "156.23.255.0"]

def devicereboot(router):
    for listip in router:
        print("Connecting to..." + listip)
    print("rebooting now")


devicereboot(iplist)
#1/usr/bin/env python3
print('What is your favorite channel?')
x = int(input('What channel do you like?'))
if 1 <= x and 10 >= x:
    print('This customer is a Basic Customer')
elif 11 <= x and 40 >= x:
    print('This customer is a Standard Customer')
elif 41 <= x and 100 >= x:
    print('This customer is a Premium Customer')
elif 101 <= x and 200 >= x:
    print('This customer is a HD Customer')
elif 201 <= x and 600 >= x:
    print('This customer want the Expensive Stuff')

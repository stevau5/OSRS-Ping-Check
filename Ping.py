import os
import time

begintime = time.time()

print (" ... Commencing World Ping Sequence ...")

try:
    os.remove("output.txt")
except: 
    print("no ouput file")

f = open("output.txt", "x")

for x in range(1, 237):
    if: 
        os.system("ping -c 1 oldschool" + str(x) + ".runescape.com >> output.txt") == 0
        #I need to add an array that stores the worlds that ahve a valid ping, if they dont have a valid ping they need 
        #there needs to be a null value. 
        print("World", x)
  



f = open("output.txt", "r")

count = 301

for line in f:
    if line.find("time") != -1:
        splitLine = line.split()
        pingIndex = splitLine[6]
        ping = pingIndex[5:]

        print("World " + str(count) + " current ping ---> ", ping)
        count += 1
        

endtime = time.time()

print("Ellapsed time: ", endtime-begintime)





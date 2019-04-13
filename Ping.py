import os
import time

begintime = time.time()

print (" ... Commencing World Ping Sequence ...")

try:
    os.remove("output.txt")
except: 
    print("no ouput file")

f = open("output.txt", "x")

for x in range(1, 32):
    os.system("ping -c 1 oldschool"+ str(x) +".runescape.com >> output.txt")

count = 301

f = open("output.txt", "r")

for line in f:
    if line.find("time") != -1:
        splitLine = line.split()
        pingIndex = splitLine[6]
        ping = pingIndex[5:]

        print("World " + str(count) + " current ping ---> ", ping)
        count += 1
        

endtime = time.time()

print("Ellapsed time: ", endtime-begintime)





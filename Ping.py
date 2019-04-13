import os
import time

begintime = time.time()

print (" ... Commencing World Ping Sequence ...")

try:
    os.remove("output.txt")
except: 
    print("no ouput file")


for x in range(23):
    print("Current Pinged World: " + str(x + 300))
    os.system("ping -c 1  -t 1 oldschool"+ str(x) +".runescape.com >> output.txt")

f = open("output.txt")

for line in f:
    if line.find("time") != -1:
        print("true   ", line)
        


endtime = time.time()

print("Ellapsed time: ", endtime-begintime)





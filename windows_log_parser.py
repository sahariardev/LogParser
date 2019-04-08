root = "/home/bjit-555/apps/logs/loghub/"
filename_adnroid = root + "Windows/Windows_2k.log"
import json
import re
lines = open(filename_adnroid, "r")
level_list=['InfoCBSFailed','InfoCBSWarning','InfoCBSExpecting','InfoCBSStartup','InfoCBSSession']

final_output = []
for line in lines:
    line=re.sub(r"  +|,","",line)
    line=line.replace("[","").replace("]","")
    data = line.split(" ")
    if data[2] in level_list:
        message = ""
        for d in range(2, len(data), 1):
            message = message + " " + data[d]

        out={
            'timestamp':data[0]+" "+data[1],
            'level':data[2].replace("InfoCBS",""),
            'message':message
        }
        final_output.append(out)

with open('windows.json', 'w') as outfile:
    json.dump(final_output, outfile)
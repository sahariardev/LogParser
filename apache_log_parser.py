root = "/home/bjit-555/apps/logs/loghub/"
filename_adnroid = root + "Apache/Apache_2k.log"
import json

lines = open(filename_adnroid, "r")
log_levels = ['notice', 'error']

final_output = []
for line in lines:
    line=line.replace("[","").replace("]","")
    data = line.strip().split(" ")
    if data[5] in log_levels:
        message = ""
        for d in range(6, len(data), 1):
            message = message + " " + data[d]
        out={
            'timestamp':data[0]+" "+data[1]+" "+data[2]+" "+data[3]+" "+data[4],
            'level':data[5],
            'message':message

        }
        final_output.append(out)
with open('apache.json', 'w') as outfile:
    json.dump(final_output, outfile)

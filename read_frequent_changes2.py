import sys
import json

with open('frequentchanges.txt') as fp:
    s = fp.read()
j = json.loads(s)
sys.stdout.write(str(j['changes']))



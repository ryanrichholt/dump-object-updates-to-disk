import json
import sys
while 1:
    try:
        with open('frequentchanges.txt') as fp:
            s = fp.read()
        j = json.loads(s)
        sys.stdout.write(str(j['changes']) + '\r')
    except json.decoder.JSONDecodeError:
        print("Unable to parse this: %s" % s)


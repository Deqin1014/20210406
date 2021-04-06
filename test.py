import hashlib
import sys

passwordList = []
with open('passwordList.txt','r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        passwordList.append(currentPlace)

print(passwordList)
if len(sys.argv) == 2:
    msg = sys.argv[1].encode()
    hashvalue = hashlib.sha256(msg)
    print(hashvalue)
    print(hashvalue.herdiget().upper())
    
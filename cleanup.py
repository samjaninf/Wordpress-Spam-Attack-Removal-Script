import os
import sys
import json

db = open('database.json', 'r')
malware_records = json.loads(db.read())
replacement = """"""

logs = open("cleanup.log","w")
for dname, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath, encoding='utf-8', errors='ignore') as f:
            print(fpath)
            if fname.lower().endswith((".png", ".jpg", ".jpeg", ".ico", ".svg")):
                continue
            else:
                s = f.read()
        length_of_original = len(s)
        for record in malware_records:
            s = s.replace(record['string'], replacement)
        if len(s) != length_of_original :
            logs.write("Cleaning " + fname + " in " + dname + "\n")
        with open(fpath, "w") as f:
            f.write(s)

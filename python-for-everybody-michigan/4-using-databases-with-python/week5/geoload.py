import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import time
import ssl


serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"


scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", ((address), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    print('Resolving', address)
    url = serviceurl + urllib.parse.urlencode({"sensor":"false", "address": address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=scontext)
    data = uh.read().decode('UTF-8')
    print('Retrieved',len(data),'characters',data[:20].replace('\n',' '))
    count = count + 1
    try: 
        js = json.loads(str(data))
      
    except: 
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( (address),(data) ) )
    conn.commit() 
    time.sleep(1)


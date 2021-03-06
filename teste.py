import speedtest
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

test = speedtest.Speedtest()

#test of download

down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

#test of upload

upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('dados.sqlite')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
cursor.execute('''INSERT INTO testes VALUES (?, ?, ?)''',(now,fDown,fUp))

# Commit your changes in the database	
conn.commit()

# Closing the connection
conn.close()



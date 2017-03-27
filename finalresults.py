import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

cur.execute("SELECT * FROM tweetwordcount ORDER BY word")

if len(sys.argv)!=1:
	word = sys.argv[1]
	for record in cur:
		if word in record:
			print('Total number of occurences of "' + word + '": ' + str(record[1]))
else:
	for record in cur:
		print("(" + record[0] + ", " + str(record[1]) + ")")


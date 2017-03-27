import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

greaterthan = sys.argv[1]
lessthan = sys.argv[2]

cur.execute("SELECT * FROM tweetwordcount WHERE count >= " + greaterthan + " AND count <= " + lessthan + " ORDER BY count")

for record in cur:
	print(record[0] + ": " + str(record[1]))


print("\n\n\n\n")
print("Top 20 Words")

cur.execute("SELECT * FROM tweetwordcount ORDER BY count DESC LIMIT 20")


for record in cur:
	print(record[0] + ": " + str(record[1]))

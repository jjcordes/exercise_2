from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.
        # Connect to the database

        conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

        #Create the Database

        try:
                # CREATE DATABASE can't run inside a transaction
                conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cur = conn.cursor()
                cur.execute("CREATE DATABASE tcount")
                cur.close()
                conn.close()
        except:
                print("Could not create tcount")

        #Connecting to tcount

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        #Create a Table
        #The first step is to create a cursor.

	try:
        	cur = conn.cursor()
        	cur.execute('''CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY     NOT NULL, count INT     NOT NULL);''')
        	conn.commit()
	except:
		print("Could not create tweetwordcount")


        # Increment the local count
        self.counts[word] += 1

	try:
	        #Insert
        	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        	cur = conn.cursor()
		cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, self.counts[word]))
        	conn.commit()

        except:
		#Update
		conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
		cur = conn.cursor()
        	cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        	conn.commit()


        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))


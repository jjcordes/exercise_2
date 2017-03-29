Exercise 2 - Twitter

Steps to run the application
----------------------------

1. Set up the EC2 AMI with attached EBS volume as described in Exercise 2 instructions

	a. Create and connect to AMI following Lab 6 instructions
	
	b. "fdisk -l" to find connected EBS store
	
	c. use command like "mount -t ext4 /dev/xvdh /data" to mount it at /data ("df -k" to check)
	
	d. "pip install psycopg2==2.6.2"
	
	e. "pip install tweepy"
	
	
2. As root user, start Postgres with "/data/start_postgres.sh" 

3. Switch to w205 user "su - w205

4. Make a new directory, navigate to it, and clone this git "git clone https://..."

5. Navigate to exercise_2 directory

Try:

	6. Type "sparse run": a program will start collecting the words and counts being tweeted from Twitter
	
	7. Use Control-Z to stop it when you've collected enough data

Except:

	If there's a bunch of empty queue exceptions, send thoughts and prayers to Twitter, and return to step 5	

8. Type "python finalresults.py (word of interest)" to see how many of a particular word was tweeted in that time

9. Type "python finalresults.py" to get the entire list of words and counts

10. Type "python histogram.py 3 8" to get a list of words with counts between 3 and 8 (and see top 20 words at the end)


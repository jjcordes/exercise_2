Exercise 2 - Twitter

Steps to run the application
----------------------------

1. Set up the EC2 AMI with attached EBS volume as described in Exercise 2 instructions
	a. AMI from Lab 6
	b. "pip install psycopg2==2.6.2"
	c. "pip install tweepy"
	
2. As root user, start Postgres with "start_postgres.sh" 

3. Clone this git "git clone https://..."

4. Navigate to tweetwordcount directory

Try:

	5. Type "sparse run": a program will start collecting the words and counts being tweeted from Twitter
	
	6. Use Control-Z to stop it when you've collected enough data

Except:

	If there's a bunch of empty queue exceptions, send thoughts and prayers to Twitter, and return to step 5	

7. Type "python finalresults.py (word of interest)" to see how many of a particular word was tweeted in that time

8. Type "python finalresults.py" to get the entire list of words and counts

9. Type "python histogram.py 3,8" to get a list of words with counts between 3 and 8 (and see top 20 words at the end)


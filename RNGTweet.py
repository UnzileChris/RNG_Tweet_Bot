#I made a stupid thing in 15 minutes so I could use my raspberry pi for something
import sys
from twython import Twython
import time
import random
CONSUMER_KEY = 'shhhhh, it is a secret'
CONSUMER_SECRET = 'shhhhh, it is a secret'
ACCESS_KEY = 'shhhhh, it is a secret'
ACCESS_SECRET = 'shhhhh, it is a secret'
t = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
while True:
	t.update_status(status=random.randint(0,1000000))
	time.sleep(1200)
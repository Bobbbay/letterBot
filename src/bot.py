import praw
import os

sub = "BobbbayBots"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass') 

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='The Letter Man',
                     username='letterManBot')

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)
if(current_time is "00:00:00"):
    f = open("amount.txt", "w")
    f.write('0')
    f.close()

moderators = list(reddit.subreddit(sub).moderator())
for submission in reddit.subreddit(sub).new(limit=None):
    if("[WAR]" in submission.title and not submission.saved):
        f = open("amount.txt", "r")
        num = int(f.read())
        f.close()

        f = open("amount.txt", "w")
        f.write(str(num + 1))
        f.close()

        reply = 'This was marked as a WAR. There have been {0} posts marked like this today. \n\n^Beep ^boop^.'.format(num + 1)
        submission.reply(reply).mod.distinguish(sticky=True)

        submission.save()
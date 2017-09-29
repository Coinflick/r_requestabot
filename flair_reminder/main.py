import praw
import datetime
import time
pm_subject = "Please flair your post"
pm_body = """
Hello there, {}. Thank you for [your submission](https://reddit.com{}) to r/battlefield_live,  and we'd like to remind you to [flair it](http://i.imgur.com/bsrYmEz.png)!

If you are on a phone you can use a comment command to flair your post, make a single comment with the following command inside your post

"!flair [See all the available flair commands](https://www.reddit.com/r/battlefield_live/wiki/guides/flair#wiki_commands)"

Thank you! /DICE and The Battlefield Live moderation team
"""
# Amount of time to send message after if there is no flair, in minutes
x = 10


reddit = praw.Reddit(user_agent='https://github.com/hkyq/r_requestabot/new/master',
                     client_id='', client_secret="",
                     username='', password='')

def get_date(submission):
    time = submission.created_utc
    time_created = datetime.datetime.utcfromtimestamp(time)
    time_current = datetime.datetime.utcnow()
    inbetween = time_current - time_created
    inbetween_total = int(inbetween.total_seconds()) / 60
    # If submission is older than 10 minutes, return True, if it isn't, return false
    if inbetween_total > x and submission._flair == None:
        return True
    else:
        return False

subreddit = reddit.subreddit('hkyq')
while True:
    for submission in subreddit.stream.submissions():
        if get_date(submission) == True:
            submission.author.message(pm_subject, pm_body.format(submission.author, submission.permalink))
            print("Post found: https://reddit.com{}".format(submission.permalink))


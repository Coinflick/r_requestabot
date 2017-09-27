from pyOutlook import *
import praw
token = ""
my_account = OutlookAccount(token)


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')
subreddit = reddit.subreddit("hkyq")

error_1_no_auth = """
ERROR: Email received but no [Authentication] found in subject
"""

error_2_no_username = """
ERROR: No username (u/) found in subject
"""

error_msg_2 = """
Hello, it seems you have attempted to authenticate your Reddit account with our private subreddit.
There was [Authentication] in your subject, but I could not find your username. Please apply with this subject:
[Authentication] u/your_reddit_username
"""

error_msg_1 = """
Hello, it seems you have attempted to authenticate your Reddit account with our private subreddit.
However, there was no [Authentication] in your subject, so I'm not sure if you were trying to authentiate or not.
If you were, please apply with this subject:
[Authentication] u/your_reddit_username

If you weren't, please don't email me. 
"""

def authenticateUser(username):
    subreddit.add_contributor(username)
    print("User authenticated: u/{}".format(username))


def emailCheck():
    while True:
        for email in my_account.get_messages():
            email_to_reply = my_account.get_message(email.message_id)
            if "[Authentication]" in email.subject:
                username = email.subject.split()[1]
                if "u/" not in username:
                    email_to_reply.reply(error_msg_2)
                    email.move_to("")
                    return error_2_no_username
                email.move_to("")
                authenticateUser(username)
            else:
                email_to_reply.reply(error_msg_1)
                email.move_to("")
                return error_1_no_auth


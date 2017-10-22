from imgurpython import ImgurClient
import praw
import random

# ----------- Authentication -------------
client_id = ""
client_secret = ""

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')
# ----------- Authentication -------------

client = ImgurClient(client_id, client_secret)
album = client.get_album_images('4Yh6F')


with open("submitted.txt", "r") as output:
    used_urls = output.readlines()

with open("number.txt", "r") as output:
    num = str(output.readline())
    print(num)
    #num = num.replace(" ", "")



def save_post(url):
    with open("submitted.txt", "w") as output:
        output.write(str(url + "\n"))

def save_number():
    with open("number.txt", "w") as output:
        print(num)
        num_to_write = int(num) + 1
        print(num_to_write)
        output.write(str(num_to_write))


def submit_post():
    img = random.choice(album)
    if img in used_urls:
        submit_post()
        print("Post already submitted, retrying. If this happens alot, I might of used the whole album.")
    else:
        reddit.subreddit('hkyq').submit('weird shit {}'.format(num), url=img.link)
        save_post(img.link)
        save_number()
        print("Post submitted.")


submit_post()

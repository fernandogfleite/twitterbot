import tweepy
from random import choice
from decouple import config
from time import sleep

consumer_key = config('API_KEY')
consumer_secret = config('API_SECRET_KEY')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')
bearer_token= config('BEARER_TOKEN')


USER_ID = config('USER_ID')

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token
)


FILE = "mentions.txt"

def retrieve_id(file):
    f_read = open(file, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()

    return last_seen_id

def store_id(id, file):
    f_write = open(file, "w")
    f_write.write(str(id))
    f_write.close()

    return

if __name__ == "__main__":
    while True:
        try:
            since_id  = retrieve_id(FILE)
            mentions = client.get_users_mentions(id=USER_ID, since_id=since_id).data

            if mentions:
                for mention in mentions:
                    options = ("É corno", "Não é corno")
                    text = choice(options)
                    response = client.create_tweet(text=text, in_reply_to_tweet_id=mention.id)  
                    since_id = mention.id
                    store_id(since_id, FILE)
        except Exception as error:
            print(error)

        sleep(60)

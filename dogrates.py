
from twython import Twython
import yaml
import time
import re

with open('credentials.yaml', 'r') as f:
    credentials = yaml.load(f)

twitter = Twython(
  credentials["twitter"]["consumer_key"],
  credentials["twitter"]['consumer_secret'],
  credentials["twitter"]['token'],
  credentials["twitter"]['token_secret'],
  )


regex = re.compile('[0-9]*.[0-9]*/10')


print "time\trating\ttext\tmedia"
user_timeline = twitter.get_user_timeline(screen_name="dog_rates",count=1)[0]
lis = [user_timeline['id']]
for i in range(0, 16):
    user_timeline = twitter.get_user_timeline(screen_name="dog_rates",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(2)

    for tweet in user_timeline:
        if tweet[u'retweeted'] == False and tweet['text'][:3] != "RT ":
            if regex.search(tweet['text']) != None:
                out = []
                out.append(tweet['created_at'])
                out.append(regex.search(tweet['text']).group().split("/")[0])
                out.append(tweet['text'].replace("\n",""))
                if tweet['entities'].has_key('media'):
                    out.append(tweet['entities']['media'][0]['media_url'])
                else:
                    out.append("")
                print "\t".join(out)

        lis.append(tweet['id'])

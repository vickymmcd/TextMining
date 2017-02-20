import twitter
import api_keys
import pickle
from pathlib import Path

def get_trump_tweets():
    my_file = Path('trumptwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('trumptwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@realDonaldTrump', 'trumptwitters.pickle',
                        '796130213826621440')


def get_clinton_tweets():
    my_file = Path('clintontwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('clintontwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@HillaryClinton', 'clintontwitters.pickle',
                        '796123724479164416')


def retrieve_tweets(name, filename, idnum):

    api = twitter.Api(api_keys.consumer_key, api_keys.consumer_secret,
                      api_keys.access_token_key,
                      api_keys.access_token_secret)

    tweets = api.GetUserTimeline(screen_name=name, count=199, max_id=idnum)
    for status in tweets:
        print(status.id)
        print(status.created_at)
    tweets = [s.text for s in tweets]
    # Save data to a file
    f = open(filename, 'wb')
    pickle.dump(tweets, f)
    f.close()

# -*- coding: utf-8 -*-
# import tweepy
import os
from os.path import expanduser
import configparser
import imp
import  twitter
from twitter import Twitter
from twitter import OAuth


# class MyStreamListener(tweepy.StreamListener,analyzer.analyzer):
    
#     def on_status(self, status):
#         self.analyze_sentiment(status.text)
        

class twitter:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(expanduser("~"),".twitter/credentials"))
        self.consumer_key = config.get("default","consumer_key")
        self.consumer_secret = config.get("default","consumer_secret")
        self.access_token = config.get("default","access_token")
        self.access_token_secret = config.get("default","access_token_secret")
        # self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        # self.auth.set_access_token(self.access_token, self.access_token_secret)
        oauth=  OAuth(self.access_token,self.access_token_secret,self.consumer_key,self.consumer_secret)
        self.api= Twitter(auth=oauth)

    def tweet_stream(self,topics):
        
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = self.auth, listener=myStreamListener)
        myStream.filter(track=topics)

    def tweet_batch(self,topics,count):
        return self.api.search.tweets(q=topics, count=count)
# -*- coding: utf-8 -*-
"""
hw4:lqi25
"""
import cv2
import tweepy
import re
from PIL import Image, ImageDraw, ImageFont
import os
#import cv2
import numpy as np
import glob
import configparser


def tweet2image(tweet_name):
    if tweet_name == "":
        return "No tweet name entered!"
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'keys')
    #config = RawConfigParser()
    config = configparser.ConfigParser()
    res = config.read(initfile)
    #config = configparser.ConfigParser()
    #config.read(r'./keys')
    try:
        consumer_key = config.get('auth', 'consumer_key').strip()
        consumer_secret = config.get('auth', 'consumer_secret').strip()
        access_token = config.get('auth', 'access_token').strip()
        access_token_secret = config.get('auth', 'access_token_secret').strip()

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        search_results = api.user_timeline(tweet_name)
        num = 0
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        for tweet in search_results:
            tweet_list = list(tweet.text)
            for i in range(len(tweet_list)):
                if (i % 60) == 0:
                    tweet_list.insert(i,'\n')
            tweet.text = ''.join(tweet_list)
            num += 1
            text_noem = highpoints.sub('--emoji--', tweet.text)
            text_noem = text_noem.encode('utf8')
            image = Image.open('C:/Users/18367/Desktop/hw5/Boston.jpg')
            draw = ImageDraw.Draw(image)
            fnt = ImageFont.truetype('C:/Users/18367/Desktop/hw5/Lato-BlackItalic.ttf', 50)
            (x, y) = (100, 100)
            color = 'rgb(0, 0, 0)'
            draw.text((x, y), tweet.text, font=fnt, fill= color)
            filename = "C:/Users/18367/Desktop/hw4/" + str(num) + ".png"
            image.save(filename)
        print("Images created")
        return "Images created!"
    except AttributeError:
        print("No keys in the file")
        return "No keys in the keys file"


def image2video(video_name):
    if video_name == "" :
        return "No video name entered!"
    img_array = []
    for filename in glob.glob('C:/Users/18367/Desktop/hw4/*.png'):
        img = cv2.imread(filename)
        try:
            height, width, layers = img.shape
            size = (width, height)
            #print(size)
            img_array.append(img)
        except AttributeError:
            pass
        #img_array.append(img)
    video_name += ".avi"
    #print(video_name)
    #video_name = "C:/Users/18367/Desktop/hw5/"+video_name
    #print(video_name)
    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('I', '4', '2', '0'), 1 / 3, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("video created")
    return "Video created!"

#tweet2image("mfaboston")
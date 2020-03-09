from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import Twitter2Video
import queue_mul
import zipfile
app = Flask(__name__)

@app.route('/') #creates the flask html route
def root():
    return render_template('tweet.html')

@app.route('/', methods=['POST'])
def upload():
    x1 = request.form['x1']  # getting usernames
    x2 = request.form['x2']
    x3 = request.form['x3']
    tweet_name=[]
    if x1 !="":
        tweet_name.append(x1)
    if x2 !="":
        tweet_name.append(x2)
    if x3 !="":
        tweet_name.append(x3)
    print(tweet_name)
    queue_mul.Mul_Threads(tweet_name,3)
    print("this is finished")
    zipFolder = zipfile.ZipFile('videos.zip', 'w', zipfile.ZIP_DEFLATED)
    for item in tweet_name:
        name = item +'.avi'
        zipFolder.write(name)

    zipFolder.close()
    return send_file('videos.zip', mimetype='zip',attachment_filename='videos.zip',as_attachment=True)

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 80, debug=True)






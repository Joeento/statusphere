from app import app
from flask import Flask, redirect, request, render_template
import tweepy
import secret
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	auth = tweepy.OAuthHandler(secret.consumer_token, secret.consumer_secret)
	try:
		redirect_url = auth.get_authorization_url()
	except tweepy.TweepError:
		print 'Error! Failed to get request token.'
	return render_template('index.html',title="Home", redirect_url=redirect_url)

@app.route('/result')
@app.route('/result.html')
def result():
	verification_code = request.args.get('code')
	auth = tweepy.OAuthHandler(secret.consumer_token, secret.consumer_secret)
	token = session.get('request_token')
	print token
	try:
	    auth.get_access_token(verification_code)
	    print "success"
	except tweepy.TweepError:
	    print 'Error! Failed to get access token.'
	return render_template('result.html',verification_code=verification_code)
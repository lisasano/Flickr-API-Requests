# my user id = 61965480@N03

import requests
import os

flickr_api_key = os.environ.get('FLICKR_API_KEY')
flickr_secret = os.environ.get('FLICKR_SECRET')

# makes functions for common parts amongst all the requests
def get_request(my_params):
	my_params['api_key'] = flickr_api_key
	my_params['format'] = 'json'
	my_params['nojsoncallback'] = 1
	r = requests.get("https://api.flickr.com/services/rest/", params=my_params)
	return r.json()


# find a member using their email address. Print out the json response and user id number
def find_member_id():
	email_address = raw_input("What is the email address you want to look up? ")
	findMemberWithEmail = {'method': 'flickr.people.findByEmail', 'find_email': email_address}
	request1 = get_request(findMemberWithEmail)
	print request1
	userIDNumber = request1['user']['nsid']   #nested dict call
	return userIDNumber


# gets list of favorites
def get_favorites_list(userIDNumber):
	favoritesList = {'method': 'flickr.favorites.getList', 'user_id': userIDNumber, 'per_page': 5, 'page': 1}
	request2 = get_request(favoritesList)
	print request2
	
	
# gets the HTML (in json) for my public photos using Flickr's API
def get_public_photos(userIDNumber):
	publicPhotos = {'method': 'flickr.people.getPublicPhotos', 'user_id': userIDNumber}
	request3 = get_request(publicPhotos)
	print request3


# get user profile for the person whose email was searched for
def find_user_profile(userIDNumber):
	findUserProfile = {'method': 'flickr.urls.getUserProfile', 'user_id': userIDNumber}
	request4 = get_request(findUserProfile)
	print request4

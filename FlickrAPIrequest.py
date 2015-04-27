# my user id = 61965480@N03

import requests
import os

flickr_api_key = os.environ.get('FLICKR_API_KEY')
flickr_secret = os.environ.get('FLICKR_SECRET')


def get_request(my_params):
	'''makes functions for common parts amongst all the requests'''
	my_params['api_key'] = flickr_api_key
	my_params['format'] = 'json'
	my_params['nojsoncallback'] = 1
	r = requests.get("https://api.flickr.com/services/rest/", params=my_params)
	return r.json()

def find_member_id_and_username(email_address):
	'''find a member using their email address. Print out the json response and user id number'''
	findMemberWithEmail = {'method': 'flickr.people.findByEmail', 'find_email': email_address}
	request1 = get_request(findMemberWithEmail)	
	userIDNumber = request1['user']['nsid']   #nested dict call
	username = request1['user']['username']['_content']
	user_info_dict = {'user_id': userIDNumber, 'username': username}
	return user_info_dict

def get_favorites_list(userIDNumber):
	'''gets list of favorites'''
	favoritesList = {'method': 'flickr.favorites.getList', 'user_id': userIDNumber, 'per_page': 5, 'page': 1}
	request2 = get_request(favoritesList)
	favorite_photos = request2['photos']['photo']
	return favorite_photos
	
def get_public_photos(userIDNumber):
	'''gets the HTML (in json) for public photos using Flickr's API'''
	publicPhotos = {'method': 'flickr.people.getPublicPhotos', 'user_id': userIDNumber, 'extras': ['url_t']}
	request3 = get_request(publicPhotos)
	photo_list = request3['photos']['photo']
	# photo_list_dict = {'photo_id': photo_list['id'], 'photo_title': photo_list['title']}
	return photo_list

def find_user_profile(userIDNumber):
	'''get user profile for the person whose email was searched for'''
	findUserProfile = {'method': 'flickr.urls.getUserProfile', 'user_id': userIDNumber}
	request4 = get_request(findUserProfile)
	my_url = request4['user']['url']
	return my_url

	# output: {u'stat': u'ok', u'user': {u'url': u'https://www.flickr.com/people/61965480@N03/', u'nsid': u'61965480@N03'}}

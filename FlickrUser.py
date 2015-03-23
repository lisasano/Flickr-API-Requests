from FlickrAPIrequest import *


class User(object):
	
	def __init__(self, email_address):
		self.email = email_address
		
		self.user_id = find_member_id(self.email)
	
		self.pub_photos = get_public_photos(self.user_id)
	
		self.fave_list = get_favorites_list(self.user_id)


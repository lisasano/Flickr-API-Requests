from FlickrAPIrequest import *
from FlickrUser import *


email_address = raw_input("What is the email address you want to look up? ")

user1 = User(email_address)
user1.fetch_user_info()
user1.fetch_public_photos()
for i in user1.pub_photos:
    i.make_url()
    print i.url


'''
print user1.email
print user1.user_id
print user1.pub_photos
print user1.fave_list
'''

from FlickrAPIrequest import *

email_address = raw_input("What is the email address you want to look up? ")
user_id = find_member_id(email_address)

user_prof = find_user_profile(user_id)
print user_prof

user_pub_photos = get_public_photos(user_id)
print user_pub_photos

user_fave_list = get_favorites_list(user_id)	
print user_fave_list
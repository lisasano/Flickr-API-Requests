from FlickrAPIrequest import *

user_id = find_member_id()
find_user_profile(user_id)
get_public_photos(user_id)
get_favorites_list(user_id)	
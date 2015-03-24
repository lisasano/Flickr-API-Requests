from FlickrAPIrequest import *
from FlickrPhoto import Photo


class User(object):
	
	def __init__(self, email_address):
		self.email = email_address
		
		self.user_id = find_member_id(self.email)
		self.pub_photos = []
		self.fave_list = []
		self._set_public_photos()
		self._set_fave_list()
		
	def _make_photo_instance_from_raw_data(self, raw_photo_data):
		'''creates and returns an instance of class photo'''
		photo_title = raw_photo_data['title']
		photo_id = raw_photo_data['id']
		photo_instance = Photo(photo_title, photo_id)
		return photo_instance
		
		
	def _set_public_photos(self):
		'''creates and prints a list of public photos'''
		raw_photo_data = get_public_photos(self.user_id)
		for photo in raw_photo_data:
			new_one = self._make_photo_instance_from_raw_data(photo)
			self.pub_photos.append(new_one)
		print self.pub_photos
		
		
		
	def _set_fave_list(self):
		'''creates and print a list of favorite photos'''
		raw_fave_list = get_favorites_list(self.user_id)
		for photo in raw_fave_list:
			new_fave = self._make_photo_instance_from_raw_data(photo)
			self.fave_list.append(new_fave)
		print self.fave_list




'''

photos = [
	{blahblah},
	{blahblah}
]
{
    u'photos': {
        u'total': u'2',
        u'photo': [
            {
                u'isfamily': 0,
                u'title': u'SunsetfromTitlowBeach',
                u'farm': 8,
                u'ispublic': 1,
                u'server': u'7287',
                u'isfriend': 0,
                u'secret': u'83ce59a669',
                u'owner': u'61965480@N03',
                u'id': u'16555365651'
            },
            {
                u'isfamily': 0,
                u'title': u'SunsetfromTitlowBeach',
                u'farm': 8,
                u'ispublic': 1,
                u'server': u'7457',
                u'isfriend': 0,
                u'secret': u'ed1eb629fc',
                u'owner': u'61965480@N03',
                u'id': u'16369591050'
            }
        ],
        u'perpage': 5,
        u'page': 1,
        u'pages': 1
    },
    u'stat': u'ok'
}u'photos': {
    u'total': u'2',
    u'photo': [
        {
            u'isfamily': 0,
            u'title': u'SunsetfromTitlowBeach',
            u'farm': 8,
            u'ispublic': 1,
            u'server': u'7287',
            u'isfriend': 0,
            u'secret': u'83ce59a669',
            u'owner': u'61965480@N03',
            u'id': u'16555365651'
        },
        {
            u'isfamily': 0,
            u'title': u'SunsetfromTitlowBeach',
            u'farm': 8,
            u'ispublic': 1,
            u'server': u'7457',
            u'isfriend': 0,
            u'secret': u'ed1eb629fc',
            u'owner': u'61965480@N03',
            u'id': u'16369591050'
        }
    ],
    u'perpage': 5,
    u'page': 1,
    u'pages': 1
},
u'stat': u'ok'
}
'''
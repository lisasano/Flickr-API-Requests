from FlickrPhoto import Photo
import unittest


class TestPhoto(unittest.TestCase):
	
	def test_title_and_id_attributes_on_instantiation(self):
		title = "title_one"
		id = "id_one"
		new_photo = Photo(title, id)
		self.assertEqual(title, new_photo.title)
		self.assertEqual(id, new_photo.id)

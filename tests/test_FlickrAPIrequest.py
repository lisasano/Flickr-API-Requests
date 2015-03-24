import unittest
import FlickrAPIrequest
from mock import patch, Mock


class TestFindMemberID(unittest.TestCase):

	def test_find_member_id_uses_email_address_to_look_up_user_id_via_flickr_api(self):
		mock_dictionary = {'user': {'nsid': 'blahblah'}}
		mock_get_request = Mock()
		mock_get_request.return_value = mock_dictionary
		
		with patch('FlickrAPIrequest.get_request', mock_get_request):
			new_member = FlickrAPIrequest.find_member_id('fake_email')
		
		self.assertEqual(new_member, 'blahblah')
	
		expected_dict = {'method': 'flickr.people.findByEmail', 'find_email': 'fake_email'}
		
		mock_get_request.assert_called_once_with(expected_dict)


	def test_get_favorites_list_using_user_id_via_flickr_api(self):
		mock_dictionary = {'photos': {'photo': 'hehehe'}}
		mock_get_request = Mock()
		mock_get_request.return_value = mock_dictionary

		with patch('FlickrAPIrequest.get_request', mock_get_request):
			new_fave_list = FlickrAPIrequest.get_favorites_list('fake_id')
			
		self.assertEqual(new_fave_list, 'hehehe')

		expected_dict = {'method': 'flickr.favorites.getList', 'user_id': 'fake_id', 'per_page': 5, 'page': 1}

		mock_get_request.assert_called_once_with(expected_dict)


	def test_get_public_photos_using_user_id_via_flickr_api(self):
		mock_dictionary = {'photos': {'photo': 'public_blahness'}}
		mock_get_request = Mock()
		mock_get_request.return_value = mock_dictionary

		with patch('FlickrAPIrequest.get_request', mock_get_request):
			new_pub_photos = FlickrAPIrequest.get_public_photos('fake_id')

		self.assertEqual(new_pub_photos, 'public_blahness')

		expected_dict = {'method': 'flickr.people.getPublicPhotos', 'user_id': 'fake_id', 'per_page': 5, 'page': 1}

		mock_get_request.assert_called_once_with(expected_dict)


	def test_find_user_profile_using_user_id_via_flickr_api(self):
		mock_get_request = Mock()

		with patch('FlickrAPIrequest.get_request', mock_get_request):
			new_profile = FlickrAPIrequest.find_user_profile('fake_id')

		expected_dict = {'method': 'flickr.urls.getUserProfile', 'user_id': 'fake_id'}

		mock_get_request.assert_called_once_with(expected_dict)	

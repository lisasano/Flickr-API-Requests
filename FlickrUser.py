from FlickrAPIrequest import *
from FlickrPhoto import Photo
from FlickrModel import Model
import psycopg2

class User(Model):
    
    def __init__(self, email_address):
        self.email = email_address
        
        self.user_id = find_member_id_and_username(self.email)['user_id']
        print "USER_ID IS: %s" % self.user_id
        self.username = find_member_id_and_username(self.email)['username']
        print "USERNAME IS: %s" % self.username
        self.url = find_user_profile(self.user_id)
        print "URL IS: %s" % self.url
        self.pub_photos = []
        self.fave_list = []
        self._set_public_photos()
        self._set_fave_list()
        self.save()
        
    def _make_photo_instance_from_raw_data(self, raw_photo_data):
        '''creates and returns an instance of class photo'''
        photo_title = raw_photo_data['title']
        photo_id = raw_photo_data['id']
        photo_instance = Photo(photo_title, photo_id, self.user_id)
        return photo_instance

    def _set_public_photos(self):
        '''creates and prints a list of public photos'''
        raw_photo_data = get_public_photos(self.user_id)
        for photo in raw_photo_data:
            new_one = self._make_photo_instance_from_raw_data(photo)
            self.pub_photos.append(new_one)
        print "PUBLIC PHOTOS are: %s" % self.pub_photos
        for photo in self.pub_photos:
            photo.save()


    def _set_fave_list(self):
        '''creates and print a list of favorite photos'''
        raw_fave_list = get_favorites_list(self.user_id)
        for photo in raw_fave_list:
            new_fave = self._make_photo_instance_from_raw_data(photo)
            self.fave_list.append(new_fave)
        print "FAVORITE PHOTOS are: %s" % self.fave_list

    def _get_query_string(self):
        return '''
            DO
            $do$
            BEGIN
            if exists (SELECT * from flickr_user_info 
            WHERE user_id = %s) THEN
                UPDATE flickr_user_info
                    SET username = %s
                    WHERE user_id = %s;
            ELSE
                INSERT INTO flickr_user_info
                    (user_id, username, url)
                VALUES
                    (%s, %s, %s);
            END IF;
            END
            $do$
        '''

    def _get_query_string_values(self):
        return (self.user_id, self.username, self.user_id, self.user_id, self.username, self.url)




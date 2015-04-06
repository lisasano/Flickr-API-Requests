import psycopg2
from FlickrModel import Model


class Photo(Model):
    
    def __init__(self, title, photo_id, user_id):
        self.title = title
        self.id = photo_id
        self.user_id = user_id
        
    def __str__(self):
        return self.title

    def _get_query_string(self):
        '''return the query string for a photo save'''
        return '''
            DO
            $do$
            BEGIN
            if exists (SELECT * from flickr_public_photos
            WHERE photo_id = %s) THEN
                UPDATE flickr_public_photos
                     SET title = %s
                    WHERE photo_id = %s;
            ELSE
                INSERT INTO flickr_public_photos
                    (user_id, photo_id, title)
                VALUES
                    (%s, %s, %s);
            END IF;
            END
            $do$
        '''

    def _get_query_string_values(self):
        '''return a tuple of values that will get inserted into the query string'''
        return (self.id, self.title, self.id, self.user_id, self.id, self.title)



import psycopg2

from FlickrModel import Model


class Photo(Model):
    
    def __init__(self, title, photo_id, user_id, farm, server, secret):
        self.title = title
        self.id = photo_id
        self.user_id = user_id
        self.farm = farm
        self.server = server
        self.secret = secret

    def make_url(self):
        '''format of url is https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg'''
        self.url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' % (self.farm, self.server, self.id, self.secret)
        return self.url

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

    @classmethod
    def load_from_user_id(cls, user_id):
        photo_list = []
        conn = psycopg2.connect("dbname=lisa user=lisa")
        cur = conn.cursor()
        cur.execute(
            '''
            SELECT * from flickr_public_photos where user_id = %s;
            ''',
            (user_id,)
        )
        records = cur.fetchall()
        for record in records:
            # do something with the data
            user_id = record[0]
            photo_id = record[1]
            title = record[2]
            photo = Photo(title, photo_id, user_id)
            photo_list.append(photo)
        conn.commit()
        cur.close()
        conn.close()
        return photo_list


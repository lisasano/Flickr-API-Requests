import psycopg2


class Photo(object):
    
    def __init__(self, title, photo_id, user_id):
        self.title = title
        self.id = photo_id
        self.user_id = user_id
        
    def __str__(self):
        return self.title

    def _save_public_photo_info(self):
        conn = psycopg2.connect("dbname=lisa user=lisa")
        cur = conn.cursor()

        cur.execute(
            '''
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
            ''',
            (self.id, self.title, self.id, self.user_id, self.id, self.title)

            )

        cur.execute("SELECT * from flickr_public_photos;")
        fetch_pub_photo_info = cur.fetchall()
        print fetch_pub_photo_info

        conn.commit()

        cur.close()
        conn.close()

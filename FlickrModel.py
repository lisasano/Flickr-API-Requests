import psycopg2


class Model(object):

    def save(self):
        # open connection/cursor
        conn = psycopg2.connect("dbname=lisa user=lisa")
        cur = conn.cursor()

        query_string = self._get_query_string()
        query_values = self._get_query_string_values()

        # cur.execute()
        cur.execute(query_string, query_values)

        # commit
        conn.commit()

        # close cursor and connection
        cur.close()
        conn.close()

    def _get_query_string(self):
        raise NotImplementedError()

    def _get_query_string_values(self):
        raise NotImplementedError()



'''

Polymorphism:
    the ability to reimplement a method or other
    behavior on different subclasses of the same
    parent class.

In this example, we have a .save() method we define
on our base Model class.

Saves do some things that are common to all Model subclasses:
    + open a db connection
    + make query cursor
    + execute some query
    + commit the operations
    + close the cursor
    + close the connection

The only thing that varies is the specific query itself.

What you will want to do is implement methods on your
User and Photo classes that build that query for you.

The basic logic in Model.save() does not need to change
between the subclasses -- only the methods that build the
query and the values that get inserted into it.

THink of Model.save() as something more abstract. It knows
it needs to open the connection and get arguments for
curs.execute(). It's up to you to supply those arguments
by writing methods that can build them in the subclasses.



'''
import FlickrAPIrequest

from FlickrUser import User
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def flickr():
    return render_template('main_form.html')

@app.route('/lookup', methods=['POST'])
def lookup_route():
    email_address = request.form.get('email')
    user1 = User(email_address)
    user1.fetch_user_info()
    return user1.user_id

if __name__ == '__main__':
    app.run()
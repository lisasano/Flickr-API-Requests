import FlickrAPIrequest

from FlickrUser import User
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def flickr():
    return render_template('main_form.html')

@app.route('/lookup', methods=['POST'])
def lookup_route(user=None):
    email_address = request.form.get('email')
    user1 = User(email_address)
    user1.fetch_user_info()
    user1.save()
    user1.fetch_public_photos()
    user1.save_public_photos()
    return render_template('user_info.html', user=user1)

if __name__ == '__main__':
    app.run()
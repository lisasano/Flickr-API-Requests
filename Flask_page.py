from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def flickr():
    return render_template('main_form.html')

@app.route('/lookup.html')
def lookup_route():
    return "hi"

if __name__ == '__main__':
    app.run()
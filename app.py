from flask import Flask
from flask import url_for, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    return redirect(url_for('static', filename='activities.html'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)




    
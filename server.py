"""Twitter-Twilio Bot."""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = FLASK_SECRET_KEY 

app.jinja_env.undefined = StrictUndefined



if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    DebugToolbarExtension(app)

    app.run(port=5000,host="0.0.0.0")
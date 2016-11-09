from flask import Flask, jsonify, Blueprint
APP = Flask(__name__)

API = Blueprint('api', __name__)


TEST = {
    'name': 'text'
}

BOOKDATA = { \
            'id': "507f191e810c19729de860ea",
            'title': "50 Shades of Grey",
            'author': "E.L. James",
            'lastplayed':{'date':"2016-11-09T15:00:08+00:00", 'position':"00:23:53"},
            'bookmarks': [{'title':"Bookmark 1", 'position':"00:05:37"},
                          {'title':"Bookmark 2", 'position':"00:50:23"}],
            'chapters':  [{'title':"Bookmark 1", 'position':"00:05:37"}],
            'file':       {'integrity': "", 'length': "01:32:00",
                           'location': "file:<{LOCATIONHERE}>"},
            'available': "true"
           }

@APP.route("/")
def hello():
    """Returns Hello World."""
    return "Hello World!"
@APP.route("/json")
def json():
    """Returns JSON example."""
    return jsonify(**TEST)
@APP.route("/json/<name>")
def jsonname(name):
    """Returns JSON example with dynamic entries."""
    user = {
        'name': name
    }
    return jsonify(**user)

@API.route("/")
def helloapi():
    """Returns Hello World."""
    return "Hello welcome to this API."
@API.route("/bookdata")
def bookjson():
    """Returns JSON bookdata."""
    bookdata = BOOKDATA.copy()
    return jsonify(**bookdata)
@API.route("/booklibrary")
def booklibjson():
    """Returns BookLibrary JSON."""
    library = {\
                'data': [BOOKDATA.copy(),
                         BOOKDATA]
              }
    return jsonify(**library)
@API.route("/userdata")
def userjson():
    """Returns JSON user data."""
    userdata = { \
                'id': "507f1f77bcf86cd799439011",
                'username': "username",
                'password': "$2a$04$Cdw08X96K87OPG9u1pxkE.5QSUeeXBWh4Q3m4LHx/U4JJ3hAP2JOq",
                'name': "Joe Bloggs",
                'premium': "true"
               }
    returndata = userdata.copy()
    del returndata['password']
    return jsonify(**returndata)

APP.register_blueprint(API)
if __name__ == "__main__":
    APP.run()

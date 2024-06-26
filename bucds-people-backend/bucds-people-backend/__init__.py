import os
from flask import Flask 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'bucds-people.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    @app.route('/people')
    def people():
        return 'hello'
    
    # register the database and associated functions
    from . import db
    db.init_app(app)

    # register data testing function
    from . import data
    data.init_app(app)
    
    return app
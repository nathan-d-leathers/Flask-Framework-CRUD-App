Project based on FreeCodeCamp "Learn Flask" video. 



to start app:

$ source flask_venv/bin/activate
$ pip install flask flask-sqlalchemy

database is SQLite, it does not need to be installed. 
Database is stored in a folder called Instance. 
Database will still retain data between sessions.

Needed to adjust 2 things from tutorial:

-at some point while building I ran into HTTP Error 403 when trying to run the app locally on port 5000. By changing the port manually to 8000 i was abel to avoid the error.

-I ran into confusion trying to connect the db, specifically how it was being done in a python shell in the command line. I kept getting a context error and after much searching found that I could create a small context using the following method to build my database as the app was built 

with app.app_context():
    db.init_app(app)
    db.create_all()


Overall the lesson was a good first step but i need to spend more time in the documentation learning how they declare their models to get a firm grasp of the model/view relationship Flask employees
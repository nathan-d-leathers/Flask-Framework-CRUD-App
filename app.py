from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# App Configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# To Do List Item Model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# Context for creating a database during a session
with app.app_context():
        db.init_app(app)
        db.create_all()


# Post/Get ToDo Items
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = ToDo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task to the database'

    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html', tasks=tasks) 


# Delete ToDo Items
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was a problem deleting the task'


# Update ToDo Items
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        
        except:
            return "There was an issue updating your task"

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(port=8000,debug=True)
    


# Web Page open @ http://127.0.0.1:5000
# interesting that localhost:5000 does not open webpage, should checks docs
# added port=8000 to run on localhost:8000, avoids HTTP Error 403 on first webpage (not sure what is causing new error)
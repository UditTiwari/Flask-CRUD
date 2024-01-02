from flask import Flask ,jsonify ,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#user:password@localhost:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/flask_database'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'


db=SQLAlchemy(app)

class Task(db.Model):
    # __table__= 'tasks'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    done = db.Column(db.Boolean,default=False)

with app.app_context():
    db.create_all()

@app.get('/')
def index():
    tasks = Task.query.all()
    task_list = [
        {'id':task.id,'title':task.title, 'done':task.done} for task in tasks
    ]
    return jsonify({'tasks':task_list})

@app.post('/tasks')
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'],done=data['done'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify ({"message":'Task created succesfully'})


if __name__=='__main__':
    app.run(debug=True)

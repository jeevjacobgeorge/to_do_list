from flask import Flask,redirect,render_template,request,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable = False)
    completed = db.Column(db.Integer,default = 0)
    date_created= db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id 
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('content')
        new_task_obj = Todo(content= task_content)
        try:
            db.session.add(new_task_obj)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content= request.form.get('content')
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a issue updating your task"
    else:
        return render_template('update.html',task=task)

@app.route('/search')    
def search():
    q = request.args.get('q')
    tasks = Todo.query.filter(Todo.content.contains(q)).all()
    # Convert Todo objects to dictionaries
    tasks_list = [task.as_dict() for task in tasks]
    return jsonify(tasks_list)



if __name__ == "__main__":
    app.run(debug=True)


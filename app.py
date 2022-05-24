from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request, redirect  
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# set up our application
app = Flask(__name__, template_folder='template') 

# this code below tells the app where our DB is located
# /// is relative path of DB and //// is absolute path of DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# the below code is to initialise our DB
db = SQLAlchemy(app)

# create a model now 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable= False)
    copmleted = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def  __repr__(self):
         return f'{self.id} -- {self.content} -- {self.date_created}'
     



# setting up a index route, so when we browse to our URL we dont encounter 404. In flask u set up routes with "@" decorater like shown below.
# The inside of route should be an URL
@app.route('/', methods=['POST','GET'])
# Then we define a function for that route like shown below
def index():
    # 1.for now at beginning we just outputted a hellow world
    # return "Hello World!" 
    # 2. now the second time we are outputting a index.html page from templates
    # as soon as we refreshed the page here we can see whats indside the index.HTML page 
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding ur task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
        
#this below code is to delete the items from database. for that we have to create a route first .
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting"
    
@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)  
 


if __name__ == "__main__":
    # initially we set debug=True just incase if our code has bugs or errors they pop up on the website
    app.run(debug=True)
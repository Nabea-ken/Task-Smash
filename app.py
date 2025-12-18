#imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
#ORM-Lets you interact with the database using Python classes instead of SQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My App - Creating app using flask
app = Flask(__name__)
#Attach Scss processing to my app
Scss(app)

# Configure the extension configure SQLAlchemy 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasksmash.db" #Tells Flask which db to use 

# creating the db itself- an obj of SQLAlchemy
db = SQLAlchemy(app)

# Creating a model Data class ~ Row of data --- Inherits from SQLAlchemy’s base model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    #Object Representation - Controls how the object appears when printed - useful for debugging -Giving data back
    def __repr__(self) -> str:
        return f"Task {self.id}"



#Routes to webpages
#Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = MyTask(content=current_task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error adding task: {e}")
            return f"Error adding task: {e}"
    # See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)

# Delete a task
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print(f"Error deleting task: {e}")
        return f"Error deleting task: {e}"
    
# Update a task
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error updating task: {e}")
            return f"Error updating task: {e}"
    else:
        return render_template("edit.html", task=task)







# Runner and Debugger
if __name__ == "__main__":
    #creating a db using a context manager
    with app.app_context():
        db.create_all()

    app.run(debug=True)
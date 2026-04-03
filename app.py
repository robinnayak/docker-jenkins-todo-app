from flask import Flask, request, redirect, render_template, url_for
from models.db import db
from models.todo import Todo


app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)

with app.app_context():
    db.create_all()

# todos = [
#     {"id": 1, "task": "Learn Python", "done": False},
#     {"id": 2, "task": "Learn Flask", "done": False},
#     {"id": 3, "task": "Learn Docker", "done": False},
# ]


@app.route("/", methods= ["GET"])
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)



@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    print("task", task)
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        
    return redirect("/")


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id):
    task = request.form.get("edit_task")
    if task:
        todo = Todo.query.get(todo_id)
        todo.task = task
        db.session.commit()
        
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
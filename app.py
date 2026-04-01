from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Learn Flask", "done": False},
    {"id": 3, "task": "Learn Docker", "done": False},
]


@app.route("/", methods= ["GET"])
def index():
    return render_template("index.html", todos=todos)



@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    print("task", task)
    if task:
        new_id = max( [ todo["id"] for todo in todos ], default=0) + 1
        todos.append({"id": new_id, "task": task, "done": False})
    return redirect("/")


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id):
    global todos
    task = request.form.get("edit_task")
    if task:
        todos = [ todo for todo in todos if todo["id"] != todo_id ]
        todos.append({"id": todo_id, "task": task, "done": False})
        todos = sorted(todos, key=lambda x: x["id"])
        
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global todos
    todos = [ todo for todo in todos if todo["id"] != todo_id ]
    return redirect("/")

if __name__ == "__main__":
    # app.run(debug=True)
    from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Learn Flask", "done": False},
    {"id": 3, "task": "Learn Docker", "done": False},
]


@app.route("/", methods= ["GET"])
def index():
    return render_template("index.html", todos=todos)



@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    print("task", task)
    if task:
        new_id = max( [ todo["id"] for todo in todos ], default=0) + 1
        todos.append({"id": new_id, "task": task, "done": False})
    return redirect("/")


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id):
    global todos
    task = request.form.get("edit_task")
    if task:
        todos = [ todo for todo in todos if todo["id"] != todo_id ]
        todos.append({"id": todo_id, "task": task, "done": False})
        todos = sorted(todos, key=lambda x: x["id"])
        
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    global todos
    todos = [ todo for todo in todos if todo["id"] != todo_id ]
    return redirect("/")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
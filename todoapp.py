from flask import Flask, request, redirect, render_template_string
import re

app = Flask(__name__)

todo_items = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>To Do List</title>
</head>
<body>
    <h1>To Do List</h1>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}

    <table border="1">
        <tr>
            <th>Task</th>
            <th>Email</th>
            <th>Priority</th>
        </tr>
        {% for item in todo_items %}
        <tr>
            <td>{{ item["task"] }}</td>
            <td>{{ item["email"] }}</td>
            <td>{{ item["priority"] }}</td>
        </tr>
        {% endfor %}
    </table>

 <h2>Add New To Do Item</h2>

    <form action="/submit" method="post">
        <label for="task">Task:</label>
        <input type="text" name="task" id="task">

        <br><br>

        <label for="email">Email:</label>
        <input type="text" name="email" id="email">

        <br><br>

        <label for="priority">Priority:</label>
        <select name="priority" id="priority">
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
        </select>

        <br><br>

        <input type="submit" value="Add To Do Item">
    </form>

    <br>

    <form action="/clear" method="post">
        <input type="submit" value="Clear">
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    error = request.args.get("error", "")
    return render_template_string(html, todo_items=todo_items, error=error)

@app.route("/submit", methods=["POST"])
def submit():
    task = request.form.get("task", "").strip()
    email = request.form.get("email", "").strip()
    priority = request.form.get("priority", "").strip()

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        return redirect("/?error=Invalid email address")

    if priority not in ["Low", "Medium", "High"]:
        return redirect("/?error=Invalid priority")

    new_item = {
        "task": task,
        "email": email,
        "priority": priority
    }

    todo_items.append(new_item)
    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear():
    todo_items.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run()
   
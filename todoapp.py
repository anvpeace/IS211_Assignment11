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

   
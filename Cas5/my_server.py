# Flask is a Python Web Framework

from flask import Flask

my_app = Flask("My First App")


@my_app.route("/")
def my_home_page():
    return "HELLO THIS IS MY HOME PAGE"


@my_app.route("/users")
def my_users():
    return "I have 20 users \n Welcome to user Login"


@my_app.route("/json")
def my_json_route():
    return {"name": "Toshe"}


my_app.run()

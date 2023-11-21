from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import Users
from flask import flash

@app.route('/')
def read_all():
    users = Users.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/user/<int:user_id>')
def read_one(user_id):
    user = Users.get_one(user_id)
    return render_template("read1.html", user = user)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        if Users.validate_user(data):
            Users.save(data)
            return redirect("/")
        else:
            return redirect('/create')
    return render_template("create.html")

@app.route('/users/update', methods=['POST'])
def edit_user():
    Users.update(request.form)
    return redirect('/')

@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    Users.delete(user_id)
    return redirect('/')
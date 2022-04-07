from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/users')
def read_all():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    user_id=User.get_all()
    # print(user_id[len(user_id)-1]['id'], '_________________')
    id = user_id[len(user_id)-1]['id']
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>')
def read_one(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    # print(user)
    return render_template("read_one.html", one_user = user)

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('edit.html', one_user = user)

@app.route('/users/<int:id>/edit_user', methods=["POST"])
def edit_user(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        'id' : id
    }
    User.update(data)
    ids=data['id']
    return redirect(f'/users/{ids}')

@app.route('/users/<int:id>/delete_user/')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
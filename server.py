from flask import Flask, render_template, url_for, request, redirect
import data_handler
import bcrypt


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main_page():
    return render_template("main.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        login_user = {'user_name': request.form.get('user_name'), 'password': request.form.get('password')}
        all_users = data_handler.get_users(login_user['user_name'])
        hashed_bytes_password = all_users[0]['password'].encode('utf-8')
        pw = bcrypt.checkpw(login_user['password'].encode('utf-8'), hashed_bytes_password)
        if pw == True:
            return render_template('account.html')
        else:
            return render_template('invalid.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        password = request.form.get('password')
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed = hashed.decode('utf-8')
        users = {'user_name': request.form.get('user_name'), 'password': hashed}
        data_handler.insert_register(users)
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
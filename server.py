from flask import Flask, render_template, url_for, request, redirect
import data_handler


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main_page():
    if request.method == 'GET':
        all_users = data_handler.get_users()
        return render_template("main.html", all_users=all_users)


@app.route("/login", methods=['GET', 'POST'])
def login():
    all_users = data_handler.get_users()
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        login_user = {'user_name': request.form.get('user_name'), 'password': request.form.get('password')}
        if login_user in all_users:
            return render_template('account.html')
        else:
            return render_template('invalid.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        users = {'user_name': request.form.get('user_name'), 'password': request.form.get('password')}
        data_handler.insert_register(users)
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
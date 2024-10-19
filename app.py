from flask import Flask, render_template, request, redirect, url_for
from flask import session as flask_session
from models.models import Post, User
from database.db import get_session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'secret'
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form['name']
		flask_session['user'] = user
		return redirect(url_for('posts'))
	else:
		return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
	flask_session.pop('user', None)
	return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def posts():
	if 'user' not in flask_session:
		return redirect(url_for('login'))
	return render_template('index.html')  # posts=Post.query.all())


if __name__ == '__main__':
	app.run(debug=True, port=5001)

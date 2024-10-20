from flask import Flask, render_template, request, redirect, url_for
from flask import session as flask_session
from models.models import Post
from database.db import get_session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'secret'
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form['name']
		flask_session['user'] = user
		return redirect(url_for('index'))
	else:
		return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
	flask_session.pop('user', None)
	return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def index():  # main page: all posts
	if 'user' not in flask_session:
		return redirect(url_for('login'))
	with get_session() as session:
		return render_template('index.html', posts=session.query(Post).all())


@app.route('/add', methods=['GET', 'POST'])
def add_post():
	if 'user' not in flask_session:
		return redirect(url_for('login'))
	if request.method == 'POST':
		with get_session() as session:
			post = Post(user_name=flask_session['user'], content=request.form['content'])
			session.add(post)
		return redirect(url_for('index'))
	else:
		return render_template('add_post.html')


if __name__ == '__main__':
	app.run(debug=True, port=5002)


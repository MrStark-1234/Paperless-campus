from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applications.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='not approved')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            if user.role == 'student':
                return redirect(url_for('student'))
            elif user.role == 'teacher':
                return redirect(url_for('teacher'))
        else:
            return 'Invalid login credentials'
    else:
        return render_template('login.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        text = request.form['application']
        application = Application(text=text)
        db.session.add(application)
        db.session.commit()
        return 'Application submitted successfully'
    else:
        return render_template('student.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'POST':
        id = request.form['id']
        status = request.form['status']
        application = Application.query.get(id)
        application.status = status
        db.session.commit()
        return 'Application updated successfully'
    else:
        applications = Application.query.all()
        return render_template('teacher.html', applications=applications)

if __name__ == '__main__':
    app.run(debug=True)

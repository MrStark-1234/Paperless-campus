from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if username and password are valid
    # Here, you could check against a database of registered users

    if username == 'admin' and password == 'password':
        return 'Logged in successfully!'
    else:
        return 'Invalid login credentials'

if __name__ == '__main__':
    app.run(debug=True)

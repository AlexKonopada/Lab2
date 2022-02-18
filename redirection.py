from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('lab2_2.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return user
    else:
        return render_template('lab2_2.html')
if __name__ == '__main__':
    app.run()
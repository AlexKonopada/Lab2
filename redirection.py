import twitter2
from lab2_3 import main
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'] )
def home():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('create_map', usr = user ))
    else:
        return render_template('lab2_2.html')

@app.route('/<usr>')
def create_map(usr):
    main(usr)
    
    return render_template('tavarischi.html')
if __name__ == '__main__':
    app.run()

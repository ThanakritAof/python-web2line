from flask import Flask,render_template,request

import reply # from file reply.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    item = request.form['text']
    reply.send(item)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

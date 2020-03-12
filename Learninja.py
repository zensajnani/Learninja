from learninja import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/base2')
def base2():
    return render_template('base2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




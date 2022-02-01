from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show_trainings')
def show_trainings():
    return render_template('show_trainings.html')

@app.route('/add_training')
def add_training():
    return render_template('add_training.html')

@app.route('/add_exercise')
def add_exercise():
    return render_template('add_exercise.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
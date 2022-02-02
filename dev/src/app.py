import os
import this
from unittest import result
from flask import Flask, render_template, url_for, redirect
from flask_migrate import Migrate
import sqlalchemy
from models import db, Exercise, Training, trainings_exercises
from forms import AddExerciseForm, AddTrainingForm, UpdateTrainingForm
from wtforms import SelectFieldBase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### DATABASE SECTION
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
####

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show_trainings')
def show_trainings():
    trainings = Training.query.all()

    return render_template('show_trainings.html', trainings=trainings)

@app.route('/add_training', methods=['GET', 'POST'])
def add_training():
    form = AddTrainingForm()

    if form.validate_on_submit():
        training_date = form.training_date.data

        new_training = Training(training_date)
        db.session.add(new_training)
        db.session.commit()

        return redirect(url_for('show_trainings'))

    return render_template('add_training.html', form=form)

@app.route('/training/<id>', methods=['GET', 'POST'])
def show_training(id):
    def get_available_exercises():

        available_exercises = Exercise.query.all()
        return_list = []
        
        for exercise in available_exercises:
            return_list.append((exercise.exercise_id, exercise.name))

        return return_list
    
    this_training = Training.query.get(id)
    result_joined = db.session.query(Training, Exercise, trainings_exercises).join(Training.exercises).join(trainings_exercises).filter(Training.training_id == id)

    result_joined_clean = []
    for row in result_joined:
        new_row = []
        new_row.append(row[1])
        new_row += row[4:]
        result_joined_clean.append(new_row)

    form = UpdateTrainingForm()
    
    available_choices = get_available_exercises()
    form.exercises.choices = available_choices

    return render_template('training.html', id=id, form=form, this_training=this_training, result_joined_clean=result_joined_clean)

@app.route('/show_exercises')
def show_exercises():
    exercises = Exercise.query.all()

    return render_template('show_exercises.html', exercises=exercises)

@app.route('/add_exercise', methods=['GET', 'POST'])
def add_exercise():
    form = AddExerciseForm()

    if form.validate_on_submit():
        name = form.name.data
        kcals_per_rep = form.kcals_per_rep.data
        type_of_exercise = form.type_of_exercise.data

        new_exercise = Exercise(name, kcals_per_rep, type_of_exercise)
        db.session.add(new_exercise)
        db.session.commit()

        return redirect(url_for('show_exercises'))

    return render_template('add_exercise.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
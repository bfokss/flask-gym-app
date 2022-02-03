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
    
    def delete_exercise():
        print('delete')

    this_training = Training.query.get(id)
    query_text = sqlalchemy.sql.text(f"""
        SELECT te.id, e.name, e.kcals_per_rep, te.repeats, te.weight, te.time
        FROM trainings t
            JOIN trainings_exercises te
                ON t.training_id = te.training_id
            JOIN exercises e
                ON te.exercise_id = e.exercise_id 
        WHERE t.training_id = {id}
        ORDER BY e.name ASC""")

    query_result = db.engine.execute(query_text)
    query_list = [list(row) for row in query_result]

    kcals_total = 0
    result_joined_clean = []
    for row in query_list:
        new_row = {}
        new_row['id'] = row[0]
        new_row['exercise_name'] = row[1]
        new_row['exercise_kcals_per_rep'] = row[2]
        new_row['repeats'] = row[3]
        new_row['weight'] = row[4]
        new_row['time'] = row[5]
        new_row['total_kcals'] = (new_row['exercise_kcals_per_rep'] * (new_row['repeats'] or '')) or (new_row['exercise_kcals_per_rep'] * (new_row['time'] or ''))

        try:
            kcals_total += new_row['total_kcals']
        except:
            kcals_total += 0

        result_joined_clean.append(new_row)

    form = UpdateTrainingForm()
    
    available_choices = get_available_exercises()
    form.exercises.choices = available_choices
    
    if form.validate_on_submit():
        exercise_id = form.exercises.data
        repeats = form.repeats.data
        weight = form.weight.data
        time = form.time.data

        new_insert = trainings_exercises.insert().values(training_id=int(id), exercise_id=int(exercise_id), repeats=repeats, weight=weight, time=time)

        db.engine.execute(new_insert)

        print('insert successful!')

        return redirect(url_for('show_training', id=id))

    return render_template('training.html', id=id, form=form, this_training=this_training, result_joined_clean=result_joined_clean, kcals_total=kcals_total)

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

@app.route('/training/<training_id>/delete/<exercise_id>')
def delete_exercise(training_id, exercise_id):
    query_text = sqlalchemy.sql.text(f"""
        DELETE FROM trainings_exercises
        WHERE id={exercise_id};""")
    
    db.engine.execute(query_text)
    print('delete')

    return redirect(url_for('show_training', id=training_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
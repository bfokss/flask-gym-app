from random import choices
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, FloatField, validators
from wtforms.fields.html5 import DateField
from models import Exercise


class AddExerciseForm(FlaskForm):
  name = StringField('Name of the exercise: ')
  kcals_per_rep = IntegerField('Kcals per repeat/minute: ')
  type_of_exercise = RadioField('Type of exercise: ', choices=[('repeatable', 'repeatable'), ('time-based', 'time-based')])
  submit = SubmitField('Add exercise')

class AddTrainingForm(FlaskForm):
  training_date = DateField('Date of training: ', format='%Y-%m-%d')
  submit = SubmitField('Add training')

class UpdateTrainingForm(FlaskForm):
  exercises = SelectField("Exercise: ", validate_choice=False)
  repeats = IntegerField('Repeats: ', validators=[validators.Optional()])
  weight = FloatField('Weight: ', validators=[validators.Optional()])
  time = FloatField('Time: ', validators=[validators.Optional()])
  submit = SubmitField('Add exercise')

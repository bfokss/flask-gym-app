from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

trainings_exercises = db.Table('trainings_exercises',
  db.Column('training_id', db.Integer, db.ForeignKey('trainings.training_id'), primary_key=True),
  db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.exercise_id'), primary_key=True),
  db.Column('repeats', db.Integer),
  db.Column('weight', db.Float),
  db.Column('time', db.Float)
)

class Exercise(db.Model):
  __tablename__ = 'exercises'
  exercise_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  kcals_per_rep = db.Column(db.Integer)
  type_of_exercise = db.Column(db.Text)
  trainings = db.relationship(
    'Training', 
    secondary=trainings_exercises,
    backref='trainings_exercises')

  def __init__(self, name, kcals_per_rep, type_of_exercise):
    self.name = name
    self.kcals_per_rep = kcals_per_rep
    self.type_of_exercise = type_of_exercise

  def __repr__(self):
    if self.type_of_exercise == 'repeatable':
      return f'Exercise {self.name} that burns {self.kcals_per_rep}kcals/repeat and is of type {self.type_of_exercise}'

    else:
      return f'Exercise {self.name} that burns {self.kcals_per_rep}kcals/minute and is of type {self.type_of_exercise}'


class Training(db.Model):
  __tablename__ = 'trainings'
  training_id = db.Column(db.Integer, primary_key=True)
  training_date = db.Column(db.Date, nullable=False)
  exercises = db.relationship(
    'Exercise', 
    secondary=trainings_exercises,
    backref='exercies_trainings')

  def __init__(self, training_date):
    self.training_date = training_date

  def __repr__(self):
    return f'Training with ID={self.training_id} made on {self.training_date}'

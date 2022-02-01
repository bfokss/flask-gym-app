from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Exercise(db.Model):
  __tablename__ = 'exercises'
  exercise_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  kcals_per_rep = db.Column(db.Integer)
  type_of_exercise = db.Column(db.Text)

  def __init__(self, name, kcals_per_rep, type_of_exercise):
    self.name = name
    self.kcals_per_rep = kcals_per_rep
    self.type_of_exercise = type_of_exercise

  def __repr__(self):
    if self.type_of_exercise == 'repeatable':
      return f'Exercise {self.name} that burns {self.kcals_per_rep}kcals/repeat and is of type {self.type_of_exercise}'

    else:
      return f'Exercise {self.name} that burns {self.kcals_per_rep}kcals/minute and is of type {self.type_of_exercise}'
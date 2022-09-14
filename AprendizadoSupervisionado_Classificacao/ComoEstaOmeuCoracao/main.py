
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('savedmodelrandom.sav', 'rb'))

@app.route('/')
def home():
  result = ''
  
  return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
  Age = int(request.form['Age'])
  Sex = int(request.form['Sex'])
  ChestPainType = int(request.form['ChestPainType'])
  RestingBP = int(request.form['RestingBP'])
  Cholesterol = int(request.form['Cholesterol'])
  FastingBS = int(request.form['FastingBS'])
  RestingECG = int(request.form['RestingECG'])
  MaxHR = int(request.form['MaxHR'])
  ExerciseAngina = int(request.form['ExerciseAngina'])
  Oldpeak = int(request.form['Oldpeak'])
  ST_Slope = int(request.form['ST_Slope'])

  result = model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])[0]

  if  result == 1:
    result = 'O paciente POSSUI tendência de problemas cardíacos'
  else:
    result = 'O paciente NÃO POSSUI tendência de problemas cardíacos'

  return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)




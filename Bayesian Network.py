import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel

dataset = pd.read_csv('Heart Disease.csv')

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'trestbps'),
					   ('exang', 'trestbps'), ('trestbps', 'heartdisease'), ('fbs', 'heartdisease'),
					   ('heartdisease', 'restecg'), ('heartdisease', 'thalach'), ('heartdisease', 'chol')])

print('\nLearning CPDs using Maximum Likelihood Estimators...')
model.fit(dataset)

print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 37, 'sex': 1})
print(q)

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 37})
print(q)

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'sex': 1})
print(q)

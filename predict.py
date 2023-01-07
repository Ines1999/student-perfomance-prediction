import sys
import pandas as pd
import joblib
from sklearn import model_selection


def function(argv):
	input = argv[1]
	data = pd.read_excel(input)
	loaded_model = joblib.load('./Models/decision_tree.pkl')
	result = loaded_model.predict(data)

	if int(result) == 0:
		print("This student is most likely to fail the mathematics subject")
	else:
		print("This student is most likely to pass the mathematics subject")

if __name__ == '__main__':
	function(sys.argv)
import sys
import pandas as pd
import joblib
from sklearn import model_selection


def function(argv):
    input = argv[1]
    data = pd.read_excel(input)
    loaded_model = joblib.load('./Models/knn.pkl')
    result = loaded_model.predict(data)

    if int(result) == 0:
        print("OPS :(!This student is most likely to fail the mathematics subject")
    else:
        print("YAY!This student is most likely to pass the mathematics subject")

function(sys.argv)
from flask import Flask
from flask import render_template, request, redirect, url_for
import csv
import pandas as pd
import prediction

app = Flask(__name__)

# adding the csv file headers
def add_header():
    header = ['lastName', 'firstName', 'failures', 'absences', 'schoolsup', 'Mjob', 'reason', 'guardian', 'paid',
              'Fedu', 'goout', 'studytime', 'traveltime', 'G1', 'G3']
    with open('test.csv', 'w', encoding='UTF8') as f:
        writer1 = csv.writer(f)
        # write the header
        writer1.writerow(header)


add_header()


@app.route("/home")
def hello():
    return render_template("home.html")


@app.route("/")
def hello_world():
    return redirect("/home")


# serving prediction pages

@app.route("/prediction")
def prediction_template():
    df = pd.read_csv('test.csv')
    if (df.empty is True):
        return redirect(url_for('addStudentForm'))

    prediction.predictionResults()
    prediction.sortingAccurcy()
    accList = list(prediction.s_accuracyPrediction.keys())
    bestAlgo = accList[0]
    bestAlgoResult = prediction.classificationResultsPrediction[bestAlgo]
    return render_template("prediction.html", bestALgo=bestAlgo,acc=prediction.s_accuracyPrediction,
                           bestAlgoResult=bestAlgoResult,
                           zip=zip, list=list, noms=prediction.noms,prenoms=prediction.prenoms )


# adding a student form
@app.route("/form", methods=["POST", "GET"])
def addStudentForm():
    if request.method == "POST":
        data = []
        storing_form_data(data)

        with open('test.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            # write the data
            writer.writerow(data)

        data.clear()
        return render_template("form.html")
    else:
        return render_template('form.html')


# clearing the csv file from the data + adding the header
@app.route("/clearing")
def empty_file():
    file = open('test.csv', "r+")
    file.truncate(0)
    file.close()
    add_header()
    return redirect(url_for('addStudentForm'))


@app.route('/dataset')
def another_page():
    table = pd.read_csv("test.csv")
    return render_template("students.html", data=table.to_html())


def storing_form_data(data):
    lastName = request.form["lastName"]
    data.append(lastName)
    firstName = request.form["firstName"]
    data.append(firstName)
    failures = request.form["failures"]
    data.append(failures)
    absences = request.form["absences"]
    data.append(absences)
    schoolsup = request.form["schoolsup"]
    data.append(schoolsup)
    Mjob = request.form["Mjob"]
    data.append(Mjob)
    reason = request.form["reason"]
    data.append(reason)
    guardian = request.form["guardian"]
    data.append(guardian)
    paid = request.form["paid"]
    data.append(paid)
    Fedu = request.form["Fedu"]
    data.append(Fedu)
    goout = request.form["goout"]
    data.append(goout)
    studytime = request.form["studytime"]
    data.append(studytime)
    traveltime = request.form["traveltime"]
    data.append(traveltime)
    G1 = request.form["G1"]
    data.append(G1)
    G3 = request.form["G3"]
    data.append(G3)


# reading
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

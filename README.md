## Research Question

By providing data attributes including student grades and demographic, social, and school-related features, can we predict a student's final academic performance? 

### Introduction

The dataset (https://archive.ics.uci.edu/ml/datasets/student+performance) we used in this project is from the UCI Machine Learning Repository. This data approach approaches student achievement in secondary education at two Portuguese schools. The data attributes include student grades, demographic, social, and school-related features, and they were collected using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: mathematics (mat) and Portuguese (por). 

### Folders & Files 

- dataset files : 
    * student-mat.csv
    * student-por.csv
- Preprocessing files : 
    * Preprocessing_classification_regression.ipynb
    * Preprocessing_classification.ipynb
    * dataset_classification.csv : a dataset created after preprocessing our intial dataset 
- Modeling files :
    * Classification.ipynb
    * Modeling_classification_and_regression.ipynb
- Web Application files : webapp folder which contains the following : 
    * templates folder : contains the different HTML files for our web application
    * static : contains the different CSS files for our web application
    * prediction.py : contains different prediction function for each one of our models 
    * app.py : contains all of the process of creating our web application (this is the final that is executed when runing our application)
    * test.csv : created when different information about a student is entered through the web application form
- Other useful files :
    * predict.py : a script that takes a data file as an argument ( we created this file to be able to run the requested scenario )
    * model_test.xlsx : an example of data file that can be given as an argument to predict.py 
    * Dockerfile
    * requirements.txt : contains the different libraries that need to be installed to build our docker image 

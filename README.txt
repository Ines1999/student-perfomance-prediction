## Research Question

By providing data attributes including student grades and demographic, social, and school-related features, can we predict a student's final academic performance? 

### Introduction

The dataset (https://archive.ics.uci.edu/ml/datasets/student+performance) we used in this project is from the UCI Machine Learning Repository. This data approach approaches student achievement in secondary education at two Portuguese schools. The data attributes include student grades, demographic, social, and school-related features, and they were collected using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: mathematics (mat) and Portuguese (por). 


### Steps

For our project, there are three significant steps: 

1. First, we'll create a branch for preprocessing so that we can gain some insight into the features and our target (which is either a student's grade if it's a regression problem or whether he passed or failed if it's a classification problem, depending on the features we choose). This is what we've been trying to do today. 

2- The second thing that interests us the most is modeling. Here we are going to try different supervised models and compare them in order to choose the one that gives the best results for our problem. 

* In essence, we will train our model with four different feature combinations.
1. Keep all the features. 
2. Keep all other features and only remove Grade 2. 
3. Keep all other features; only remove Grade 1 and Grade 2. 
4. Keep only Grade 1 and Grade 2 features.  

3- For our last step, we will create a web application that uses the models that we've created to make new predictions on new data that can be submitted directly by users through the interface.

These three steps will be pushed separately into three branches: Preprocessing - Modeling- Webapp.
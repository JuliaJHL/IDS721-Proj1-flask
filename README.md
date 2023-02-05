[![CI](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/cicd.yml/badge.svg)](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/cicd.yml)
## Cloud Continuous Delivery of Microservice (MLOps or Data Engineering Focused)

In this project, I wrote an Iris species prediction model in python and built the microservice using flask.

[!!!!!todo]

### Requirements
* Create a Microservice in Flask or Fast API
* Push source code to Github
* Configure Build System to Deploy changes
* Use IaC (Infrastructure as Code) to deploy code
* Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
* Containerization is optional, but recommended

### Dataset and Model
* I used Iris data set which is made by Ronald Fisher in his 1936 paper. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris versicolor and Iris virginica). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 
* I applied `RandomForestClassifier()` as the model for training and prediction.

### GitHub Actions
* Apply GitHub Actions as build system to deploy changes. 
  * do automatically code format, lint and test.
  * based on `Makefile` and `workflows/cicd.yml`


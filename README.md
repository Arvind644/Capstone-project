# Capstone-project

# house-price prediction project

We are making a house-price prediction model which tell the price of house

## Problem description

In this project, we are predicting price of house. The model take variables and predict the price


## file structure

notebook.ipynb - main jupyter noetbook <br />
app.py - contain extract and main model from jupyter noetbook.  <br />
prediction_regression_project.py - it perdict the result. <br /> 
predict-test.py - contain sample data <br /> 
best_model.pkl, poly.pkl, scalar.pkl - it saveds the model. <br />
Dockerfile - to riun the application in docker image

## Deployment of model

I am currently using Windows, so I am using waitress in order to deploy the model. To deploy this model with waitress, please use: waitress-serve --listen=0.0.0.0:9696 predict:app

# Docker

If you choose to build a docker file locally instead, here are the steps to do so:

In your command line, run: docker run -it --rm --entrypoint=bash python:3.8.12-slim to create a docker image.

Create a Dockerfile as such:
````
```
FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock",  "./"]

RUN pipenv install --system --deploy

COPY ["prediction_regression_project.py", "best_model.pkl", "poly.pkl", "scalar.pkl", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "app:app"]
```
````
This allows us to install python, run pipenv and its dependencies, run our predict script and our model itself and deploys our model using waitress. Similarly, you can just use the dockerfile in this repository.

Details regarding input
````
```
 """House Price Prediction
    Note: Only for houses with Latitude Ranging from: 24.93 - 24.97 , Longitude: 121.47 - 121.54
    ---
    parameters:
        - name: House Age
          in: query
          type: number
          description: "0 - 43"
          required: true
        - name: Distance_to_the_nearest_MRT_station
          in: query
          type: number
          description: "24 - 4k"
          required: true
        - name: number_of_convenience_stores
          in: query
          type: number
          description: "0-10"
          required: true
        - name: Latitude
          in: query
          type: number
          description: "24.93-25"
          required: true
        - name: Longitude
          in: query
          type: number
          description: "121.47 - 121.57"
          required: true
    responses:
          200:
              description: The output values
    """
````
```
![alt text](https://github.com/Arvind644/Capstone-project/blob/main/a.jpg?raw=true)

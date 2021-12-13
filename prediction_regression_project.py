import numpy as np
import joblib

loaded_model = joblib.load('best_model')
poly = joblib.load('polynomial feature')
sc = joblib.load('scaler')

def prediction(model,poly,sc):
    l=[]
    l.append(float(input('Enter House Age: ')))
    l.append(float(input('distance to the nearest MRT station: ')))
    l.append(float(input('number of convenience stores: ')))
    l.append(float(input('Latitude: ')))
    l.append(float(input('Longitude: ')))
    arr = np.asarray([l])
    arr = poly.transform(arr)
    print(arr.shape)
    scaled_arr = sc.transform(arr)
    print('Price of the house per unit area: ', round(model.predict(scaled_arr)[0][0],2))

prediction(loaded_model,poly,sc)


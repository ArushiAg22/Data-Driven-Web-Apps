import pickle

def predict(age, sex, bmi, children, smoker, region):

    model = pickle.load(open('rf_model.pkl', 'rb'))

    prediction = model.predict([[age, sex, bmi, children, smoker, region]])
    output = round(prediction[0], 2)
    data = [age, sex, bmi, children, smoker, region, output]
    return{"data":[age, sex, bmi, children, smoker, region, output]}

from flask import Flask, redirect, url_for, render_template, request
import prediction
import ml
import data
import database

app = Flask(__name__)
app.app_context().push()

with app.app_context():
    @app.route('/')
    def default():
        return database.database()


    @app.route('/getdata')
    def get_data():
        return data.get_data()


    @app.route('/train')
    def train_model():
        return ml.ML_model()


    @app.route('/predict', methods=['POST'])
    def predict():
        input = request.json["data"]
        return prediction.predict(input[0], input[1], input[2], input[3], input[4], input[5])


    @app.route('/add', methods=['POST'])
    def add_data():
        input = request.json["data"]
        return data.add_data(input)


if __name__ == '__main__':
    app.run()

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'), encoding='bytes')


@app.route('/')
def home():
    return render_template('index.html', result="")


@app.route('/', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    outlook = int(request.form['outlook'])
    temperature = int(request.form['temperature'])
    humidity = int(request.form['humidity'])
    windy = int(request.form['windy'])

    x = np.array([[outlook, temperature, humidity, windy]])

    prediction = model.predict(x)
    output = round(prediction[0], 0)

    if(output == 0):
        prediction = "Sorry, stay inside :("
    elif(output == 1):
        prediction = "Yeah, U can play :)"

    return render_template('index.html', result=prediction, outlook=outlook, temperature=temperature, humidity=humidity, windy=windy)


if __name__ == "__main__":
    app.run(debug=True)

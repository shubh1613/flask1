import pickle

from flask import Flask, request, render_template

app = Flask("prediction")
kodel = pickle.load(open('score1.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
        hours = float(request.form['hours'])

        prediction = kodel.predict([[hours]])
        output = round(prediction[0], 2)

        return render_template('predict.html', text='Your score is {}%'.format(output))



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import request
from flask_cors import CORS
import joblib
app= Flask(__name__)
app.config["DEBUG"] = True
# app= Flask(__name__)


CORS(app)

@app.route('/',methods=['GET'])
def home():
    return '<h1> API is working... </h1>'

@app.route('/hello',methods=['GET'])
def hello():
    return " Hello API "


@app.route('/predict',methods=['GET'])
def predict():
    model = joblib.load('marrige_age.ml')
    age= model.predict([[int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms'])
                           ]])
    return str(round(age[0],2))

if __name__ == "__main__":
  app.run(port=5000, debug=True)

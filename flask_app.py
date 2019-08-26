import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS
from model import spell_model

app = Flask(__name__)
CORS(app)
@app.route('/spellCorrect/<word>')
def return_price(word):
  #word = request.args.get('word')
  model = spell_model()
  corrected_words  = model.predict(word)
  output_dict = {
                'corrected_words': corrected_words
                }
  print(output_dict)
  #return jsonify(output_dict)


@app.route("/",methods=['GET'])
def default():
    return "<h1> Welcome to spell corrector <h1>"

if __name__ == "__main__":
    app.run()
from flask import Flask,jsonify,request
from flask_cors import CORS
from model import spell_corrector

app = Flask(__name__)
CORS(app)
@app.route("/spellCorrect/<word>")
def return_words(word):
  spell_corrector_object = spell_corrector()
  corrected_words  = spell_corrector_object.predict(word)
  corrected_words = ' '.join(corrected_words)
  output_dict = {
                'corrected_words': corrected_words
                }
  return jsonify(output_dict)

@app.route("/",methods=['GET'])
def default():
  return "<h1> Welcome to spell corrector <h1>"

if __name__ == "__main__":
    app.run()

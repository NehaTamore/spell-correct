import pickle
from spell_corrector import correction

class spell_model:
    def __init__(self):
        pass

    def deserialize(self):
        # de-serialize spell_corrector.pkl file into an object called model using pickle
        with open('spell_corrector.pkl', 'rb') as handle:
            model = pickle.load(handle)
        return model

    def predict(self, word):
        return correction(word)


import pickle
from spell_corrector import correction

class spell_model:
    def __init__(self):
        pass

    def predict(self, word):
        return correction(word)


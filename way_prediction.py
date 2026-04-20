import random

class WayPrediction:
    def __init__(self, prediction_accuracy=0.8,
                 energy_predict=0.2,
                 energy_mispredict=0.8):
        self.prediction_accuracy = prediction_accuracy
        self.energy_predict = energy_predict
        self.energy_mispredict = energy_mispredict
        self.extra_energy = 0

    def predict(self):
        if random.random() < self.prediction_accuracy:
            self.extra_energy += self.energy_predict
            return True
        else:
            self.extra_energy += self.energy_mispredict
            return False

    def get_prediction_energy(self):
        return self.extra_energy
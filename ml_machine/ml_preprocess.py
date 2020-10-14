from sklearn.model_selection import train_test_split

class Preprocess():
    def __init__(self, machine, data):
        self.M = machine
        self.dataX = data[0]
        self.datay = data[1]
        self.X, self.Xtest, self.y, self.ytest =  train_test_split(self.dataX, self.datay)

    def train(self):
        if self.M.setup['dont_train_test_split'] == True:
            return self.dataX, self.datay
        else:
            return self.X, self.y

    def test(self):
        return self.Xtest, self.ytest



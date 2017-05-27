import numpy as np


class ThirdNeutralNetworks(object):
    def __init__(self, X, y):
        self.X = X
        self.y = y
        pass

    def nonlin(self, x, deriv=False):
        if (deriv == True):
            return x * (1 - x)

        return 1 / (1 + np.exp(-x))

    def get_synx(self):
        np.random.seed(1)

        # randomly initialize our weights with mean 0
        syn0 = 2 * np.random.random((7, 8)) - 1
        syn1 = 2 * np.random.random((8, 1)) - 1

        for j in range(60000):

            # Feed forward through layers 0, 1, and 2
            l0 = self.X
            l1 = self.nonlin(np.dot(l0, syn0))
            l2 = self.nonlin(np.dot(l1, syn1))

            # how much did we miss the target value?
            l2_error = self.y - l2

            if (j % 10000) == 0:
                print("Error:" + str(np.mean(np.abs(l2_error))))

            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            l2_delta = l2_error * self.nonlin(l2, deriv=True)

            # how much did each l1 value contribute to the l2 error (according to the weights)?
            l1_error = l2_delta.dot(syn1.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            l1_delta = l1_error * self.nonlin(l1, deriv=True)

            syn1 += l1.T.dot(l2_delta)
            syn0 += l0.T.dot(l1_delta)
        print("Output After Training:")
        print(l1)
        # print("111")
        # print(l1.dot(X))
        print(l2)
        return syn0, syn1

    def predict(self, x):
        syn0, syn1 = self.get_synx()
        input = self.nonlin(np.dot(x, syn0))
        out = self.nonlin(np.dot(input, syn1))
        print("out=", out)
        if out[0] - 0.9 > 0:
            print("succeed")
            return True
        else:
            print("failed")
            return False

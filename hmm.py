import csv
import time
import numpy as np


'''
构建一个 Python 版本的框架

'''


class Hmm:
    def __init__(self, Ann, Bnm, pi1n):
        self.A = np.array(Ann)
        self.B = np.array(Bnm)
        self.pi = np.array(pi1n)
        self.N = self.A.shape[0]
        self.M = self.B.shape[1]

    def test(self):
        print('ok')
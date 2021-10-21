#!/usr/bin/python

#########################################
# module: cs5600_6600_f21_hw02.py
# YOUR NAME: Connor Osborne
# YOUR A#: A01880782
#########################################

import numpy as np
import pickle
from cs5600_6600_f21_hw02_data import *


# sigmoid function and its derivative.
# you'll use them in the training and fitting
# functions below.
def sigmoidf(x):
    # your code here
    return 1 / (1 + np.exp(-x))


def sigmoidf_prime(x):
    # your code here
    return x * (1 - x)


# persists object obj to a file with pickle.dump()
def save(obj, file_name):
    with open(file_name, 'wb') as fp:
        pickle.dump(obj, fp)


# restores the object from a file with pickle.load()
def load(file_name):
    with open(file_name, 'rb') as fp:
        obj = pickle.load(fp)
    return obj


def build_nn_wmats(mat_dims):
    # your code here
    weights = []
    np.random.seed(33)
    for x in range(len(mat_dims) - 1):
        w = np.random.randn(mat_dims[x], mat_dims[x + 1])
        weights.append(w)

    weights = tuple(weights)
    return weights


def build_231_nn():
    return build_nn_wmats((2, 3, 1))


def build_2331_nn():
    return build_nn_wmats((2, 3, 3, 1))


def build_221_nn():
    return build_nn_wmats((2, 2, 1))


def build_838_nn():
    return build_nn_wmats((8, 3, 8))


def build_949_nn():
    return build_nn_wmats((9, 4, 9))


def build_4221_nn():
    return build_nn_wmats((4, 2, 2, 1))


def build_421_nn():
    return build_nn_wmats((4, 2, 1))


def build_121_nn():
    return build_nn_wmats((1, 2, 1))


def build_1221_nn():
    return build_nn_wmats((1, 2, 2, 1))


# Training 3-layer neural net.
# X is the matrix of inputs
# y is the matrix of ground truths.
# build is a nn builder function.
def train_3_layer_nn(numIters, X, y, build):
    # your code here
    nn = []
    w1, w2 = build()

    for i in range(numIters):
        # forward
        z2 = np.dot(X, w1)
        a2 = sigmoidf(z2)
        z3 = np.dot(a2, w2)
        yHat = sigmoidf(z3)

        # back propogation
        yHat_err = y - yHat
        yHat_delta = yHat_err * sigmoidf_prime(yHat)

        a2_error = yHat_delta.dot(w2.T)
        a2_delta = a2_error * sigmoidf_prime(a2)

        w2 += a2.T.dot(yHat_delta)
        w1 += X.T.dot(a2_delta)

        nn = yHat

    return w1, w2


def train_4_layer_nn(numIters, X, y, build):
    # your code here
    nn = []
    w1, w2, w3 = build()

    for i in range(numIters):
        # forward
        z2 = np.dot(X, w1)
        a2 = sigmoidf(z2)
        z3 = np.dot(a2, w2)
        a3 = sigmoidf(z3)
        z4 = np.dot(a3, w3)
        yHat = sigmoidf(z4)

        # back propogation
        yHat_err = y - yHat
        yHat_delta = yHat_err * sigmoidf_prime(yHat)

        a3_error = yHat_delta.dot(w3.T)
        a3_delta = a3_error * sigmoidf_prime(a3)

        a2_error = a3_delta.dot(w2.T)
        a2_delta = a2_error * sigmoidf_prime(a2)

        w3 += a3.T.dot(yHat_delta)
        w2 += a2.T.dot(a3_delta)
        w1 += X.T.dot(a2_delta)

        nn = yHat

    return w1, w2, w3


def fit_3_layer_nn(x, wmats, thresh=0.4, thresh_flag=False):
    # your code here
    z2 = np.dot(x, wmats[0])
    a2 = sigmoidf(z2)
    z3 = np.dot(a2, wmats[1])
    yHat = sigmoidf(z3)

    if thresh_flag is True:
        if yHat[0] > thresh:
            return 1
        else:
            return 0
    else:
        return yHat


def fit_4_layer_nn(x, wmats, thresh=0.4, thresh_flag=False):
    # your code here
    z2 = np.dot(x, wmats[0])
    a2 = sigmoidf(z2)
    z3 = np.dot(a2, wmats[1])
    a3 = sigmoidf(z3)
    z4 = np.dot(a3, wmats[2])
    yHat = sigmoidf(z4)

    if thresh_flag is True:
        if yHat[0] > thresh:
            return 1
        else:
            return 0
    else:
        return yHat


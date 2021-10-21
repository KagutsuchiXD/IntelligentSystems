# /usr/bin/python

from ann import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

####################################
# CS5600/6600: F21: HW04
# Your Name: Connor Osborne
# Your A#: A01880782
# Write your code at the end of
# this file in the provided
# function stubs.
#
#
# net1 Best Results:
# Testing: eta=0.2, lambda=0.2, number of nodes=10
# Epoch 29 training complete
# Cost on training data: 0.41147697887755064
# Accuracy on training data: 47063 / 50000
# Cost on evaluation data: 0.5816038967303068
# Accuracy on evaluation data: 9259 / 10000
#
#
# net2 Best Results:
# Testing: eta=0.3, lambda=0.5, n1=11, n2=11
# Epoch 29 training complete
# Cost on training data: 0.4306176076130792
# Accuracy on training data: 47221 / 50000
# Cost on evaluation data: 0.7489069428124053
# Accuracy on evaluation data: 9295 / 10000
#
#
# net3 Best Results:
# Testing: eta=0.3, lambda=0.1, n1=11, n2=10, n3=11
# Epoch 29 training complete
# Cost on training data: 0.403367517358154
# Accuracy on training data: 47132 / 50000
# Cost on evaluation data: 0.5734782520493629
# Accuracy on evaluation data: 9291 / 10000
#####################################


# auxiliary functions
from mnist_loader import load_data_wrapper


def load(filename):
    """Load a neural network from the file ``filename``.  Returns an
    instance of ann.

    """
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    cost = getattr(sys.modules[__name__], data["cost"])
    net = ann(data["sizes"], cost=cost)
    net.weights = [np.array(w) for w in data["weights"]]
    net.biases = [np.array(b) for b in data["biases"]]
    return net


# plotting costs and accuracies
def plot_costs(eval_costs, train_costs, num_epochs):
    plt.title('Evaluation Cost (EC) and Training Cost (TC)')
    plt.xlabel('Epoch')
    plt.ylabel('Cost')
    epochs = [i for i in range(num_epochs)]
    plt.plot(epochs, eval_costs, label='EC', c='g')
    plt.plot(epochs, train_costs, label='TC', c='b')
    plt.grid()
    plt.autoscale(tight=True)
    plt.legend(loc='best')
    plt.show()


def plot_accuracies(eval_accs, train_accs, num_epochs):
    plt.title('Evaluation Acc (EA) and Training Acc (TC)')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    epochs = [i for i in range(num_epochs)]
    plt.plot(epochs, eval_accs, label='EA', c='g')
    plt.plot(epochs, train_accs, label='TA', c='b')
    plt.grid()
    plt.autoscale(tight=True)
    plt.legend(loc='best')
    plt.show()


# num_nodes -> (eval_cost, eval_acc, train_cost, train_acc)
# use this function to compute the eval_acc and min_cost.
def collect_1_hidden_layer_net_stats(lower_num_hidden_nodes,
                                     upper_num_hidden_nodes,
                                     cost_function,
                                     num_epochs,
                                     mbs,
                                     eta,
                                     lmbda,
                                     train_data,
                                     eval_data):
    # your code here
    # train_d, valid_d, test_d = load_data_wrapper()
    # Best overall: eta=0.2, lambda=0.2, number of nodes=10
    nets_by_nodes = {}
    for n in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
        print("Testing: eta={}, lambda={}, number of nodes={}".format(eta, lmbda, n))
        net = ann([784, n, 10], cost=cost_function)
        net_stats = net.mini_batch_sgd(train_data,
                                       num_epochs, mbs, eta, lmbda=lmbda,
                                       evaluation_data=eval_data,
                                       monitor_evaluation_cost=True,
                                       monitor_evaluation_accuracy=True,
                                       monitor_training_cost=True,
                                       monitor_training_accuracy=True)
        nets_by_nodes[n] = net_stats

    return nets_by_nodes


def testc1(eta_samples=[0.1, 0.2, 0.3, 0.4, 0.5], lmbda_samples=[0.1, 0.2, 0.3, 0.4, 0.5]):
    train_d, valid_d, test_d = load_data_wrapper()
    for x in eta_samples:
        for y in lmbda_samples:
            collect_1_hidden_layer_net_stats(10, 11, CrossEntropyCost, 30, 10, x, y, train_d, test_d)


def collect_2_hidden_layer_net_stats(lower_num_hidden_nodes,
                                     upper_num_hidden_nodes,
                                     cost_function,
                                     num_epochs,
                                     mbs,
                                     eta,
                                     lmbda,
                                     train_data,
                                     eval_data):
    # your code here
    # Best Overall: eta=0.3, lambda=0.5, n1=11, n2=11
    nets_by_nodes = {}
    for x in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
        for y in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
            print("Testing: eta={}, lambda={}, n1={}, n2={}".format(eta, lmbda, x, y))
            net = ann([784, x, y, 10], cost=cost_function)
            net_stats = net.mini_batch_sgd(train_data,
                                           num_epochs, mbs, eta, lmbda=lmbda,
                                           evaluation_data=eval_data,
                                           monitor_evaluation_cost=True,
                                           monitor_evaluation_accuracy=True,
                                           monitor_training_cost=True,
                                           monitor_training_accuracy=True)
            key = "{}_{}".format(x, y)
            nets_by_nodes[key] = net_stats

    return nets_by_nodes


def collect_3_hidden_layer_net_stats(lower_num_hidden_nodes,
                                     upper_num_hidden_nodes,
                                     cost_function,
                                     num_epochs,
                                     mbs,
                                     eta,
                                     lmbda,
                                     train_data,
                                     eval_data):
    # your code here
    # Best Overall: eta=0.3, lambda=0.1, n1=11, n2=10, n3=11
    nets_by_nodes = {}
    for x in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
        for y in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
            for z in range(lower_num_hidden_nodes, upper_num_hidden_nodes + 1):
                print("Testing: eta={}, lambda={}, n1={}, n2={}, n3={}".format(eta, lmbda, x, y, z))
                net = ann([784, x, y, z, 10], cost=cost_function)
                net_stats = net.mini_batch_sgd(train_data,
                                               num_epochs, mbs, eta, lmbda=lmbda,
                                               evaluation_data=eval_data,
                                               monitor_evaluation_cost=True,
                                               monitor_evaluation_accuracy=True,
                                               monitor_training_cost=True,
                                               monitor_training_accuracy=True)
                key = "{}_{}_{}".format(x, y, z)
                nets_by_nodes[key] = net_stats

    return nets_by_nodes


def testc2_and_c3(eta_samples=[0.1, 0.3, 0.5], lmbda_samples=[0.1, 0.3, 0.5]):
    train_d, valid_d, test_d = load_data_wrapper()
    print("Now testing Collect 2...")
    for x in eta_samples:
        for y in lmbda_samples:
            collect_2_hidden_layer_net_stats(10, 11, CrossEntropyCost, 30, 10, x, y, train_d, test_d)
    print("\n\n\nNow testing Collect 3...")
    for x in eta_samples:
        for y in lmbda_samples:
            collect_3_hidden_layer_net_stats(10, 11, CrossEntropyCost, 30, 10, x, y, train_d, test_d)


def save_best_nets():
    DIR_PATH = 'C:/Users/Sanko/Documents/School/IntelligentSystems/hw04/hw04/sols/nets/'
    # Best overall: eta=0.2, lambda=0.2, number of nodes=10
    train_d, valid_d, test_d = load_data_wrapper()
    net1 = ann([784, 10, 10], cost=CrossEntropyCost)
    net1_stats = net1.mini_batch_sgd(train_d, 30, 10, 0.2, lmbda=0.2,
                                     evaluation_data=test_d,
                                     monitor_evaluation_cost=True,
                                     monitor_evaluation_accuracy=True,
                                     monitor_training_cost=True,
                                     monitor_training_accuracy=True)
    net1.save(DIR_PATH + 'net1.json')

    # Best Overall: eta=0.3, lambda=0.5, n1=11, n2=11
    net2 = ann([784, 11, 11, 10], cost=CrossEntropyCost)
    net2_stats = net2.mini_batch_sgd(train_d, 30, 10, 0.3, lmbda=0.5,
                                     evaluation_data=test_d,
                                     monitor_evaluation_cost=True,
                                     monitor_evaluation_accuracy=True,
                                     monitor_training_cost=True,
                                     monitor_training_accuracy=True)
    net2.save(DIR_PATH + 'net2.json')

    # Best Overall: eta=0.3, lambda=0.1, n1=11, n2=10, n3=11
    net3 = ann([784, 11, 10, 11, 10], cost=CrossEntropyCost)
    net3_stats = net3.mini_batch_sgd(train_d, 30, 10, 0.3, lmbda=0.1,
                                     evaluation_data=test_d,
                                     monitor_evaluation_cost=True,
                                     monitor_evaluation_accuracy=True,
                                     monitor_training_cost=True,
                                     monitor_training_accuracy=True)
    net3.save(DIR_PATH + 'net3.json')
    pass

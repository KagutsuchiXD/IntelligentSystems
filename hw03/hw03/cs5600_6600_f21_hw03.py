#/usr/bin/python

from ann import ann
from mnist_loader import load_data_wrapper


train_d, valid_d, test_d = load_data_wrapper()

HLS = [10, 25, 50]
ETA = [0.5, 0.25, 0.125]


def train_1_hidden_layer_anns(hls=HLS, eta=ETA, mini_batch_size=10, num_epochs=10):
    for x in HLS:
        for y in ETA:
            print('\n*** Training 784x{}x10 ANN with eta= {} '.format(x, y))
            net = ann([784, x, 10])
            # net.mini_batch_sgd(train_d, epoch, batch, learnrate, test_data=test_d)
            net.mini_batch_sgd(train_d, num_epochs, mini_batch_size, y, test_data=test_d)
            print('\n*** Training 784x{}x10 ANN with eta={} DONE!'.format(x, y))


def train_2_hidden_layer_anns(hls=HLS, eta=ETA, mini_batch_size=10, num_epochs=10):
    # your code here
    for w in HLS:
        for x in HLS:
            for y in ETA:
                print('\n*** Training 784x{}x{}x10 ANN with eta= {} '.format(w, x, y))
                net = ann([784, w, x, 10])
                # net.mini_batch_sgd(train_d, epoch, batch, learnrate, test_data=test_d)
                net.mini_batch_sgd(train_d, num_epochs, mini_batch_size, y, test_data=test_d)
                print('\n*** Training 784x{}x{}x10 ANN with eta={} DONE!'.format(w, x, y))
    pass


# Uncomment to run
if __name__ == '__main__':
    train_1_hidden_layer_anns(hls=HLS, eta=ETA, mini_batch_size=10, num_epochs=10)
    train_2_hidden_layer_anns(hls=HLS, eta=ETA, mini_batch_size=10, num_epochs=10)
    pass

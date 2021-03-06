import gzip
import cPickle as pickle


def load(filename):
    with gzip.open(filename) as f:
        train_set, valid_set, test_set = pickle.load(f)
        return ((train_set[0] > 0.5, train_set[1]),
                (valid_set[0] > 0.5, valid_set[1]),
                (test_set[0] > 0.5, test_set[1]))

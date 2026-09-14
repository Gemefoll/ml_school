import numpy as np


def prod_non_zero_diag(x: np.ndarray):
    xd = x.diagonal()
    return np.where(xd != 0, xd, 1).prod()


def are_multisets_equal(x, y):
    return (np.sort(x) == np.sort(y))[0]


def max_after_zero(x: np.ndarray):
    return (x[1:]).compress(x[:-1] == 0).max()


def convert_image(img, coefs):
    return (img @ coefs[:, np.newaxis]).sum(axis=-1).round().astype(np.uint8)


def run_length_encoding(x: np.ndarray):
    dat = np.r_[True, x[1:] != x[:-1]]
    return x[dat], np.diff(np.r_[dat, x.size])


def pairwise_distance(x, y):
    return ((x[:, np.newaxis] - y[np.newaxis, :]) ** 2).sum(axis=-1) ** 0.5
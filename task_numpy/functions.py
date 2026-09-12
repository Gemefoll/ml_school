from math import inf


def prod_non_zero_diag(x):
    prod = 1
    for i in range(min(len(x), len(x[0]))):
        prod *= 1 if x[i][i] == 0 else x[i][i]
    return prod


def are_multisets_equal(x, y):
    return sorted(x) == sorted(y)


def max_after_zero(x):
    mx = -inf
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            mx = max(mx, x[i])
    return mx


def convert_image(img, coefs):
    return [
        [
            round(
                img[i][j][0] * coefs[0]
                + img[i][j][1] * coefs[1]
                + img[i][j][2] * coefs[2]
            )
            for j in range(len(img[i]))
        ]
        for i in range(len(img))
    ]


def run_length_encoding(x):
    ans1 = [x[0]]
    ans2 = [0]
    for i in x:
        if i == ans1[-1]:
            ans2[-1] += 1
        else:
            ans1.append(i)
            ans2.append(1)
    return ans1, ans2


def pairwise_distance(x, y):
    return [
        [
            (sum((x[i][k] - y[j][k]) ** 2 for k in range(len(x[i])))) ** 0.5
            for j in range(len(y))
        ]
        for i in range(len(x))
    ]
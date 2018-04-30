from hash import sha256, md5
from kmv import kmin, simulate


def count_small_errors(errors):
    small_errors = [x for x in errors if abs(x - 1) < 0.1]
    percent = len(small_errors) / len(errors) * 100
    print("Small errors {}, total errors {}, percent {}".format(len(small_errors), len(errors), percent))


N = range(1, 10001)
K = [345]

results = simulate(K,N, md5)

count_small_errors(results[0])

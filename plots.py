import hashlib
import matplotlib.pyplot as pyplot

from hash import md5, sha256


# def kmin(k, h, M):
#     hashes = prepare_hashes(h, M)
#
#     # print("normalized hashes {}".format(hashes))
#     mins = [1] * k
#
#     for hash in hashes:
#         # print("comparing hash {} and max hash {}".format(hash, mins[k-1]))
#         if hash < mins[k - 1] and hash not in mins:
#             # print(mins)
#             # print("hash {} is smaller than max hash {} and not in set".format(hash, mins[k - 1]))
#             mins[k - 1] = hash
#             mins.sort()
#
#     # print("Hashes: {}, mins: {}".format(hashes, mins))
#     # print("How much hashes: {}, ones: {}".format(len(hashes), mins.count(1)))
#     # print("Max: {}".format(max(mins)))
#
#     if mins[k - 1] == 1:
#         return len(hashes) - mins.count(1)
#     else:
#         return (k - 1) / max(mins)
from kmv import kmin, simulate

# def normalize(values):
#     # print("data to normalize {}".format(values))
#     return [(x - min(values)) / (max(values) - min(values)) for x in values]
#
#


N = range(1, 1001)
K = [2, 3, 10, 100, 400]

# k = 325 - 95%

results = simulate(K, N, md5)

for i in range(len(K)):

    pyplot.plot(N, results[i], "b.")
    pyplot.show()

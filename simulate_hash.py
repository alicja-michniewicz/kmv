from kmv import simulate, count_small_errors
from hash import *

H = [sha1, pearson_64, sha256, shake128_8, shake256_16, shake256_32, shake256_64, shake256_128, shake256_256, blake2b, md5, sha3_224, sha3_256, sha3_512]

K = [100]
N = range(2,1000)

for h in H:
    results = simulate(K, N, h)

    for result in results:
        print("h {}".format(h.__name__))
        count_small_errors(result)

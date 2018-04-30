import random


def prepare_hashes(h, M):
    hashes = [h(m) for m in M]
    # return normalize(hashes)
    return hashes


def count_small_errors(errors):
    small_errors = [x for x in errors if abs(x - 1) < 0.1]
    percent = len(small_errors) / len(errors) * 100
    print("Small errors {}, total errors {}, percent {}".format(len(small_errors), len(errors), percent))

def normalize(hashes):

    if len(hashes) == 1:
        return [random.uniform(0, 1)]

    minimum = min(hashes)
    maximum = max(hashes)

    return [(x - minimum) / (maximum - minimum) for x in hashes]

def kmin(k, h, M):
    hashes = prepare_hashes(h, M)

    # print("normalized hashes count {}".format(len(hashes)))
    # print("normalized hashes {}".format(hashes))
    mins = hashes[:k]

    counter = 0

    for hash in hashes:
        counter += 1
        maximum = max(mins)
        # print("comparing hash {} and max hash. Counter {}".format(hash, counter))
        if hash < maximum and hash not in mins:
            # print(mins)
            # print("hash {} is smaller than max hash {} and not in set".format(hash, mins[k - 1]))
            mins.remove(maximum)
            mins.append(hash)

    # print("Hashes: {}, mins: {}".format(hashes, mins))
    # print("How much hashes: {}, ones: {}".format(len(hashes), mins.count(1)))
    # print("Max: {}".format(max(mins)))

    return (k - 1) / max(mins)


def simulate(K, N, h):
    results = []

    divided_ns = []
    i = 1

    for n in N:
        ns = []

        for _ in range(n):
            ns.append(i)
            i += 1

        divided_ns.append(ns)

    for k in K:
        errors = []
        for i in range(len(N)):
            estimate = kmin(k, h, [str(j) for j in divided_ns[i]])
            errors.append(estimate / N[i])

        results.append(errors)

    return results

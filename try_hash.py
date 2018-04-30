from hash import *
from kmv import kmin

print(hashlib.algorithms_available)


# distinct_values = kmin(100, ripemd160, [str(i) for i in range(1001)])
# print(distinct_values)

print("SHA 256")
distinct_values = kmin(100, sha256, [str(i) for i in range(10000)])
print(distinct_values)

print("MD5")
distinct_values = kmin(100, md5, [str(i) for i in range(10000)])
print(distinct_values)


print("SHAKE 256 B 64")
distinct_values = kmin(100, shake256_64, [str(i) for i in range(10000)])
print(distinct_values)

print("SHAKE 256 B 128")
distinct_values = kmin(100, shake256_128, [str(i) for i in range(10000)])
print(distinct_values)

print("SHAKE 256 B 256")
distinct_values = kmin(100, shake256_256, [str(i) for i in range(10000)])
print(distinct_values)

print("SHAKE 256 B 256")
distinct_values = kmin(100, shake256_256, [str(i) for i in range(10000)])
print(distinct_values)
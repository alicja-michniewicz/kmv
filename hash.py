import hashlib
from pearhash import PearsonHasher


def md5(element):
    return int.from_bytes(hashlib.md5(element.encode()).digest(), 'big') / (1 << 128)


def sha256(element):
    return int.from_bytes(hashlib.sha256(element.encode()).digest(), 'big') / (1 << 256)

def sha1(element):
    return int.from_bytes(hashlib.sha1(element.encode()).digest(), 'big') / (1 << 160)


def pearson_64(element):
    hasher = PearsonHasher(int(64 / 8))  # Set desired hash length in bytes.
    return int(hasher.hash(element.encode()).hexdigest(), 16) / (1 << 64)


# def ripemd160(element):
#     h = hashlib.new('RIPEMD160')
#     return int.from_bytes(h.update(element.encode()).digest(), 'big') / (1 << 160)

def shake128_8(element):
    return int.from_bytes(hashlib.shake_128(element.encode()).digest(1), 'big') / (1 << 9 - 1)


def shake256_16(element):
    return int.from_bytes(hashlib.shake_256(element.encode()).digest(int(16 / 8)), 'big') / (1 << 17 - 1)


def shake256_32(element):
    return int.from_bytes(hashlib.shake_256(element.encode()).digest(int(32 / 8)), 'big') / (1 << 32)


def shake256_64(element):
    return int.from_bytes(hashlib.shake_256(element.encode()).digest(int(64 / 8)), 'big') / (1 << 64)


def shake256_128(element):
    return int.from_bytes(hashlib.shake_256(element.encode()).digest(int(128 / 8)), 'big') / (1 << 128)


def shake256_256(element):
    return int.from_bytes(hashlib.shake_256(element.encode()).digest(int(256 / 8)), 'big') / (1 << 256)


def blake2b(element):
    return int.from_bytes(hashlib.blake2b(element.encode()).digest(), 'big') / (1 << 512)


def blake2s(element):
    return int.from_bytes(hashlib.blake2s(element.encode()).digest(), 'big') / (1 << 256)


def sha3_224(element):
    return int.from_bytes(hashlib.sha3_224(element.encode()).digest(), 'big') / (1 << 224)


def sha3_256(element):
    return int.from_bytes(hashlib.sha3_256(element.encode()).digest(), 'big') / (1 << 256)


def sha3_512(element):
    return int.from_bytes(hashlib.sha3_512(element.encode()).digest(), 'big') / (1 << 512)


def whirlpool(element):
    h = hashlib.new('whirlpool')
    return int.from_bytes(h.digest(), 'big') / (1 << 512)

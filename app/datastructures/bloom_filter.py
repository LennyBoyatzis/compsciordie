import hashlib


class BloomFilter(set):
    def __init__(self, size=10000, hash_fns=[]):
        super(BloomFilter, self).__init__()
        self.size = size
        self.store = [0] * size
        self.hash_fns = hash_fns

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.store)

    def get_idx(self, fn, item):
        hashval = fn(item.encode('utf-8')).digest()
        hashint = int.from_bytes(hashval, byteorder='big')
        return hashint % self.size

    def add(self, item):
        for fn in self.hash_fns:
            idx = self.get_idx(fn, item)
            self.store[idx] = 1

    def __contains__(self, item):
        return all([self.store[self.get_idx(fn, item)]
                    for fn in self.hash_fns])


if __name__ == '__main__':
    m1 = hashlib.md5
    m2 = hashlib.sha1
    m3 = hashlib.sha224

    hash_fns = [m1, m2, m3]
    bfilter = BloomFilter(hash_fns=hash_fns)

    bfilter.add('carrot')
    print('carrot' in bfilter)

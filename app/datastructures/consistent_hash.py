import sys


class ConsistentHash:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self, key):
        pass


if __name__ == '__main__':
    ips = [
      '17.41.226.116',
      '69.223.63.24',
      '3.68.196.59',
      '104.43.45.206',
      '93.42.41.96',
      '73.64.241.153',
      '136.81.226.104',
      '161.131.67.73',
      '184.34.5.150',
      '99.196.98.21']

    for ip in ips:
        hashed = hash(ip) / sys.maxsize
        mapping = abs(int(hashed * 256))
        print(f'what is the mapping {mapping}')

    hash_ring = ConsistentHash(5)

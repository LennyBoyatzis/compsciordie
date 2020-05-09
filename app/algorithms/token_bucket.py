from time import time, sleep


class TokenBucket():
    """Implementation of the token bucket algorithm"""
    def __init__(self, tokens, fill_rate):
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = float(fill_rate)
        self.timestamp = time()

    def consume(self, tokens):
        """Returns True if sufficient tokens else False"""
        if tokens <= self.tokens:
            self._tokens -= tokens
        else:
            return False
        return True

    def get_tokens(self):
        if self._tokens < self.capacity:
            now = time()
            delta = self.fill_rate * (now - self.timestamp)
            self._tokens = min(self.capacity, self._tokens + delta)
            self.timestamp = now
        return self._tokens
    tokens = property(get_tokens)


if __name__ == '__main__':
    bucket = TokenBucket(80, 1)
    print(f'tokens {bucket.tokens}')
    print(f'consume(10) {bucket.consume(10)}')
    print(f'consume(10) {bucket.consume(10)}')
    sleep(1)
    print(f'tokens {bucket.tokens}')
    sleep(1)
    print(f'tokens {bucket.tokens}')
    print(f'consume(90) {bucket.consume(90)}')
    print(f'tokens {bucket.tokens}')

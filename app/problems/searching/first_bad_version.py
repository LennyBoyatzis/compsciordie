class API:
    def __init__(self, n, first_bad_version):
        self.response = [False if i < first_bad_version else True for i in range(1, n+1)]

api = API(10, 3)

print(f'api.response {api.response}')

def is_bad_version(n):
    return api.response[n]


def first_bad_version(n):
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2

        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    
    return left


if __name__ == '__main__':
    n = 10
    res = first_bad_version(n)
    print(f'res {res}')

def num_tile_possibilities(tiles):
    res = set()

    def backtrack(path, t):
        if path not in res:
            if path:
                print(f'path {path}')
                res.add(path)

            for i in range(len(t)):
                backtrack(path+t[i], t[:i] + t[i+1:])

    backtrack('', tiles)
    return len(res)


if __name__ == '__main__':
    tiles = 'AAB'
    result = num_tile_possibilities(tiles)
    print(f'result {result}')

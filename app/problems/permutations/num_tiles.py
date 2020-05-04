def num_tile_possibilities(tiles):
    res = set()

    def dfs(path, t):
        if path:
            res.add(path)

        for i in range(len(t)):
            dfs(path+t[i], t[:i] + t[i+1:])

    dfs('', tiles)
    return len(res)


def num_tiles_poss(tiles):
    res = {''}

    for c in tiles:
        res |= {d[:i] + c + d[i:] for d in res for i in range(len(d) + 1)}
    return len(res) - 1


if __name__ == '__main__':
    tiles = "AAABBC"
    result = num_tiles(tiles)
    print(f'what is the result {result}')

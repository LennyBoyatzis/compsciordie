def countdown(n):
    if n == 0:
        return []
    else:
        test = []
        res = countdown(n-1)
        res.append(n)
        return res

res = countdown(5, test)
print(f'res {res}')

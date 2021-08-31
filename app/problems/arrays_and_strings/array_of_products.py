def array_of_products(array):
    left = [1]*len(array)
    right = [1]*len(array)

    if len(array) == 1:
        return [1]
    elif len(array) == 2:
        return [array[1], array[0]]

    left[1] = array[0]

    for i in range(1, len(array)):
        left[i] = left[i-1]*array[i-1]

    right[-2] = array[-1]

    for j in range(len(right)-2, -1, -1):
        right[j] = right[j+1]*array[j+1]

    ans = []

    for i in range(len(array)):
        ans.append(left[i]*right[i])
    return ans

if __name__ == '__main__':
    array = [5, 1, 4, 2]
    res = array_of_products(array)
    print(f'res {res}')

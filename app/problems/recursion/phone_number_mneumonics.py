def phone_number_mneumonics(phone_num):
    num_map = {
        '1': '1',
        '0': '0',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}

    options = []

    def build_mneumonics(phone_num, i, path):
        if i == len(phone_num):
            options.append(path)
            return

        digit = phone_num[i]
        chars = num_map[digit]

        for option in chars:
            build_mneumonics(phone_num, i+1, path+option)

    build_mneumonics(phone_num, 0, '')
    return options

if __name__ == '__main__':
    phone = '1905'
    res = phone_number_mneumonics(phone)
    print(f'res -> {res}')

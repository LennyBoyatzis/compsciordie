def valid_starting_city(distances, fuel, mpg):
    num_cities = len(distances)
    miles_left = 0

    start_idx = 0
    miles_left_at_start = 0

    for city_idx in range(1, num_cities):
        dist_from_prev = distances[city_idx - 1]
        fuel_from_prev = fuel[city_idx - 1]
        miles_left += fuel_from_prev * mpg - dist_from_prev

        if miles_left < miles_left_at_start:
            miles_left_at_start = miles_left
            start_idx = city_idx
    return start_idx


if __name__ == '__main__':
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    res = valid_starting_city(distances, fuel, mpg)
    print(f'res {res}')

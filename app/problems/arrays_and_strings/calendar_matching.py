from typing import List


def add_cal_bounds(cal, bounds):
    start, end = bounds
    cal.insert(0, ['0:00', start])
    cal.append([end, '23:59'])
    return cal


def merge_cals(c1, c2):
    merged = []
    p1, p2 = 0, 0

    while p1 < len(c1) and p2 < len(c2):
        next_c1, next_c2 = c1[p1], c2[p2]

        if next_c1[0] <= next_c2[0]:
            merged.append(next_c1)
            p1 += 1
        else:
            merged.append(next_c2)
            p2 += 1

    if p1 < len(c1):
        merged.extend(c1[p1:])

    if p2 < len(c2):
        merged.extend(c2[p2:])

    return merged


def flatten(merged_cal):
    flat_cal = [merged_cal[0]]

    for i in range(1, len(merged_cal)):
        prev_start, prev_end = flat_cal[-1]
        next_start, next_end = merged_cal[i]

        if next_start <= prev_end:
            flat_cal[-1] = [prev_start, max(prev_end, next_end)]
        else:
            flat_cal.append([next_start, next_end])
    return flat_cal


def convert_time_to_int(time_str):
    hours, mins = time_str.split(':')
    return int(hours) * 60 + int(mins)

def convert_int_to_time(int):
    hours, mins = divmod(int, 60)
    mins_prefix = '0' if mins < 10 else ''
    return f'{hours}:{mins_prefix}{mins}'

def convert_cal_to_ints(cal):
    return [[convert_time_to_int(start),
             convert_time_to_int(end)] for start, end in cal]

def convert_cal_to_time(cal):
    return [[convert_int_to_time(start),
             convert_int_to_time(end)] for start, end in cal]

def get_free_time(flat_cal, duration):
    free_time = []

    for i in range(1, len(flat_cal)):
        prev_start, prev_end = flat_cal[i-1]
        next_start, next_end = flat_cal[i]

        # 60 mins interval
        # 15 mins duration
        interval = next_start - prev_end
        chunks = interval // duration
        current = prev_end

        for i in range(chunks):
            free_time.append([current, current+duration])
            current += duration

    return free_time


def calendar_matching(c1, db1, c2, db2, duration):
    c1 = add_cal_bounds(c1, db1)
    c2 = add_cal_bounds(c2, db2)

    c1 = convert_cal_to_ints(c1)
    c2 = convert_cal_to_ints(c2)

    merged_cal = merge_cals(c1, c2)
    flat_cal = flatten(merged_cal)

    free_time = get_free_time(flat_cal, duration)
    free_time = convert_cal_to_time(free_time)

    return free_time


if __name__ == '__main__':
    c1 = [
        ["9:00", "10:30"],
        ["12:00", "13:00"],
        ["16:00", "18:00"]]

    db1 = ["9:00", "20:00"]

    c2 = [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]]

    db2 = ["10:00", "18:30"]

    duration = 30 

    res = calendar_matching(c1, db1, c2, db2, duration)

from typing import List


Time = str
Meeting = List[Time]
Bounds = List[Time]
Calendar = List[Meeting]


def merge_intervals(c1: Calendar, c2: Calendar) -> Calendar:
    """Merges two calendars together and returns as output"""
    merged = []
    p1, p2 = 0, 0
    c1_size, c2_size = len(c1), len(c2)

    while p1 < c1_size and p2 < c2_size:
        if c1[p1][0] <= c2[p2][0]:
            if not merged:
                merged.append(c1[0])
            else:
                if c1[[p1]][0] < merged
            p1 += 1
        else:
            merged.append(c2[0])
            p2 += 1


def time_to_mins(time: Time) -> int:
    """Converts 24hr time string to minutes from 00:00"""
    hours, mins = [int(part) for part in time.split(':')]
    return hours * 60 + mins


def mins_to_time(mins: int) -> Time:
    """Converts mins to 24hr time string"""
    hrs, mins = divmod(mins, 60)
    mins_prefix = '0' if mins < 10 else ''
    return f'{hrs}:{mins_prefix}{mins}'


def split_by_duration(start: Time, end: Time, duration: int) -> Calendar:
    """Splits time block into intervals of duration"""
    start_mins, end_mins = time_to_mins(start), time_to_mins(end)
    intervals = []

    for i in range(start_mins, end_mins, duration):
        intervals.append([i, i+duration])
    
    return intervals


def convert_meeting_to_mins(meeting: Meeting) -> Meeting:
    """Converts a meeting to minutes"""


def calendar_matching(c1, db1, c2, db2) -> Calendar:
    """Finds available time slots between 2 calendars"""

    c1_mins, c2_mins = [], []

    for meeting in c1:
        start_time, end_time = meeting 
        c1_mins.append([time_to_mins(start_time), time_to_mins(end_time)])

    for meeting in c2:
        start_time, end_time = meeting
        c2_mins.append([time_to_mins(start_time), time_to_mins(end_time)])

    print(f'c1_mins {c1_mins}')
    print(f'c2_mins {c2_mins}')
    # test = split_by_duration('9:00', '16:00', 30)
    test = merge_intervals(c1_mins, c2_mins)
    print(f'test {test}')


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

    res = calendar_matching(c1, db1, c2, db2)

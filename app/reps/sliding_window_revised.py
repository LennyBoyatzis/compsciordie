from collections import deque

# Fixed length sliding windows
def sliding_window(array):
    window_size = 3
    left, right = 0, 0
    window = deque([])

    while right < len(array):
        if len(window) < window_size:
            window.append(array[right])
        else:
            window.popleft()
            window.append(array[right])
        right +=1
        print(window)


def sliding_window(array):
    window_size = 3
    left, right = 0, 0

    while right < len(array):
        if right - left < window_size:
            right += 1
        else:
            right += 1
            left += 1
        print(array[left:right])


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sliding_window(array)

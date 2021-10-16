def build_output(max_index, sequences, disks):
    output = []
    curr_index = max_index

    while curr_index:
        disk = disks[curr_index]
        output.append(disk)
        curr_index = sequences[curr_index]

    return output[::-1]


# Runtime O(n^2)
# Space O(n)
def stack_disks(disks):
    disks.sort(key=lambda x: x[2])
    max_heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]

    for i in range(1, len(disks)):
        curr = disks[i]
        w_c, d_c, h_c = curr

        for j in range(0, i):
            prev = disks[j]
            w_p, d_p, h_p = prev

            if w_c > w_p and d_c > d_p and h_c > h_p:
                if max_heights[j] + h_c > max_heights[i]:
                    max_heights[i] = max_heights[j] + h_c
                    sequences[i] = j
                else:
                    max_heights[i] = max_heights[i]

    max_height = max(max_heights)
    max_index = max_heights.index(max_height)
    ans = build_output(max_index, sequences, disks)
    return ans


if __name__ == '__main__':
    disks = [
      [2, 1, 2],
      [3, 2, 3],
      [2, 2, 8],
      [2, 3, 4],
      [1, 3, 1],
      [4, 4, 5]]
    ans = stack_disks(disks)
    print(f'ans {ans}')

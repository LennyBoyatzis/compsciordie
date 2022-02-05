# Bottom Up DFS

# manager = [1, 2, 3, 4, 5, 6, -1]
# inform_time = [0, 6, 5, 4, 3, 2, 1]

# i =  
# manager[i] = 1
# inform_time[i] = 0

# From every node in the tree we traverse it and calculate the inform time
# until we reach the parent


def num_of_mins(n, head_id, manager, inform_time):
    def dfs(i):
        if manager[i] != -1:
            inform_time[i] += dfs(manager[i])
            manager[i] = -1
        return inform_time[i]
    return max(map(dfs, range(n)))


def num_of_mins(n, head_id, manager, inform_time):
    children = [[] for i in range(n)]

    for i, m in enumerate(manager):
        if m >= 0:
            children[m].append(i)

    def dfs(i):
        return max([dfs(j) for j in children[i]] or [0]) + inform_time[i]

    return dfs(head_id)



if __name__ == '__main__':
    n = 7
    head_id = 6
    manager = [1, 2, 3, 4, 5, 6, -1]
    inform_time = [0, 6, 5, 4, 3, 2, 1]
    res = num_of_mins(n, head_id, manager, inform_time)
    print(f'res {res}')

import numpy as np

maze_shape = (17, 37)
maze = np.zeros(maze_shape)

for i in range(maze_shape[0]):
    print('\n')
    for j in range(maze_shape[1]):
        index = i * maze_shape[1] + j
        if index % 7 == 0 or index % 13 == 0 or index % 17 == 0:
            maze[i, j] = 1
            print('#', end="")
        else:
            print('.', end="")


start = (maze_shape[0] - 1, 0)
end = (0, maze_shape[1] - 1)
maze_visited = maze

def get_adjacent_positions(S):
    adjacent_positions = []
    A1 = (S[0] + 1, S[1])
    A2 = (S[0], S[1] + 1])
    A3 = (S[0] - 1, S[1] + 1)
    if S[0] + 1 >= 0 and S[0] + 1 < maze_shape[0] and maze_visited[:
        adjacent_positions.append((S[0] + 1, S[1]))
    if S[1] + 1 >= 0 and S[1] + 1 < maze_shape[1]:
        adjacent_positions.append((S[0], S[1] + 1))
    if S[0] - 1 >= 0 and S[0] - 1 < maze_shape[0]:
        adjacent_positions.append((S[0] - 1, S[1]))
    if S[1] - 1 >= 0 and S[1] - 1 < maze_shape[1]:
        adjacent_positions.append((S[0], S[1] - 1))
    
    return adjacent_positions


def path_finder(S, E):
    if maze_visited[S] == 1:
        return False
    
    if start == end:
        print(start)
        return True
    
    adjacent_positions = get_adjacent_positions(S)
    for position in adjacent_positions:
        if path_finder(position, E):
            print(position)
            return True
        else:
            maze_visited[position] = 1
    maze_visited[S] = 1

    return False

#path_finder(end, end)
#path_finder(start, end)




def value_count(data, value):
    count = 0
    for i in data:
        for j in i:
            if j == value:
                count += 1
    return count

def value_positions(data, value):
    positions = list()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == value:
                positions.append((i, j))
    return positions